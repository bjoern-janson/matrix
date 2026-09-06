import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from a2_v1.authorities import load_authorities, reconstruct_historical, compile_p3
from a2_v1.engine import Learner, Feedback, execute_paired_cell, stratum
from a2_v1.checks import check_pair
from a2_v1.derived import derive
from a2_v1.runner import validate, run_prospective, InvalidAssay


class AuthoritiesTests(unittest.TestCase):
    def test_pinned_authorities_and_historical_seal(self):
        a = load_authorities()
        self.assertEqual(len(a.priorities), 24)
        self.assertEqual(reconstruct_historical(a)[1], '3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117')

    def test_corruption_stops_loading(self):
        with patch('a2_v1.authorities.EXPECTED', {'contract': '0'*64}):
            with self.assertRaises(InvalidAssay): load_authorities()

    def test_p3_is_independently_compiled(self):
        a = load_authorities()
        hist, _ = reconstruct_historical(a)
        with patch('a2_v1.engine.execute_paired_cell', side_effect=AssertionError('engine used')):
            p3 = compile_p3(a, hist)
        self.assertEqual(len(p3), 320)
        self.assertTrue(all(u[1] == 3 for u in p3))


class EngineTests(unittest.TestCase):
    def test_priority_selection_is_not_numeric_min(self):
        a = load_authorities(); learner = Learner(a.priorities[1], {8, 11})
        self.assertEqual(learner.active, 11)

    def test_invalid_feedback_preserves_live_but_charges_scan(self):
        a = load_authorities(); learner = Learner(a.priorities[0]); before = learner.snapshot()
        work = learner.update((0,0,0), 0, Feedback(False, False))
        self.assertEqual(learner.snapshot(), before); self.assertEqual((work.checks, work.charge), (48,1))

    def test_informative_update_retains_truth(self):
        a = load_authorities(); learner = Learner(a.priorities[1])
        obs = (1,0,1); pred = learner.predict(obs)
        learner.update(obs, pred, Feedback(True, pred == 5))
        self.assertIn(0, learner.live)

    def test_reference_smoke_and_invariants(self):
        a = load_authorities()
        for unit in ((0,0,0),(1,7,2),(8,0,0),(8,3,4)):
            self.assertNotEqual(stratum(unit), 'PROSPECTIVE_TARGET')
            self.assertTrue(all(x['status']=='PASS' for x in check_pair(execute_paired_cell(unit,a))))

    def test_mutations_are_detected(self):
        a=load_authorities(); p=execute_paired_cell((1,1,0),a)
        for field, value in [('training_charge',39),('constructor',{'task':'BAD','active':1})]:
            bad=json.loads(json.dumps(p)); bad['treatment'][field]=value
            with self.assertRaises(InvalidAssay): check_pair(bad)
        bad=json.loads(json.dumps(p)); bad['treatment']['trace'][0]['observations'][0]^=1
        with self.assertRaises(InvalidAssay): check_pair(bad)
        bad=json.loads(json.dumps(p)); bad['treatment']['trace'][0]['live_after'].pop()
        with self.assertRaises(InvalidAssay): check_pair(bad)
        bad=json.loads(json.dumps(p)); bad['treatment']['measurement']['witnesses'][3]=[]
        with self.assertRaises(InvalidAssay): check_pair(bad)


class DerivedTests(unittest.TestCase):
    def test_exact_set_sensitivity_and_distinct_loss_notions(self):
        rows=[]
        for p in range(2):
            for k in range(2):
                minus=[10+p] if k==0 else [10+p,30]
                rows.append({'unit':[8,p,k],'phi_treatment':[0,1+p+k], 'delta_plus':[20] if p else [],'delta_minus':minus})
        d=derive(rows, hypotheses=(8,), priorities=(0,1), rotations=(0,1))
        self.assertEqual(d['E_K']['members'], [[8,0],[8,1]])
        self.assertEqual(d['E_P']['members'], [[8,0],[8,1]])
        self.assertEqual(d['L_any_P']['members'], [[8,0],[8,1]])
        self.assertEqual(d['L_common_P']['members'], [[8,1]])
        self.assertEqual(d['C_P']['8,0'], [])


class RunnerTests(unittest.TestCase):
    def fake(self, unit, authorities):
        return {'unit':list(unit), 'stratum':stratum(unit), 'phi_control':[]}

    def test_validation_never_calls_target_and_is_immutable(self):
        calls=[]
        def fake(u,a): calls.append(u); return self.fake(u,a)
        with tempfile.TemporaryDirectory() as td:
            with patch('a2_v1.runner.execute_paired_cell', side_effect=fake), patch('a2_v1.runner._match_reference', return_value=True), patch('a2_v1.runner.check_pair', return_value=[]):
                r=validate(Path(td)/'run')
            self.assertEqual(r['status'],'PASS'); self.assertEqual(len(calls),2176)
            self.assertFalse(any(stratum(u)=='PROSPECTIVE_TARGET' for u in calls))
            with self.assertRaises(FileExistsError): validate(Path(td)/'run')

    def test_each_gate_mismatch_stops_before_targets(self):
        for failing in ('THEOREM_CONTROL','HISTORICAL_P0','COVARIANCE_P3'):
            calls=[]
            def fake(u,a): calls.append(u); return self.fake(u,a)
            def match(p,e): return p['stratum'] != failing
            with tempfile.TemporaryDirectory() as td:
                with patch('a2_v1.runner.execute_paired_cell',side_effect=fake), patch('a2_v1.runner._match_reference',side_effect=match), patch('a2_v1.runner.check_pair',return_value=[]):
                    with self.assertRaises(InvalidAssay): validate(Path(td)/'x')
                receipt=json.loads((Path(td)/'x'/'receipt.json').read_text())
                self.assertEqual(receipt['status'],'INVALID_NO_SCIENTIFIC_RESULT')
                self.assertEqual(receipt['counters']['PROSPECTIVE_TARGET'],0)

    def test_invariant_mismatch_stops_before_targets(self):
        calls=[]
        def fake(u,a): calls.append(u); return self.fake(u,a)
        with tempfile.TemporaryDirectory() as td:
            with patch('a2_v1.runner.execute_paired_cell',side_effect=fake), patch('a2_v1.runner._match_reference',return_value=True), patch('a2_v1.runner.check_pair',side_effect=InvalidAssay('INVARIANT_MISMATCH')):
                with self.assertRaises(InvalidAssay): validate(Path(td)/'x')
            receipt=json.loads((Path(td)/'x'/'receipt.json').read_text())
            self.assertEqual(receipt['counters']['PROSPECTIVE_TARGET'],0)

    def test_science_repeats_fresh_gate_and_stored_pass_cannot_bypass(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'s'; out.mkdir(); (out/'receipt.json').write_text('{"status":"PASS"}')
            with self.assertRaises(FileExistsError): run_prospective(out)


if __name__ == '__main__': unittest.main()
