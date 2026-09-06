"""Post-execution analysis only. Reads sealed records; imports no assay engine."""
import argparse, hashlib, json, zipfile, gzip
from pathlib import Path
from itertools import permutations, product
from collections import Counter

MAPS=tuple(tuple(sum((((x>>(2-s[j]))&1)^b[j])<<(2-j) for j in range(3)) for x in range(8)) for s in permutations(range(3)) for b in product((0,1),repeat=3))
FIX=tuple(tuple(sum(1<<x for x in range(8) if MAPS[a][x]==MAPS[h][x]) for h in range(48)) for a in range(48))
FLOOR={0,1,2,4,8,16,32,64,128}
PHI=tuple(sum(1<<s for s in range(256) if s in FLOOR or not(s&~m)) for m in range(256))
FULL=(1<<256)-1

def stream_records(path):
    # Canonical evidence has one top-level records array, after checks/identities.
    # Preserve bounded memory while skipping the already hash-verified prefix.
    marker='"records":['; decoder=json.JSONDecoder(); buf=''
    with path.open() as f:
        while marker not in buf:
            chunk=f.read(65536)
            if not chunk: raise ValueError('records array missing')
            buf=buf[-len(marker):]+chunk
        buf=buf.split(marker,1)[1]
        while True:
            buf=buf.lstrip()
            if buf.startswith(','): buf=buf[1:].lstrip()
            if buf.startswith(']'): return
            try: record,end=decoder.raw_decode(buf)
            except json.JSONDecodeError:
                chunk=f.read(65536)
                if not chunk: raise
                buf+=chunk; continue
            yield record
            buf=buf[end:]

def classify(p0,p1):
    gain=bool(p1&~p0);loss=bool(p0&~p1)
    return 'TRADEOFF' if gain and loss else 'EXPANSION' if gain else 'CONTRACTION' if loss else 'NULL'

def affine_closure_with_complements(mask):
    points=[x for x in range(8) if mask>>x&1]
    if not points: return 0
    base=points[0]; span={0}
    for direction in [7]+[x^base for x in points]: span |= {v^direction for v in span}
    return sum(1<<(base^v) for v in span)

def summarize(record,unit,stratum):
    h,p,k=unit; arm=record['treatment']; active=arm['constructor']['active'];live=arm['final_live']
    assert h in live and active in live and record['control']['constructor']['active']==0
    m0,m1=FIX[0][h],FIX[active][h];p0,p1=PHI[m0],PHI[m1]
    for label,m in [('control',m0),('treatment',m1)]:
        measured=record[label]['measurement']; observed=sum(1<<s for s in measured['frontier'])
        assert observed==PHI[m]
        diag=measured['executions'][8]
        assert sum(1<<x for x,r in enumerate(diag) if r['success'])==m
    c=sum(1<<t['x'] for t in arm['trace'] if t['actual_correctness'])
    nonidentity_correct=[t['x'] for t in arm['trace'] if t['actual_correctness'] and t['x']!=int(''.join(map(str,t['observations'])),2)]
    certain=255;common_gain=FULL; any_loss=0;all_strict=True;alternatives=Counter()
    for candidate in live:
        good=FIX[active][candidate];certain &= good
        before,after=PHI[FIX[0][candidate]],PHI[good]
        common_gain &= after&~before;any_loss |= before&~after
        cls=classify(before,after);alternatives[cls]+=1;all_strict &= cls=='EXPANSION'
    assert not(c&~certain) and not(certain&~m1)
    closure=affine_closure_with_complements(c); assert not(closure&~certain)
    for x in nonidentity_correct: assert common_gain & (1<<((1<<x)|(1<<(x^7))))
    return {'unit':list(unit),'stratum':stratum,'class':classify(p0,p1),'exact':active==h,'active':active,'live':live,'baseline_success_mask':m0,'final_success_mask':m1,'correct_training_mask':c,'certain_success_mask':certain,'positive_affine_closure_mask':closure,'nonidentity_correct_states':nonidentity_correct,'all_live_worlds_strict_expansion':all_strict,'all_live_worlds_no_loss':not any_loss,'common_gain_masks':[s for s in range(256) if common_gain>>s&1],'live_world_classes':dict(alternatives),'positive_episodes':c.bit_count(),'failures':8-c.bit_count()}

