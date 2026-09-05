"""Exercise real gating and custody; injected faults never run unresolved units."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from a2_v0 import model as m, measurement as e, runner as r


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(hasattr(r, 'validate'), 'control-first runner is not implemented')

    def test_01_all_theorem_signatures_before_remaining_invariants(self):
        with tempfile.TemporaryDirectory() as parent:
            out = Path(parent) / 'validation'
            report = r.validate(out)
            self.assertEqual(report['status'], 'PASS')
            self.assertEqual(report['controls_matched'], 64)
            self.assertEqual(report['unresolved_units_executed'], 0)
            self.assertEqual(report['stages'][0], '64_CONTROL_SIGNATURES_MATCHED')
            self.assertEqual(report['stages'][1], 'REMAINING_INVARIANTS_PASSED')
            self.assertEqual(report['source_digest'], r.source_digest())
            records = json.loads((out / 'primary.json').read_text())['units']
            self.assertEqual(len(records), 64)
            self.assertEqual(sum(p['classification'] == 'NULL' for p in records), 8)
            self.assertEqual(sum(p['classification'] == 'EXPANSION' for p in records), 56)
            for p in records:
                self.assertEqual(p['phi_treatment'], list(range(256)))
                self.assertEqual(p['delta_minus'], [])
                if p['unit'][0]:
                    self.assertEqual(p['phi_control'], [0, 1, 2, 4, 8, 16, 32, 64, 128])

    def test_02_control_mismatch_stops_before_invariants_and_unresolved_training(self):
        real_primary, real_train = e.primary_record, r.train_pair
        seen = []

        def corrupt(*args):
            result = real_primary(*args)
            result['phi_treatment'] = []
            return result

        def observe(unit):
            seen.append(unit)
            self.assertLess(unit[0], 8, 'gate leaked an unresolved training unit')
            return real_train(unit)

        with tempfile.TemporaryDirectory() as parent:
            out = Path(parent) / 'run'
            with patch.object(e, 'primary_record', side_effect=corrupt), \
                 patch.object(r, 'train_pair', side_effect=observe), \
                 patch.object(r, 'check_invariants', side_effect=AssertionError('too early')):
                with self.assertRaises(r.ControlMismatch):
                    r.run_unresolved(out)
            self.assertEqual(seen, [(0, 0)])
            self.assertFalse((out / 'primary.json').exists())
            failure = json.loads((out / 'validation' / 'report.json').read_text())
            self.assertEqual(failure['status'], 'CONTROL_MISMATCH')

    def test_03_invariant_failure_stops_before_unresolved_training(self):
        real_train, seen = r.train_pair, []

        def observe(unit):
            seen.append(unit)
            self.assertLess(unit[0], 8, 'invalid gate leaked an unresolved unit')
            return real_train(unit)

        with tempfile.TemporaryDirectory() as parent:
            out = Path(parent) / 'run'
            with patch.object(r, 'train_pair', side_effect=observe), \
                 patch.object(r, 'check_invariants', side_effect=m.InvalidAssay('injected fault')):
                with self.assertRaises(m.InvalidAssay):
                    r.run_unresolved(out)
            self.assertEqual(len(seen), 64)
            self.assertFalse((out / 'primary.json').exists())
            failure = json.loads((out / 'validation' / 'report.json').read_text())
            self.assertEqual(failure['status'], 'INVALID_NO_SCIENTIFIC_RESULT')

    def test_04_output_seals_cannot_overwrite_existing_results(self):
        with tempfile.TemporaryDirectory() as parent:
            path = Path(parent) / 'record.json'
            first_hash = r.seal(path, {'value': 1})
            with self.assertRaises(FileExistsError):
                r.seal(path, {'value': 2})
            self.assertEqual(json.loads(path.read_text()), {'value': 1})
            self.assertEqual(first_hash, r.file_digest(path))

    def test_05_secondary_output_requires_sealed_primary(self):
        # Known control data exercise the future output writer without science.
        pair = r.train_pair((1, 0))
        with tempfile.TemporaryDirectory() as parent:
            out = Path(parent)
            with self.assertRaises(m.InvalidAssay):
                r.seal_utilities(out, [pair], '0' * 64)
            primary_hash = r.seal_primary(out, [pair])
            utility_hash = r.seal_utilities(out, [pair], primary_hash)
            mechanism_hash = r.seal_transplants(out, [pair], utility_hash)
            utility = json.loads((out / 'utilities.json').read_text())
            self.assertEqual(utility['primary_sha256'], primary_hash)
            self.assertEqual(utility['units'][0]['c_improve'], {'numerator': 1, 'denominator': 1})
            self.assertEqual(mechanism_hash, r.file_digest(out / 'transplants.json'))

    def test_06_secondary_output_rejects_changed_primary(self):
        pair = r.train_pair((1, 0))
        with tempfile.TemporaryDirectory() as parent:
            out = Path(parent)
            primary_hash = r.seal_primary(out, [pair])
            with (out / 'primary.json').open('ab') as stream:
                stream.write(b' ')
            with self.assertRaises(m.InvalidAssay):
                r.seal_utilities(out, [pair], primary_hash)
            self.assertFalse((out / 'utilities.json').exists())

    def test_07_paired_training_has_matched_work_and_frozen_evaluation(self):
        pair = r.train_pair((7, 4))
        self.assertTrue(pair.clone_equal)
        self.assertTrue(pair.mutable_disjoint)
        self.assertEqual(pair.treatment.constructor.active, 7)
        self.assertEqual(pair.control.constructor.active, 0)
        for arm in (pair.control, pair.treatment):
            self.assertEqual(arm.training_charge, 40)
            self.assertEqual(arm.hypothesis_checks, 384)
            self.assertTrue(arm.evaluation_unchanged)
            self.assertTrue(all(7 in t['live_after'] for t in arm.trace))

    def test_08_cli_defaults_to_controls_and_validation_only(self):
        with tempfile.TemporaryDirectory() as parent:
            out = Path(parent) / 'validation'
            result = subprocess.run([sys.executable, '-m', 'a2_v0', '--output', str(out)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report['mode'], 'validate')
            self.assertEqual(report['unresolved_units_executed'], 0)


if __name__ == '__main__':
    unittest.main()
