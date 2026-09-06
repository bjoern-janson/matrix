"""Exact registered set-valued derived structures."""
from itertools import combinations

def derive(rows,hypotheses=range(8,48),priorities=range(24),rotations=range(8)):
    ix={tuple(r['unit']):r for r in rows}; result={}
    ek=[]; ekw={}; ep=[]; epw={}; epk=[]; epkw={}
    gamma=lambda h,p,k:(tuple(ix[h,p,k]['delta_plus']),tuple(ix[h,p,k]['delta_minus']))
    phi=lambda h,p,k:set(ix[h,p,k]['phi_treatment'])
    for h in hypotheses:
      for p in priorities:
        for k,k2 in combinations(rotations,2):
          if gamma(h,p,k)!=gamma(h,p,k2): ek.append([h,p]); ekw[f'{h},{p}']=[k,k2]; break
      for k in rotations:
        for p,p2 in combinations(priorities,2):
          if gamma(h,p,k)!=gamma(h,p2,k): ep.append([h,k]); epw[f'{h},{k}']=[p,p2]; break
      found=False
      for p,p2 in combinations(priorities,2):
       for k,k2 in combinations(rotations,2):
        d=lambda q:(sorted(phi(h,q,k)-phi(h,q,k2)),sorted(phi(h,q,k2)-phi(h,q,k)))
        if d(p)!=d(p2): epk.append(h); epkw[str(h)]=[p,p2,k,k2]; found=True; break
       if found: break
    result['E_K']={'members':ek,'witnesses':ekw}; result['E_P']={'members':ep,'witnesses':epw}; result['E_PK']={'members':epk,'witnesses':epkw}
    anyp=[]; commonp=[]; cp={}; anyk=[]; commonk=[]; ck={}
    for h in hypotheses:
      for k in rotations:
        fs=[set(ix[h,p,k]['delta_minus']) for p in priorities]; common=set.intersection(*fs); cp[f'{h},{k}']=sorted(common)
        if all(fs): anyp.append([h,k])
        if common: commonp.append([h,k])
      for p in priorities:
        fs=[set(ix[h,p,k]['delta_minus']) for k in rotations]; common=set.intersection(*fs); ck[f'{h},{p}']=sorted(common)
        if all(fs): anyk.append([h,p])
        if common: commonk.append([h,p])
    result.update({'L_any_P':{'members':anyp},'L_common_P':{'members':commonp},'C_P':cp,'L_any_K':{'members':anyk},'L_common_K':{'members':commonk},'C_K':ck})
    return result
