"""Immutable ordered validation gate and future fresh-gate science path."""
from hashlib import sha256
import json,platform
from pathlib import Path
from .engine import InvalidAssay as EngineInvalid, execute_paired_cell, stratum

InvalidAssay = EngineInvalid
InvalidAssay.status = 'INVALID_NO_SCIENTIFIC_RESULT'
from .authorities import canonical as _canon, thaw, freeze
def _seal(path,x):
    b=_canon(x)
    with Path(path).open('xb') as f:f.write(b)
    return sha256(b).hexdigest()
def source_manifest():
    from .authorities import PATHS
    impl=Path(__file__).resolve().parents[1]; repo=Path(__file__).resolve().parents[4]; paths=sorted((impl/'a2_v1').glob('*.py'))+sorted((impl/'tests').glob('test_*.py'))+list(PATHS.values())
    manifest={str(p.relative_to(repo)):sha256(p.read_bytes()).hexdigest() for p in paths}
    return manifest

def source_digest(): return sha256(_canon(source_manifest())).hexdigest()
def _references(a):
    from .authorities import compile_p3,compile_theorem,reconstruct_historical
    theorem=compile_theorem(a); hist,seal=reconstruct_historical(a)
    if seal!=a.contract['references']['historical']['reconstructed_primary_sha256']: raise InvalidAssay('HISTORICAL_RECONSTRUCTION_MISMATCH')
    p0={(h,0,k):{**r,'unit':[h,0,k],'stratum':'HISTORICAL_P0'} for (h,k),r in hist.items()}; return theorem,p0,compile_p3(a,hist)
def _match_reference(pair,expected):
    for f in ('phi_control','phi_treatment','delta_plus','delta_minus'):
      if pair.get(f)!=expected.get(f): return False
    if 'active_control' in expected:
      if pair['control']['constructor']['active']!=expected['active_control'] or pair['treatment']['constructor']['active']!=expected['active_treatment']: return False
    if 'predicted_training_failures' in expected:
      if sum(not t['actual_correctness'] for t in pair['treatment']['trace']) != expected['predicted_training_failures']: return False
    return True
def _phase_units(name):
    if name=='THEOREM_CONTROL': return ((h,p,k) for h in range(8) for p in range(24) for k in range(8))
    if name=='HISTORICAL_P0': return ((h,0,k) for h in range(8,48) for k in range(8))
    if name=='COVARIANCE_P3': return ((h,3,k) for h in range(8,48) for k in range(8))
    return ((h,p,k) for h in range(8,48) for p in range(24) if p not in (0,3) for k in range(8))
PHASES=('THEOREM_CONTROL','HISTORICAL_P0','COVARIANCE_P3','PROSPECTIVE_TARGET')
COUNTS=dict(zip(PHASES,(1536,320,320,7040)))

def _verify_seals(out,seals):
    for name,expected in seals.items():
        path=out/name
        if not path.is_file() or sha256(path.read_bytes()).hexdigest()!=expected:
            raise InvalidAssay('ARTIFACT_SEAL_MISMATCH:'+name)

def _coverage(records,expected):
    units=[tuple(p['unit']) for p in records]
    if len(units)!=len(set(units)) or set(units)!=set(expected):
        raise InvalidAssay('INVARIANT_MISMATCH:EXACT_UNIT_COVERAGE')
    baselines={}
    for record,u in zip(records,units):
        if not all(type(x) is int for x in u) or len(u)!=3 or not (0<=u[0]<48 and 0<=u[1]<24 and 0<=u[2]<8) or record['stratum']!=stratum(u):
            raise InvalidAssay('INVARIANT_MISMATCH:UNIT_STRATUM')
        frontier=tuple(record['phi_control'])
        if u[0] in baselines and baselines[u[0]]!=frontier:
            raise InvalidAssay('INVARIANT_MISMATCH:CONTROL_BASELINE')
        baselines[u[0]]=frontier

def _primary(records):
    return {'schema':'a2-v1-primary/1','rows':[{k:p[k] for k in ('unit','stratum','phi_control','phi_treatment','delta_plus','delta_minus')} for p in sorted(records,key=lambda p:tuple(p['unit']))]}

