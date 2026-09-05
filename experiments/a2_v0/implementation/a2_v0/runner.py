"""Control-first execution. A prior JSON receipt never bypasses fresh gates."""
from copy import deepcopy
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path
import platform
from . import model as m, measurement as e
from .checks import check_invariants


class ControlMismatch(m.InvalidAssay):
    status = 'CONTROL_MISMATCH'


@dataclass(frozen=True, slots=True)
class ArmRun:
    constructor: m.ConstructorInput
    final_live: tuple[int, ...]
    trace: tuple[dict, ...]
    measurement: e.Measurement
    training_charge: int
    hypothesis_checks: int
    evaluation_unchanged: bool


@dataclass(frozen=True, slots=True)
class PairRun:
    unit: tuple[int, int]
    control: ArmRun
    treatment: ArmRun
    clone_equal: bool
    mutable_disjoint: bool


def _train_arm(learner, unit, informative):
    hi, rotation = unit
    trace = []
    training_charge = hypothesis_checks = 0
    for episode in range(8):
        x = (rotation + episode) % 8
        observations = m.channel(m.HYPOTHESES[hi], x)
        before = sorted(learner.live)
        prediction = learner.predict(observations)
        correct = prediction == x
        feedback = m.Feedback(True, correct) if informative else m.Feedback(False, False)
        processing = learner.update(observations, prediction, feedback)
        training_charge += 4 + processing.charge
        hypothesis_checks += processing.hypothesis_checks
        trace.append({'episode': episode, 'x': x, 'query_slots': [0, 1, 2],
                      'observations': list(observations), 'prediction': prediction,
                      'actual_correctness': correct,
                      'feedback': [feedback.valid, feedback.correct],
                      'live_before': before, 'live_after': sorted(learner.live),
                      'active_after': learner.active, 'primitive_charge': 4,
                      'processing_charge': processing.charge,
                      'hypothesis_checks': processing.hypothesis_checks})
    constructor = learner.freeze()
    before_evaluation = learner.snapshot()
    measurement = e.measure(hi, constructor)
    return ArmRun(constructor, tuple(sorted(learner.live)), tuple(trace), measurement,
                  training_charge, hypothesis_checks, learner.snapshot() == before_evaluation)


def train_pair(unit) -> PairRun:
    m.require(unit in m.UNITS, 'unit is outside the frozen universe')
    initial = m.Learner()
    control, treatment = deepcopy(initial), deepcopy(initial)
    equal = control.snapshot() == treatment.snapshot() == initial.snapshot()
    disjoint = (control is not treatment and control.live is not treatment.live
                and control.live is not initial.live and treatment.live is not initial.live)
    m.require(equal and disjoint, 'invalid pre-treatment cloning')
    c = _train_arm(control, unit, False)
    t = _train_arm(treatment, unit, True)
    return PairRun(unit, c, t, equal, disjoint)


