"""Independent mathematical verification of continuous traces and policy evidence."""
from itertools import permutations, product
from .engine import InvalidAssay

# Enumerate the mathematical authority independently of engine decoders.
MAPS=tuple(tuple(sum((((x>>(2-s[j]))&1)^b[j])<<(2-j) for j in range(3)) for x in range(8))
           for s in permutations(range(3)) for b in product((0,1),repeat=3))

def _need(value,name,checks):
    if not value:
        exc=InvalidAssay('INVARIANT_MISMATCH:'+name)
        exc.partial_checks=checks+[{'name':name,'status':'FAIL'}]
        raise exc
    checks.append({'name':name,'status':'PASS'})

def _observations(h,x): return [int(v) for v in format(MAPS[h][x],'03b')]
def _decode(h,obs): return MAPS[h].index(int(''.join(map(str,obs)),2))
def _oracle_frontier(h,a):
    good={x for x in range(8) if MAPS[h][x]==MAPS[a][x]}
    return sorted({0,1,2,4,8,16,32,64,128}|{s for s in range(256) if all(not(s>>x&1) or x in good for x in range(8))})
def _unit_stratum(u):
    h,p,k=u
    return 'THEOREM_CONTROL' if h<8 else 'HISTORICAL_P0' if p==0 else 'COVARIANCE_P3' if p==3 else 'PROSPECTIVE_TARGET'

def _measurement(h,constructor,m,label,checks):
    active=constructor['active']
    _need(m['subsets_checked']==256 and len(m['witnesses'])==256 and len(m['executions'])==9 and all(len(r)==8 for r in m['executions']),'full_evaluation_'+label,checks)
    policies=[{'kind':'immediate','target':pi,'hypothesis':None,'provenance':['SWITCHBOARD_3',active,'immediate',pi],'realization_cost':1} for pi in range(8)]
    policies.append({'kind':'diagnostic','target':None,'hypothesis':active,'provenance':['SWITCHBOARD_3',active,'diagnostic',active],'realization_cost':1})
    _need(m['policies']==policies,'realized_policy_boundary_'+label,checks)
    for pi,row in enumerate(m['executions']):
      for x,r in enumerate(row):
        obs=[] if pi<8 else _observations(h,x)
        repair=pi if pi<8 else _decode(active,obs)
        actions=[['r',repair]] if pi<8 else [['q',0],['q',1],['q',2],['r',repair]]
        _need(r=={'success':repair==x,'cost':1+len(actions),'actions':actions,'observations':obs},'policy_execution_'+label+'_'+str(pi)+'_'+str(x),checks)
    expected_witnesses=[[pi for pi in range(9) if all(not(s>>x&1) or ((pi==x) if pi<8 else MAPS[h][x]==MAPS[active][x]) for x in range(8))] for s in range(256)]
    _need(m['witnesses']==expected_witnesses,'exact_common_witnesses_'+label,checks)
    oracle=_oracle_frontier(h,active)
    _need(m['frontier']==oracle and m['success_states']==[x for x in range(8) if MAPS[h][x]==MAPS[active][x]],'independent_frontier_'+label,checks)
    q=set(m['frontier'])
    _need(all((s^(1<<x)) in q for s in q for x in range(8) if s>>x&1),'downward_closed_'+label,checks)

def check_pair(pair,authorities=None):
    from .authorities import load_authorities
    a=authorities if authorities is not None else load_authorities()
    checks=[]
    try:
      h,p,k=pair['unit']
      _need(all(type(x) is int for x in (h,p,k)) and 0<=h<48 and 0<=p<24 and 0<=k<8,'unit_universe',checks)
      _need(pair['stratum']==_unit_stratum((h,p,k)),'unit_stratum',checks)
      _need(pair['clone_equal'] and pair['mutable_disjoint'],'pair_isolation',checks)
      rank={x:i for i,x in enumerate(a.priorities[p])}
      for label in ('control','treatment'):
        arm=pair[label]; informative=label=='treatment'
        _need(arm['priority_order']==list(a.priorities[p]),'frozen_priority_'+label,checks)
        _need(len(arm['trace'])==8 and arm['training_charge']==40 and arm['hypothesis_checks']==384,'fixed_work_'+label,checks)
        live=list(range(48)); active=0
        for i,t in enumerate(arm['trace']):
          obs=_observations(h,(k+i)%8)
          _need(t['episode']==i and t['x']==(k+i)%8 and t['query_slots']==[0,1,2] and t['observations']==obs,'schedule_'+label,checks)
          _need(t['live_before']==live and t['active_before']==active,'continuous_state_'+label,checks)
          prediction=_decode(active,obs); correct=prediction==t['x']
          _need(t['prediction']==prediction and type(t['actual_correctness']) is bool and t['actual_correctness']==correct,'prediction_correctness_'+label,checks)
          _need(t['feedback']==([True,correct] if informative else [False,False]),'feedback_'+label,checks)
          _need((t['primitive_charge'],t['processing_charge'],t['hypothesis_checks'])==(4,1,48),'step_work_'+label,checks)
          new=[candidate for candidate in live if (_decode(candidate,obs)==prediction)==correct] if informative else live[:]
          _need(t['live_after']==new and h in new,'equality_truth_'+label,checks)
          selected=min(new,key=rank.__getitem__)
          _need(t['active_after']==selected and rank[selected]>=rank[active],'active_rank_'+label,checks)
          _need((selected==active) if (not informative or correct) else (active not in new),'feedback_selection_'+label,checks)
          live,active=new,selected
        _need(arm['final_live']==live and arm['constructor']=={'task':'SWITCHBOARD_3','active':active},'final_constructor_link_'+label,checks)
        _need(arm['evaluation_unchanged'] and arm['frozen_snapshot_before']==[live,True] and arm['frozen_snapshot_after']==[live,True],'frozen_state_'+label,checks)
        _measurement(h,arm['constructor'],arm['measurement'],label,checks)
        _need(pair['phi_'+label]==arm['measurement']['frontier'],'primary_measurement_link_'+label,checks)
      _need(pair['delta_plus']==sorted(set(pair['phi_treatment'])-set(pair['phi_control'])) and pair['delta_minus']==sorted(set(pair['phi_control'])-set(pair['phi_treatment'])),'directed_differences',checks)
      changed=pair['phi_control']!=pair['phi_treatment']
      _need(set(pair['transplants'])==({'control_to_treatment','treatment_to_control'} if changed else set()),'transplant_coverage',checks)
      if changed:
        for donor,recipient in (('control','treatment'),('treatment','control')):
          key=donor+'_to_'+recipient; transplant=pair['transplants'][key]
          _need(transplant['donor']==donor and transplant['recipient']==recipient and transplant['recipient_before']==pair[recipient]['constructor'] and transplant['constructor']==pair[donor]['constructor'],'transplant_constructor_'+key,checks)
          _measurement(h,transplant['constructor'],transplant['measurement'],key,checks)
          _need(transplant['measurement']['frontier']==pair['phi_'+donor],'transplant_donor_frontier_'+key,checks)
      return checks
    except (KeyError,ValueError,TypeError,IndexError) as exc:
      invalid=InvalidAssay('INVARIANT_MISMATCH:MALFORMED_EVIDENCE:'+str(exc)); invalid.partial_checks=checks
      raise invalid from exc