def census(rows):
    nonexact=[r for r in rows if r['class']=='EXPANSION' and not r['exact']]
    def counts(fn,rs=nonexact): return dict(sorted(Counter(str(fn(r)) for r in rs).items()))
    return {'units':len(rows),'classes':counts(lambda r:r['class'],rows),'exact_selected':sum(r['exact'] for r in rows),'singleton_live':sum(len(r['live'])==1 for r in rows),'exact_selected_with_nonsingleton_live':sum(r['exact'] and len(r['live'])>1 for r in rows),'nonexact_expansions':len(nonexact),'nonexact_geometry':counts(lambda r:(r['baseline_success_mask'].bit_count(),r['final_success_mask'].bit_count())), 'nonexact_positive_episodes':counts(lambda r:r['positive_episodes']),'nonexact_live_sizes':counts(lambda r:len(r['live'])),'nonexact_certain_sizes':counts(lambda r:r['certain_success_mask'].bit_count()),'nonexact_certain_equals_actual':sum(r['certain_success_mask']==r['final_success_mask'] for r in nonexact),'nonexact_certain_stronger_than_positive_affine_closure':sum(r['certain_success_mask']!=r['positive_affine_closure_mask'] for r in nonexact),'nonexact_with_nonidentity_correct':sum(bool(r['nonidentity_correct_states']) for r in nonexact),'nonexact_joint_certification':counts(lambda r:(r['all_live_worlds_strict_expansion'],r['all_live_worlds_no_loss'],bool(r['common_gain_masks']))),'nonexact_all_live_worlds_strict_expansion':sum(r['all_live_worlds_strict_expansion'] for r in nonexact),'nonexact_all_live_worlds_no_loss':sum(r['all_live_worlds_no_loss'] for r in nonexact),'nonexact_common_gain_nonempty':sum(bool(r['common_gain_masks']) for r in nonexact),'nonexact_has_live_world_loss':sum(any(r['live_world_classes'].get(c,0) for c in ['CONTRACTION','TRADEOFF']) for r in nonexact)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--v1-output',type=Path,required=True)
    parser.add_argument('--v0-archive',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(); INPUT=args.v1_output; OUT=args.output
    OUT.mkdir(parents=True,exist_ok=False)
    receipt=json.loads((INPUT/'receipt.json').read_text())
    assert hashlib.sha256((INPUT/'receipt.json').read_bytes()).hexdigest()=='4b41b91ea06af7d5f9b77ee33b523bdb178f7c321c17af8aa33dcdd546aa44f2'
    for name in ['primary.json','evidence.json']:
        with (INPUT/name).open('rb') as f: assert hashlib.file_digest(f,'sha256').hexdigest()==receipt['artifacts'][name]
    primary={tuple(r['unit']):r for r in json.loads((INPUT/'primary.json').read_text())['rows']}
    rows=[]
    for r in stream_records(INPUT/'evidence.json'):
        unit=tuple(r['unit']); pr=primary[unit]
        assert all(r[f]==pr[f] for f in ('unit','stratum','phi_control','phi_treatment','delta_plus','delta_minus'))
        rows.append(summarize(r,unit,r['stratum']))
    assert len(rows)==len({tuple(r['unit']) for r in rows})==len(primary)==9216
    archive=args.v0_archive
    assert hashlib.sha256(archive.read_bytes()).hexdigest()=='cb9e444d1264b68013ead4c895fc5717b70bd310d6523cd6f091460c748021ff'
    with zipfile.ZipFile(archive) as z:
        raw=z.read('trajectories.json')
        assert hashlib.sha256(raw).hexdigest()=='aad6a6782c55f74537d274f78e53668daafddc6834a929ca4efde8018c0795b7'
        v0=[summarize(r,(r['unit'][0],0,r['unit'][1]),'HISTORICAL_P0') for r in json.loads(raw)['units']]
    p0={tuple(r['unit']):r for r in rows if r['stratum']=='HISTORICAL_P0'}
    assert len(v0)==320 and all(r==p0[tuple(r['unit'])] for r in v0)
    summary={'standing':'POST_EXECUTION_DERIVED_NON_PREREGISTERED','source_commit':'c2b99a917b6d7ca54a4eea8f22e59646fd23fbb9','v1_primary_sha256':receipt['primary_sha256'],'v1_evidence_sha256':receipt['evidence_sha256'],'v0':census(v0),'v1':{s:census([r for r in rows if r['stratum']==s]) for s in sorted({r['stratum'] for r in rows})},'noncontrol_combined':census([r for r in rows if r['unit'][0]>=8]),'learner_runs':0}
    (OUT/'CENSUS.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    payload=(json.dumps({'standing':summary['standing'],'rows':sorted(rows,key=lambda r:r['unit'])},sort_keys=True,separators=(',',':'))+'\n').encode()
    (OUT/'UNIT_ANALYSIS.json.gz').write_bytes(gzip.compress(payload,mtime=0))
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