def _run_gate(out,science=False):
    from .authorities import load_authorities
    counters={x:0 for x in PHASES}; entered=dict(counters)
    stages=[]; records=[]; checks=[]; seals={}; digest=None; current=None; partial=None
    validation_out=out/'validation' if science else out
    def seal(name,value):
        seals[name]=_seal(out/name,value)
        return seals[name]
    def reverify():
        if source_digest()!=digest: raise InvalidAssay('SOURCE_CHANGED_DURING_RUN')
        if source_manifest()!=manifest: raise InvalidAssay('SOURCE_MANIFEST_CHANGED_DURING_RUN')
        if load_authorities()!=a: raise InvalidAssay('AUTHORITIES_CHANGED_DURING_RUN')
        _verify_seals(out,seals)
    try:
      if science: validation_out.mkdir()
      a=load_authorities(); refs=freeze(_references(a)); manifest=source_manifest(); digest=source_digest()
      if sha256(_canon(manifest)).hexdigest()!=digest:
          raise InvalidAssay('SOURCE_CHANGED_DURING_PREPARATION')
      units={phase:tuple(_phase_units(phase)) for phase in PHASES}
      for phase in PHASES:
          declared={(h,p,k) for s in a.contract['strata'] if s['code']==phase for h in s['hypothesis_indices'] for p in s['priority_ids'] for k in s['rotations']}
          if set(units[phase])!=declared or len(units[phase])!=COUNTS[phase]: raise InvalidAssay('UNIT_MANIFEST_MISMATCH')
      for phase,expected in zip(PHASES,refs):
          if set(expected)!=set(units[phase]): raise InvalidAssay('EXPECTED_REFERENCE_COVERAGE_MISMATCH:'+phase)
      seal('source_manifest.json',manifest)
      seal('unit_manifest.json',{phase:[list(u) for u in rows] for phase,rows in units.items()})
      seal('expected_references.json',{phase:[thaw(expected[u]) for u in units[phase]] for phase,expected in zip(PHASES,refs)})
      seal('preparation.json',{'schema':'a2-v1-preparation/1','source_digest':digest,'identities':a.identities,'artifacts':dict(seals),'counts':COUNTS})
      reverify()
      stages.append('PREPARATION_SEALED')
      def execute(phase,u,expected=None):
          nonlocal current,partial
          current={'phase':phase,'requested_unit':list(u),'status':'ENTERED'}
          entered[phase]+=1
          pair=execute_paired_cell(u,a)
          counters[phase]+=1; records.append(pair); current['status']='COMPLETED'
          if pair.get('unit')!=list(u) or pair.get('stratum')!=phase: raise InvalidAssay('REQUESTED_RETURNED_UNIT_MISMATCH')
          check_record={'unit':list(u),'checks':[]}; checks.append(check_record)
          try: check_record['checks']=check_pair(pair,a)
          except Exception as exc:
              check_record['checks']=getattr(exc,'partial_checks',[])
              check_record['error']=str(exc)
              raise
          if expected is not None and not _match_reference(pair,thaw(expected)):
              check_record['reference_match']='FAIL'
              raise InvalidAssay({'THEOREM_CONTROL':'THEOREM_CONTROL_MISMATCH','HISTORICAL_P0':'P0_REPLAY_MISMATCH','COVARIANCE_P3':'P3_COVARIANCE_MISMATCH'}[phase])
          check_record['reference_match']='PASS' if expected is not None else 'NOT_APPLICABLE'
          current=None
      for phase,expected in zip(PHASES,refs):
          for u in units[phase]: execute(phase,u,expected[u])
          stages.append(phase+'_MATCHED')
      reference_units=set().union(*(set(units[p]) for p in PHASES[:3]))
      _coverage(records,reference_units)
      if counters!={**{p:COUNTS[p] for p in PHASES[:3]},'PROSPECTIVE_TARGET':0} or entered!=counters: raise InvalidAssay('REFERENCE_COUNTER_MISMATCH')
      stages.append('REMAINING_INVARIANTS_PASSED')
      reverify()
      prefix='validation/' if science else ''
      evhash=seal(prefix+'evidence.json',{'schema':'a2-v1-validation-evidence/2','records':records,'checks':checks,'identities':a.identities})
      receipt={'schema':'a2-v1-validation/2','mode':'fresh-science-gate' if science else 'validate','status':'PASS','source_digest':digest,'counters':dict(counters),'entered':dict(entered),'stages':list(stages),'artifacts':dict(seals),'evidence_sha256':evhash,'python':platform.python_version(),'scientific_interpretation':'NOT_RUN'}
      seal(prefix+'receipt.json',receipt)
      # Validation also rechecks the newly written evidence and receipt; science must
      # cross this same fresh check immediately before the first target boundary.
      reverify()
      if not science: return receipt
      for u in units['PROSPECTIVE_TARGET']: execute('PROSPECTIVE_TARGET',u)
      _coverage(records,set().union(*(set(rows) for rows in units.values())))
      if counters!=COUNTS or entered!=COUNTS: raise InvalidAssay('COMPLETE_COUNTER_MISMATCH')
      reverify()
      evhash=seal('evidence.json',{'schema':'a2-v1-evidence/2','records':records,'checks':checks,'identities':a.identities})
      primary=_primary(records); primary_hash=seal('primary.json',primary)
      from .derived import derive
      derived_hash=seal('derived.json',{'schema':'a2-v1-derived/1','primary_sha256':primary_hash,'structures':derive(primary['rows'])})
      reverify()
      receipt={'schema':'a2-v1-receipt/2','mode':'prospective','status':'COMPLETE','source_digest':digest,'reference_seals':a.identities,'counters':dict(counters),'entered':dict(entered),'stages':stages+['PROSPECTIVE_TARGET_COMPLETE','FINAL_INVARIANTS_AND_SEALS'],'artifacts':dict(seals),'fresh_validation_sha256':seals['validation/receipt.json'],'evidence_sha256':evhash,'primary_sha256':primary_hash,'derived_sha256':derived_hash,'python':platform.python_version(),'scientific_interpretation':'ADMITTED'}
      seal('receipt.json',receipt); reverify(); return receipt
    except Exception as exc:
      partial=getattr(exc,'partial_record',None)
      diagnostic={'schema':'a2-v1-diagnostics/2','records':records,'checks':checks,'current_execution':current,'partial_record':partial,'reason':str(exc),'preexisting_artifact_seals':dict(seals)}
      diagnostic_hash=_seal(out/'diagnostics.json',diagnostic)
      receipt={'schema':'a2-v1-receipt/2','mode':'prospective' if science else 'validate','status':'INVALID_NO_SCIENTIFIC_RESULT','reason':str(exc),'source_digest':digest,'counters':counters,'entered':entered,'stages':stages,'diagnostics_sha256':diagnostic_hash,'artifacts':dict(seals),'scientific_interpretation':'NOT_ADMITTED'}
      # A late seal fault cannot overwrite any earlier receipt, even a PASS.
      _seal(out/'invalid_receipt.json',receipt)
      if not (out/'receipt.json').exists(): _seal(out/'receipt.json',receipt)
      raise InvalidAssay(str(exc)) from exc
def validate(output_dir):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=False); return _run_gate(out,False)
def run_prospective(output_dir):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=False); return _run_gate(out,True)

from .checks import check_pair
