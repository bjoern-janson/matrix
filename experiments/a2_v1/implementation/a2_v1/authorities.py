"""Pinned authority loading and engine-independent reference compilation."""
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping

ROOT = Path(__file__).resolve().parents[4]
PATHS = {
 'contract': ROOT/'experiments/a2_v1/PREREG_CONTRACT.json',
 'priority': ROOT/'experiments/a2_v1/audit/PRIORITY_FAMILY_AUDIT.json',
 'theorem': ROOT/'experiments/a2_v1/audit/THEOREM_CONTROL_PREDICTIONS.json',
 'historical': ROOT/'experiments/a2_v0/results/primary_compact.json',
 'model': ROOT/'experiments/a2_v0/implementation/a2_v0/model.py',
 'protocol': ROOT/'experiments/A2_PREREG_V1.md'}
EXPECTED={'contract':'8ae73dd492f9c762546554ed5dc20f18c9a1220c955f3efa7f384cccf07a6b22','priority':'a11c989c0a72d4d0363077ce353fd5642f708933adedee475ca2c1678497bb2c','theorem':'aa274d3038c9a6633a35a3ef66395773bb27413e8768f0956b878667941deaf5','historical':'0c59eb2324c244af83ebb8be86fdb496897a81566a9d3896e61fc2f26d84aeca','model':'6ab7a3a27d7be6aed5f7743f6b302e1264c958eef8f1c45b367562613f850eef'}

EXPECTED['protocol']='25cbe801494101c18a75bb64300b7bd54b7c47a5ed74dc6a0d206a757ea7c243'

def freeze(value):
    if isinstance(value, Mapping): return MappingProxyType({k:freeze(v) for k,v in value.items()})
    if isinstance(value,(list,tuple)): return tuple(freeze(v) for v in value)
    return value

def thaw(value):
    if isinstance(value, Mapping): return {k:thaw(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [thaw(v) for v in value]
    return value

def canonical(value): value=thaw(value); return (json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
def digest(path): return sha256(Path(path).read_bytes()).hexdigest()

@dataclass(frozen=True)
class Authorities:
    contract: dict; priorities: tuple; theorem: dict; historical: dict; identities: dict

def load_authorities():
    from .runner import InvalidAssay
    identities={k:digest(PATHS[k]) for k in EXPECTED}
    if identities != EXPECTED: raise InvalidAssay('SOURCE_OR_REFERENCE_IDENTITY_MISMATCH')
    contract=json.loads(PATHS['contract'].read_text()); audit=json.loads(PATHS['priority'].read_text())
    priorities=tuple(tuple(x['order']) for x in audit['distinct_priorities'])
    reps=tuple(x['representative_index'] for x in audit['distinct_priorities'])
    if len(priorities)!=24 or reps != tuple(contract['priority_family']['representative_indices']) or any(p[0]!=0 or len(set(p))!=48 for p in priorities):
        raise InvalidAssay('PRIORITY_FAMILY_MISMATCH')
    maps=_hypothesis_maps()
    audited=tuple(tuple(x['state_map']) for x in audit['hypotheses'])
    if tuple(maps)!=audited or contract['total_paired_cells']!=9216 or sum(x['paired_cells'] for x in contract['strata'])!=9216:
        raise InvalidAssay('FROZEN_UNIVERSE_MISMATCH')
    units={(h,p,k) for h in range(48) for p in range(24) for k in range(8)}
    strata=[]
    for s in contract['strata']:
        cells={(h,p,k) for h in s['hypothesis_indices'] for p in s['priority_ids'] for k in s['rotations']}
        if len(cells)!=s['paired_cells']: raise InvalidAssay('STRATUM_COUNT_MISMATCH')
        strata.append(cells)
    if set().union(*strata)!=units or sum(map(len,strata))!=len(units): raise InvalidAssay('STRATUM_PARTITION_MISMATCH')
    return Authorities(freeze(contract),priorities,freeze(json.loads(PATHS['theorem'].read_text())),freeze(json.loads(PATHS['historical'].read_text())),freeze(identities))

def _phi(mask):
    floor={0,1,2,4,8,16,32,64,128}
    return sorted(floor|{s for s in range(256) if not s & ~mask})

def reconstruct_historical(a):
    units=[]
    for r in a.historical['rows']:
        h,k,code,ac,at,cm,tm,*_=r; pc,pt=_phi(cm),_phi(tm)
        units.append({'unit':[h,k],'phi_control':pc,'phi_treatment':pt,'delta_plus':sorted(set(pt)-set(pc)),'delta_minus':sorted(set(pc)-set(pt)),'classification':a.historical['class_codes'][code]})
    obj={'endpoint':'full_frontier_sets','set_encoding':'8-bit subset mask; bit x denotes state x','units':units}
    indexed={tuple(x['unit']):dict(x) for x in units}
    for r in a.historical['rows']:
        indexed[(r[0],r[1])].update(active_control=r[3],active_treatment=r[4])
    return indexed,sha256(canonical(obj)).hexdigest()

def _hypothesis_maps():
    from itertools import permutations,product
    maps=[]
    for sig in permutations(range(3)):
      for mask in product((0,1),repeat=3):
        maps.append(tuple(sum((((x>>(2-sig[j]))&1)^mask[j])<<(2-j) for j in range(3)) for x in range(8)))
    return maps

def compile_p3(a,historical):
    """Transport P0 endpoints using explicit state bijections, never V1 execution."""
    maps=_hypothesis_maps(); lookup={m:i for i,m in enumerate(maps)}; q=lambda x:x^4
    out={}
    def conjugate(i): return lookup[tuple(q(maps[i][q(x)]) for x in range(8))]
    for (h,k),r in historical.items():
        hp=conjugate(h); unit=(hp,3,(k+4)%8)
        tr=lambda fam: sorted(sum(1<<q(x) for x in range(8) if s&(1<<x)) for s in fam)
        out[unit]={'unit':list(unit),'stratum':'COVARIANCE_P3','phi_control':tr(r['phi_control']),'phi_treatment':tr(r['phi_treatment']),'delta_plus':tr(r['delta_plus']),'delta_minus':tr(r['delta_minus']),'active_control':conjugate(r['active_control']),'active_treatment':conjugate(r['active_treatment'])}
    if len(out)!=320: raise ValueError('P3 reference census mismatch')
    return out

def compile_theorem(a):
    codes=a.theorem['set_codes']; cols=a.theorem['columns']; out={}
    for values in a.theorem['rows']:
      r=dict(zip(cols,values)); unit=(r['hypothesis_index'],r['priority_id'],r['rotation'])
      def fam(v):
        if isinstance(v,(list,tuple)): return list(v)
        if v=='FULL': return list(range(256))
        if v=='EMPTY': return []
        if v=='SINGLETON_FLOOR': return [0,1,2,4,8,16,32,64,128]
        if v=='NON_SINGLETON_SETS': return [x for x in range(256) if x not in (0,1,2,4,8,16,32,64,128)]
        return thaw(codes[v])
      out[unit]={**r,'unit':list(unit),**{n:fam(r[n]) for n in ('phi_control','phi_treatment','delta_plus','delta_minus')}}
    return out
