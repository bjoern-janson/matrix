import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from a2_v1 import runner, engine, authorities
from a2_v1.checks import check_pair

class ReviewRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=authorities.load_authorities()
        cls.pair=engine.execute_paired_cell((1,1,0),cls.a)

    def test_disconnected_or_falsified_trajectory_rejected(self):
        mutations=[
            lambda p:p['control']['trace'][0]['live_before'].pop(),
            lambda p:p['treatment']['trace'][1].update(live_before=list(range(48))),
            lambda p:p['treatment'].update(final_live=list(range(48))),
            lambda p:p['treatment']['constructor'].update(active=0),
            lambda p:p['treatment']['trace'][0].update(prediction=7),
            lambda p:p['treatment']['trace'][0].update(actual_correctness=True),
            lambda p:p['treatment']['trace'][0].update(processing_charge=2),
            lambda p:p['treatment']['trace'][0].update(hypothesis_checks=47),
            lambda p:p['treatment'].update(priority_order=list(range(48))),
            lambda p:p['treatment'].pop('priority_order'),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                p=copy.deepcopy(self.pair); mutate(p)
                with self.assertRaises(engine.InvalidAssay): check_pair(p)

    def test_execution_and_complete_witness_linkage(self):
        mutations=[
            lambda p:p['control']['measurement']['executions'][8][0]['observations'].__setitem__(0,0),
            lambda p:p['control']['measurement']['executions'][0][0]['actions'].append(['q',2]),
            lambda p:p['control']['measurement']['executions'][0][0].update(success=False),
            lambda p:p['control']['measurement']['witnesses'][0].pop(),
            lambda p:p.update(phi_control=[0]),
            lambda p:p.update(stratum='HISTORICAL_P0'),
        ]
        # h=1 emits 001, corrupt a definitely nonzero observation.
        mutations[0]=lambda p:p['control']['measurement']['executions'][8][0]['observations'].__setitem__(2,0)
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                p=copy.deepcopy(self.pair); mutate(p)
                with self.assertRaises(engine.InvalidAssay): check_pair(p)

    def test_transplants_are_actual_executions(self):
        self.assertIn('transplants',self.pair)
        self.assertEqual(set(self.pair['transplants']),{'control_to_treatment','treatment_to_control'})
        p=copy.deepcopy(self.pair)
        p['transplants']['control_to_treatment']['measurement']['executions'][0][0]['cost']=99
        with self.assertRaises(engine.InvalidAssay): check_pair(p)

    def test_nested_authorities_immutable_and_protocol_pinned(self):
        self.assertIn('protocol',authorities.EXPECTED)
        with self.assertRaises(TypeError): self.a.contract['references']['historical']['reconstructed_primary_sha256']='bad'
        with self.assertRaises(TypeError): self.a.identities['model']='bad'

    def test_preparation_failure_has_invalid_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'run'
            with patch('a2_v1.authorities.load_authorities',side_effect=engine.InvalidAssay('broken authority')):
                with self.assertRaises(engine.InvalidAssay): runner.validate(out)
            self.assertEqual(json.loads((out/'receipt.json').read_text())['status'],'INVALID_NO_SCIENTIFIC_RESULT')
            self.assertTrue((out/'diagnostics.json').exists())

    def test_seals_precede_first_pair_and_failure_retains_record(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'run'
            def fail(u,a):
                self.assertTrue((out/'preparation.json').exists())
                self.assertTrue((out/'expected_references.json').exists())
                self.assertTrue((out/'unit_manifest.json').exists())
                p=copy.deepcopy(self.pair); p['unit']=list(u); return p
            with patch('a2_v1.runner.execute_paired_cell',side_effect=fail):
                with self.assertRaises(engine.InvalidAssay): runner.validate(out)
            diagnostics=json.loads((out/'diagnostics.json').read_text())
            self.assertEqual(len(diagnostics['records']),1)
            receipt=json.loads((out/'receipt.json').read_text())
            self.assertEqual(receipt['entered']['THEOREM_CONTROL'],1)
            self.assertEqual(receipt['counters']['THEOREM_CONTROL'],1)

    def test_partial_execution_retained(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'run'
            exc=engine.InvalidAssay('partial'); exc.partial_record={'unit':[0,0,0],'control':{'trace':[{'episode':0}]}}
            with patch('a2_v1.runner.execute_paired_cell',side_effect=exc):
                with self.assertRaises(engine.InvalidAssay): runner.validate(out)
            d=json.loads((out/'diagnostics.json').read_text()); r=json.loads((out/'receipt.json').read_text())
            self.assertEqual(d['partial_record'],exc.partial_record)
            self.assertEqual(r['entered']['THEOREM_CONTROL'],1)
            self.assertEqual(r['counters']['THEOREM_CONTROL'],0)

class ControllerRegressions(unittest.TestCase):
    def test_coverage_exact_and_full_map_baseline(self):
        records=[{'unit':[8,0,0],'stratum':'HISTORICAL_P0','phi_control':[0]}, {'unit':[8,1,0],'stratum':'PROSPECTIVE_TARGET','phi_control':[0]}]
        self.assertTrue(hasattr(runner,'_coverage'))
        runner._coverage(records,{(8,0,0),(8,1,0)})
        for change in ('unit','stratum','baseline'):
            bad=copy.deepcopy(records)
            if change=='unit': bad[1]['unit']=[48,1,0]
            if change=='stratum': bad[1]['stratum']='HISTORICAL_P0'
            if change=='baseline': bad[1]['phi_control']=[1]
            with self.assertRaises(engine.InvalidAssay): runner._coverage(bad,{(8,0,0),(8,1,0)})

    def test_primary_is_lexicographic(self):
        self.assertTrue(hasattr(runner,'_primary'))
        fields={'stratum':'synthetic','phi_control':[],'phi_treatment':[],'delta_plus':[],'delta_minus':[]}
        rows=[dict(fields,unit=list(u)) for u in [(47,0,7),(8,3,0),(8,1,0),(0,0,0)]]
        self.assertEqual([r['unit'] for r in runner._primary(rows)['rows']],[[0,0,0],[8,1,0],[8,3,0],[47,0,7]])

    def test_seal_reverification_rejects_changes(self):
        self.assertTrue(hasattr(runner,'_verify_seals'))
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'x.json'; seal=runner._seal(p,{'ok':True}); p.write_text('{}')
            with self.assertRaises(engine.InvalidAssay): runner._verify_seals(Path(td),{'x.json':seal})

    def test_source_change_blocks_validation_pass_and_target_entry(self):
        calls=[]
        def fake(u,a):
            calls.append(u)
            return {'unit':list(u),'stratum':engine.stratum(u),'phi_control':[]}
        for science in (False,True):
            calls.clear()
            with tempfile.TemporaryDirectory() as td:
                out=Path(td)/'run'
                with patch.object(runner,'execute_paired_cell',side_effect=fake), patch.object(runner,'check_pair',return_value=[]), patch.object(runner,'_match_reference',return_value=True), patch.object(runner,'source_digest',side_effect=[runner.source_digest(),runner.source_digest(),'changed']):
                    with self.assertRaisesRegex(engine.InvalidAssay,'SOURCE_CHANGED'): (runner.run_prospective if science else runner.validate)(out)
                self.assertEqual(len(calls),2176)
                self.assertFalse(any(engine.stratum(u)=='PROSPECTIVE_TARGET' for u in calls))
                self.assertEqual(json.loads((out/'receipt.json').read_text())['status'],'INVALID_NO_SCIENTIFIC_RESULT')

    def test_fresh_science_gate_order_and_stops_at_synthetic_target_boundary(self):
        calls=[]
        def fake(u,a):
            calls.append(u)
            if engine.stratum(u)=='PROSPECTIVE_TARGET': raise engine.InvalidAssay('synthetic target sentinel')
            return {'unit':list(u),'stratum':engine.stratum(u),'phi_control':[]}
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'run'
            with patch.object(runner,'execute_paired_cell',side_effect=fake), patch.object(runner,'check_pair',return_value=[]), patch.object(runner,'_match_reference',return_value=True):
                with self.assertRaisesRegex(engine.InvalidAssay,'synthetic target sentinel'): runner.run_prospective(out)
            self.assertEqual([engine.stratum(calls[i]) for i in (0,1536,1856,2176)],['THEOREM_CONTROL','HISTORICAL_P0','COVARIANCE_P3','PROSPECTIVE_TARGET'])
            self.assertEqual(json.loads((out/'validation'/'receipt.json').read_text())['status'],'PASS')
            self.assertEqual(json.loads((out/'receipt.json').read_text())['counters']['PROSPECTIVE_TARGET'],0)

    def test_production_reference_matching_each_phase_with_real_checked_failure_cell(self):
        a=authorities.load_authorities(); original=runner._references(a)
        for index,phase in enumerate(runner.PHASES[:3]):
            expected=copy.deepcopy(original)
            first=next(runner._phase_units(phase))
            # Deliberately falsify a compiled expectation, leaving execution unchanged.
            expected[index][first]['phi_treatment']=[999]
            reference_pair=engine.execute_paired_cell(first,a)
            self.assertTrue(check_pair(reference_pair,a))
            def fake(u,auth):
                if u==first: return copy.deepcopy(reference_pair)
                r=original[runner.PHASES.index(engine.stratum(u))][u]
                n=r.get('predicted_training_failures',0)
                return {**copy.deepcopy(r),'unit':list(u),'stratum':engine.stratum(u),'control':{'constructor':{'active':r.get('active_control',0)}},'treatment':{'constructor':{'active':r.get('active_treatment',0)},'trace':[{'actual_correctness':False}]*n}}
            def check(p,auth): return check_pair(p,auth) if tuple(p['unit'])==first else []
            with tempfile.TemporaryDirectory() as td:
                out=Path(td)/'run'
                with patch.object(runner,'_references',return_value=expected),patch.object(runner,'execute_paired_cell',side_effect=fake),patch.object(runner,'check_pair',side_effect=check):
                    with self.assertRaisesRegex(engine.InvalidAssay,['THEOREM_CONTROL_MISMATCH','P0_REPLAY_MISMATCH','P3_COVARIANCE_MISMATCH'][index]): runner.validate(out)
                d=json.loads((out/'diagnostics.json').read_text()); receipt=json.loads((out/'receipt.json').read_text())
                self.assertEqual(d['records'][-1]['unit'],list(first))
                self.assertEqual(d['checks'][-1]['reference_match'],'FAIL')
                self.assertEqual(receipt['entered']['PROSPECTIVE_TARGET'],0)

    def test_seal_change_after_gate_prevents_target_entry(self):
        calls=[]
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'run'; original_seal=runner._seal
            def seal(path,value):
                result=original_seal(path,value)
                if Path(path)==out/'validation'/'receipt.json': (out/'unit_manifest.json').write_text('{}')
                return result
            def fake(u,a):
                calls.append(u); return {'unit':list(u),'stratum':engine.stratum(u),'phi_control':[]}
            with patch.object(runner,'_seal',side_effect=seal),patch.object(runner,'execute_paired_cell',side_effect=fake),patch.object(runner,'_match_reference',return_value=True),patch.object(runner,'check_pair',return_value=[]):
                with self.assertRaisesRegex(engine.InvalidAssay,'ARTIFACT_SEAL_MISMATCH'): runner.run_prospective(out)
            self.assertEqual(len(calls),2176)
            self.assertTrue((out/'invalid_receipt.json').exists())

    def test_actual_engine_partial_record_on_evaluation_fault(self):
        from a2_v1.frozen_model import model
        execute=model.execute; calls=[]
        def fail(policy,h,x):
            calls.append(x)
            if len(calls)==4: raise RuntimeError('evaluation fault')
            return execute(policy,h,x)
        with patch.object(model,'execute',side_effect=fail):
            with self.assertRaises(engine.InvalidAssay) as cm: engine.execute_paired_cell((0,0,0),authorities.load_authorities())
        p=cm.exception.partial_record
        self.assertEqual(len(p['control']['trace']),8)
        self.assertEqual(len(p['control']['measurement']['executions'][0]),3)
        self.assertEqual(p['control']['measurement']['current_execution'],{'policy':0,'state':3})

    def test_derived_effect_witness_and_both_encounter_loss_structures(self):
        from a2_v1.derived import derive
        rows=[]
        for p in range(2):
            for k in range(2):
                rows.append({'unit':[8,p,k],'phi_treatment':[0,1+p+k], 'delta_plus':[20] if p else [],'delta_minus':([10+p] if k==0 else [10+p,30])})
        d=derive(rows,hypotheses=(8,),priorities=(0,1),rotations=(0,1))
        self.assertEqual(d['E_PK'],{'members':[8],'witnesses':{'8':[0,1,0,1]}})
        self.assertEqual(d['L_any_K']['members'],[[8,0],[8,1]])
        self.assertEqual(d['L_common_K']['members'],[[8,0],[8,1]])
        self.assertEqual(d['C_K'],{'8,0':[10],'8,1':[11]})
        rows[1]['delta_minus']=[12]
        d=derive(rows,hypotheses=(8,),priorities=(0,1),rotations=(0,1))
        self.assertEqual(d['L_any_K']['members'],[[8,0],[8,1]])
        self.assertEqual(d['L_common_K']['members'],[[8,1]])
        self.assertEqual(d['C_K']['8,0'],[])

    def test_partial_training_and_constructor_context_survives_fault(self):
        calls=[]; update=engine.Learner.update
        def fail(learner,*args):
            calls.append(1)
            if len(calls)==4: raise RuntimeError('training fault')
            return update(learner,*args)
        with patch.object(engine.Learner,'update',new=fail):
            with self.assertRaises(engine.InvalidAssay) as cm: engine.execute_paired_cell((0,0,0),authorities.load_authorities())
        arm=cm.exception.partial_record['control']
        self.assertEqual(len(arm['trace']),3)
        self.assertEqual(arm['current_episode']['episode'],3)
        self.assertEqual(arm['training_charge'],15)
        with patch.object(engine,'_measure',side_effect=RuntimeError('measurement fault')):
            with self.assertRaises(engine.InvalidAssay) as cm: engine.execute_paired_cell((0,0,0),authorities.load_authorities())
        self.assertEqual(cm.exception.partial_record['control']['constructor'],{'task':'SWITCHBOARD_3','active':0})
