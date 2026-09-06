"""Frozen priority-aware learner and paired execution."""
from copy import deepcopy
from dataclasses import dataclass
from itertools import permutations,product

class InvalidAssay(RuntimeError): pass
def require(x,msg):
    if not x: raise InvalidAssay(msg)

HYPOTHESES=tuple((s,b) for s in permutations(range(3)) for b in product((0,1),repeat=3))
def channel(i,x):
    s,b=HYPOTHESES[i]; return tuple(((x>>(2-s[j]))&1)^b[j] for j in range(3))
def decode(i,o):
    s,b=HYPOTHESES[i]; return sum((o[j]^b[j])<<(2-s[j]) for j in range(3))

@dataclass(frozen=True)
class Feedback: valid:bool; correct:bool
@dataclass(frozen=True)
class Work: checks:int; charge:int

class Learner:
    def __init__(self,priority,live=None): self.priority=tuple(priority); self.rank={h:r for r,h in enumerate(priority)}; self.live=set(range(48) if live is None else live); self.frozen=False
    @property
    def active(self): return min(self.live,key=self.rank.__getitem__)
    def snapshot(self): return (tuple(sorted(self.live)),self.frozen)
    def predict(self,o): return decode(self.active,o)
    def update(self,o,repair,feedback):
        require(not self.frozen,'learning frozen')
        # The abstract processing batch scans every candidate in both arms.
        consistent={i for i in range(48) if (decode(i,o)==repair)==feedback.correct}
        proposed=self.live & consistent
        if feedback.valid: require(proposed,'empty live set'); self.live=proposed
        return Work(48,1)
    def freeze(self): self.frozen=True; return {'task':'SWITCHBOARD_3','active':self.active}

def stratum(unit):
    h,p,k=unit
    if h<8:return 'THEOREM_CONTROL'
    if p==0:return 'HISTORICAL_P0'
    if p==3:return 'COVARIANCE_P3'
    return 'PROSPECTIVE_TARGET'

def _measure(h,constructor,record=None):
    from .frozen_model import model
    require(set(constructor)=={'task','active'},'constructor boundary')
    policies=model.realize(model.ConstructorInput(**constructor))
    result={} if record is None else record
    executions=[]; result['executions']=executions
    result['policies']=[{'kind':p.kind,'target':p.target,'hypothesis':p.hypothesis,
                         'provenance':list(p.provenance),'realization_cost':p.realization_cost} for p in policies]
    for pi,policy in enumerate(policies):
      row=[]; executions.append(row)
      for x in range(8):
        result['current_execution']={'policy':pi,'state':x}
        r=model.execute(policy,model.HYPOTHESES[h],x)
        row.append({'success':r.success,'cost':r.cost,'actions':[list(a) for a in r.actions],'observations':list(r.observations)})
        result.pop('current_execution')
    witnesses=[[pi for pi,row in enumerate(executions) if all(row[x]['success'] and row[x]['cost']<=5 for x in range(8) if subset>>x&1)] for subset in range(256)]
    result.update(frontier=[s for s,w in enumerate(witnesses) if w],success_states=[x for x,r in enumerate(executions[8]) if r['success']],subsets_checked=256,witnesses=witnesses)
    return result

def _arm(learner,h,k,informative,record):
    trace=[]; record.update(trace=trace,training_charge=0,hypothesis_checks=0,priority_order=list(learner.priority)); charge=checks=0
    for episode in range(8):
      x=(k+episode)%8; obs=channel(h,x); before=sorted(learner.live); active_before=learner.active; pred=learner.predict(obs); fb=Feedback(True,pred==x) if informative else Feedback(False,False); record['current_episode']={'episode':episode,'x':x,'observations':list(obs),'prediction':pred,'live_before':before,'active_before':active_before,'feedback':[fb.valid,fb.correct]}; work=learner.update(obs,pred,fb); charge+=4+work.charge; checks+=work.checks
      trace.append({'episode':episode,'x':x,'query_slots':[0,1,2],'observations':list(obs),'prediction':pred,'actual_correctness':pred==x,'feedback':[fb.valid,fb.correct],'live_before':before,'live_after':sorted(learner.live),'active_before':active_before,'active_after':learner.active,'primitive_charge':4,'processing_charge':work.charge,'hypothesis_checks':work.checks})
      record.update(training_charge=charge,hypothesis_checks=checks); record.pop('current_episode')
    constructor=learner.freeze(); snap=learner.snapshot(); record.update(constructor=constructor,final_live=sorted(learner.live),frozen_snapshot_before=[list(snap[0]),snap[1]]); record['measurement']={}; measurement=_measure(h,constructor,record['measurement'])
    record.update({'constructor':constructor,'priority_order':list(learner.priority),'final_live':sorted(learner.live),'trace':trace,'measurement':measurement,'training_charge':charge,'hypothesis_checks':checks,'evaluation_unchanged':snap==learner.snapshot(),'frozen_snapshot_before':[list(snap[0]),snap[1]],'frozen_snapshot_after':[list(learner.snapshot()[0]),learner.snapshot()[1]]})
    return record

def execute_paired_cell(unit,authorities):
    """The sole paired training boundary; failures expose partial_record diagnostics."""
    record={'unit':list(unit),'control':{},'treatment':{},'transplants':{}}
    try:
      h,p,k=unit; require(0<=h<48 and 0<=p<24 and 0<=k<8,'unit outside universe')
      base=Learner(authorities.priorities[p]); c=deepcopy(base); t=deepcopy(base)
      record.update(stratum=stratum(unit),clone_equal=c.snapshot()==t.snapshot()==base.snapshot(),
                    mutable_disjoint=c.live is not t.live and c.live is not base.live and t.live is not base.live)
      cr=_arm(c,h,k,False,record['control']); tr=_arm(t,h,k,True,record['treatment'])
      pc,pt=cr['measurement']['frontier'],tr['measurement']['frontier']
      record.update(phi_control=pc,phi_treatment=pt,delta_plus=sorted(set(pt)-set(pc)),delta_minus=sorted(set(pc)-set(pt)))
      if pc!=pt:
        for donor,recipient in (('control','treatment'),('treatment','control')):
          # Replace only active constructor state on a fresh recipient constructor.
          constructor=dict(record[recipient]['constructor'])
          constructor['active']=record[donor]['constructor']['active']
          transplant={'donor':donor,'recipient':recipient,'recipient_before':dict(record[recipient]['constructor']),
                      'constructor':constructor,'measurement':{}}
          record['transplants'][donor+'_to_'+recipient]=transplant
          _measure(h,constructor,transplant['measurement'])
      return record
    except Exception as exc:
      failure=InvalidAssay(str(exc)); failure.partial_record=record
      raise failure from exc