def source_digest():
    root = Path(__file__).resolve().parent.parent
    paths = [root / 'PROTOCOL.md']
    paths += sorted((root / 'a2_v0').glob('*.py'))
    paths += sorted((root / 'tests').glob('test_*.py'))
    provenance = root / 'PROVENANCE.json'
    if provenance.exists():
        paths.append(provenance)
    identities = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths}
    return sha256(json.dumps(identities, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def file_digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def seal(path, value):
    path = Path(path)
    payload = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    # Exclusive creation protects prior observations against routine reruns.
    with path.open('xb') as stream:
        stream.write(payload)
    return sha256(payload).hexdigest()


def _require_seal(path, expected):
    path = Path(path)
    m.require(path.is_file() and file_digest(path) == expected,
              'missing or changed preceding endpoint seal: ' + path.name)


def seal_primary(out, pairs):
    records = [e.primary_record(p.unit, p.control.measurement, p.treatment.measurement) for p in pairs]
    return seal(Path(out) / 'primary.json', {'endpoint': 'full_frontier_sets',
                'set_encoding': '8-bit subset mask; bit x denotes state x', 'units': records})


def _rational(value):
    return {'numerator': value.numerator, 'denominator': value.denominator}


def seal_utilities(out, pairs, primary_hash):
    out = Path(out)
    _require_seal(out / 'primary.json', primary_hash)
    units = []
    for p in pairs:
        c, t = e.utility(p.control.measurement), e.utility(p.treatment.measurement)
        units.append({'unit': list(p.unit), 'control': _rational(c), 'treatment': _rational(t),
                      'c_improve': _rational(t - c)})
    return seal(out / 'utilities.json', {'endpoint': 'coupled_deployment_utility',
                'primary_sha256': primary_hash, 'units': units})


def seal_transplants(out, pairs, utility_hash):
    out = Path(out)
    _require_seal(out / 'utilities.json', utility_hash)
    units = []
    for p in pairs:
        if p.control.measurement.frontier == p.treatment.measurement.frontier:
            continue
        hi = p.unit[0]
        onto_treatment = e.measure(hi, m.ConstructorInput(active=p.control.constructor.active))
        onto_control = e.measure(hi, m.ConstructorInput(active=p.treatment.constructor.active))
        matched = (onto_treatment == p.control.measurement and onto_control == p.treatment.measurement)
        m.require(matched, 'transplant violated the constructor information boundary')
        units.append({'unit': list(p.unit), 'both_directions_match': True})
    return seal(out / 'transplants.json', {'standing': 'CONTRACT_CHECK_ONLY',
                'utility_sha256': utility_hash, 'units': units})


def _expected_control(unit):
    full = list(range(256))
    singletons = [0, 1, 2, 4, 8, 16, 32, 64, 128]
    is_null = unit[0] == 0
    return {'unit': list(unit), 'phi_control': full if is_null else singletons,
            'phi_treatment': full,
            'delta_plus': [] if is_null else [s for s in full if s not in singletons],
            'delta_minus': [], 'classification': 'NULL' if is_null else 'EXPANSION'}


def validate(output_directory):
    out = Path(output_directory)
    out.mkdir(parents=True, exist_ok=False)
    fingerprint = source_digest()
    pairs, checks, stages, attempted = [], [], [], []
    try:
        for unit in m.CONTROLS:
            attempted.append(list(unit))
            pair = train_pair(unit)
            observed = e.primary_record(unit, pair.control.measurement, pair.treatment.measurement)
            expected = _expected_control(unit)
            if (observed != expected or pair.treatment.constructor.active != unit[0]
                    or pair.control.constructor.active != 0):
                seal(out / 'control_mismatch.json', {'unit': list(unit),
                     'expected': expected, 'observed': observed,
                     'active_control': pair.control.constructor.active,
                     'active_treatment': pair.treatment.constructor.active})
                raise ControlMismatch('theorem-derived control mismatch at ' + repr(unit))
            pairs.append(pair)
        m.require(len(pairs) == 64, 'not all controls executed')
        stages.append('64_CONTROL_SIGNATURES_MATCHED')
        primary_hash = seal_primary(out, pairs)
        checks = check_invariants(pairs)
        stages.append('REMAINING_INVARIANTS_PASSED')
        utility_hash = seal_utilities(out, pairs, primary_hash)
        # These utilities are theorem-derived control signatures, not new findings.
        for p in pairs:
            m.require(e.utility(p.treatment.measurement) == 1,
                      'treated control utility disagrees with theorem')
            m.require(e.utility(p.control.measurement) == (1 if p.unit[0] == 0 else 0),
                      'untreated control utility disagrees with theorem')
        checks.append({'name': 'exact_rational_control_utilities', 'status': 'PASS'})
        transplant_hash = seal_transplants(out, pairs, utility_hash)
        checks.append({'name': 'bidirectional_transplant_contract', 'status': 'PASS'})
        stages.append('SECONDARY_CONTRACT_CHECKS_PASSED')
        traces_hash = seal(out / 'trajectories.json', {'units': [asdict(p) for p in pairs]})
        m.require(source_digest() == fingerprint, 'source changed during validation')
        report = {'schema': 'a2-v0-validation/1', 'mode': 'validate', 'status': 'PASS',
                  'source_digest': fingerprint, 'python': platform.python_version(),
                  'controls_matched': 64, 'control_units_executed': attempted,
                  'unresolved_units_executed': 0, 'stages': stages, 'checks': checks,
                  'sealed_files': {'primary.json': primary_hash, 'utilities.json': utility_hash,
                                   'transplants.json': transplant_hash, 'trajectories.json': traces_hash}}
        seal(out / 'report.json', report)
        return report
    except Exception as exc:
        failure = {'schema': 'a2-v0-validation/1', 'mode': 'validate',
                   'status': getattr(exc, 'status', 'INVALID_NO_SCIENTIFIC_RESULT'),
                   'reason': str(exc), 'source_digest': fingerprint,
                   'controls_matched': len(pairs), 'control_units_executed': attempted,
                   'unresolved_units_executed': 0, 'stages': stages, 'checks': checks}
        seal(out / 'report.json', failure)
        raise


def run_unresolved(output_directory):
    """Explicit scientific command; always repeats fresh gates before any open unit."""
    out = Path(output_directory)
    out.mkdir(parents=True, exist_ok=False)
    gate = validate(out / 'validation')
    m.require(gate['status'] == 'PASS' and gate['controls_matched'] == 64,
              'control and invariant gate has not passed')
    m.require(source_digest() == gate['source_digest'], 'source changed after gate')
    pairs = []
    try:
        for unit in m.UNRESOLVED:
            pairs.append(train_pair(unit))
        m.require(len(pairs) == 320, 'unresolved unit census is incomplete')
        check_invariants(pairs)
        primary_hash = seal_primary(out, pairs)
        utility_hash = seal_utilities(out, pairs, primary_hash)
        transplant_hash = seal_transplants(out, pairs, utility_hash)
        traces_hash = seal(out / 'trajectories.json', {'units': [asdict(p) for p in pairs]})
        m.require(source_digest() == gate['source_digest'], 'source changed during execution')
        report = {'schema': 'a2-v0-run/1', 'mode': 'run-unresolved', 'status': 'COMPLETE',
                  'source_digest': gate['source_digest'], 'python': platform.python_version(),
                  'unresolved_units_executed': len(pairs),
                  'validation_sha256': file_digest(out / 'validation' / 'report.json'),
                  'sealed_files': {'primary.json': primary_hash, 'utilities.json': utility_hash,
                                   'transplants.json': transplant_hash, 'trajectories.json': traces_hash}}
        seal(out / 'report.json', report)
        return report
    except Exception as exc:
        seal(out / 'report.json', {'schema': 'a2-v0-run/1',
             'status': getattr(exc, 'status', 'INVALID_NO_SCIENTIFIC_RESULT'), 'reason': str(exc),
             'unresolved_units_completed': len(pairs), 'scientific_interpretation': 'NOT_ADMITTED'})
        raise
