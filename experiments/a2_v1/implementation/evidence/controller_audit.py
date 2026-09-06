"""External verification observer; never authorizes a prospective pair.

This uses an independently compiled, hash-checked reference file. It observes
the actual implementation boundary and invokes the normal validation CLI.
It is not imported by the implementation and changes no source file.
"""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import runpy
import sys
import unittest

FIELDS = ('unit', 'stratum', 'phi_control', 'phi_treatment', 'delta_plus', 'delta_minus')
REFERENCE_SHA256 = '54ab95996fb33a7cdc1c8b460cdd634701a6b4a6b528c50930aa90594086950f'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('tests', 'validate'))
    parser.add_argument('--implementation', type=Path, required=True)
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--audit', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.mode == 'validate' and args.output is None:
        parser.error('--output is required for validation')
    reference_bytes = args.reference.read_bytes()
    if sha256(reference_bytes).hexdigest() != REFERENCE_SHA256:
        raise RuntimeError('Independent reference artifact identity mismatch')
    reference = {tuple(r['unit']): r for r in json.loads(reference_bytes)['units']}
    phase_order = ('THEOREM_CONTROL', 'HISTORICAL_P0', 'COVARIANCE_P3')
    ordered = [u for phase in phase_order for u in sorted(reference)
               if reference[u]['stratum'] == phase]
    assert len(ordered) == len(reference) == 2176
    sys.path.insert(0, str(args.implementation.resolve()))
    from a2_v1 import engine, runner
    actual_pair = engine.execute_paired_cell
    calls, completed, matched, forbidden = [], [], [], []

    def observed_pair(unit, *positional, **keyword):
        u = tuple(unit)
        if u not in reference:
            forbidden.append(u)
            raise RuntimeError('EXTERNAL_AUDIT_BLOCKED_NONREFERENCE_PAIR: ' + str(u))
        if args.mode == 'validate' and (len(calls) >= len(ordered) or u != ordered[len(calls)]):
            raise RuntimeError('EXTERNAL_AUDIT_PHASE_OR_UNIT_ORDER_MISMATCH: ' + str(u))
        calls.append(u)
        pair = actual_pair(unit, *positional, **keyword)
        completed.append(u)
        projection = {field: pair.get(field) for field in FIELDS}
        same = projection == reference[u]
        if args.mode == 'validate':
            encode = lambda value: json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)
            same = encode(projection) == encode(reference[u])
        if not same and args.mode == 'validate':
            raise RuntimeError('EXTERNAL_AUDIT_ENDPOINT_MISMATCH: ' + str(u))
        if same:
            matched.append(u)
        return pair

    engine.execute_paired_cell = observed_pair
    runner.execute_paired_cell = observed_pair
    status, error, software_tests = 'INVALID', None, None
    try:
        if args.mode == 'tests':
            suite = unittest.defaultTestLoader.discover(str(args.implementation / 'tests'))
            result = unittest.TextTestRunner(verbosity=2).run(suite)
            software_tests = {'run': result.testsRun, 'failures': len(result.failures),
                              'errors': len(result.errors), 'skipped': len(result.skipped)}
            if not result.wasSuccessful():
                raise RuntimeError('Software suite failed')
        else:
            sys.argv = ['a2_v1', 'validate', '--output', str(args.output.resolve())]
            try:
                runpy.run_module('a2_v1', run_name='__main__')
            except SystemExit as exc:
                if exc.code not in (None, 0):
                    raise
            receipt = json.loads((args.output / 'receipt.json').read_bytes())
            if receipt['status'] != 'PASS':
                raise RuntimeError('Validation did not report PASS')
            if calls != ordered or completed != ordered or matched != ordered:
                raise RuntimeError('Actual validation call coverage mismatch')
        if forbidden:
            raise RuntimeError('Forbidden pair attempts observed')
        status = 'PASS'
    except BaseException as exc:
        error = type(exc).__name__ + ': ' + str(exc)
        raise
    finally:
        evidence = {
            'schema': 'a2-v1-external-call-and-reference-audit/1',
            'mode': args.mode, 'status': status, 'error': error,
            'observer_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
            'independent_reference_sha256': REFERENCE_SHA256,
            'actual_pair_entries': len(calls), 'actual_completed_pairs': len(completed),
            'independently_matching_endpoints': len(matched),
            'unique_reference_units': len(set(calls)),
            'stratum_call_counts': dict(Counter(reference[u]['stratum'] for u in calls)),
            'forbidden_pair_attempts': [list(u) for u in forbidden],
            'prospective_pairs_executed': 0,
            'actual_unit_sequence': [list(u) for u in calls],
            'software_tests': software_tests,
        }
        args.audit.parent.mkdir(parents=True, exist_ok=True)
        with args.audit.open('x') as f:
            json.dump(evidence, f, sort_keys=True, separators=(',', ':'))
            f.write('\n')


if __name__ == '__main__':
    main()
