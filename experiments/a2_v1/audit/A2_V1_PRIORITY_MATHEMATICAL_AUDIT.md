# A2-V1: mathematical audit of the proposed conjugation priorities

Date: 2026-09-06. Standing: **PRE-REGISTRATION MATHEMATICAL AUDIT / CANDIDATE FAMILY**.

**Verdict:** the proposed conjugation family is well-defined and has exactly **24 distinct priority orders**. Every order starts at the original identity hypothesis. The untreated baseline is unchanged. The family is a restricted intervention on active-survivor priority, with explicit invariants described below.

This document is not the A2-V1 preregistration. No A2-V1 learner, assay runner, training trajectory, or scientific endpoint has been implemented or executed. No repository file was modified. Enumerating group operations, priority lists, and theorem-predicted control signatures is the only computation performed by the accompanying audit script.

## 1. Source and convention

Source was read from `bjoern-janson/matrix` at commit `1a73502759a308f99d09de88aca67f0dfdcfd412`, whose direct parent is the reported structural-analysis commit `4f28e4fb00a9342824330c7587ab22ab54286be2`. The newer commit clarifies version-space refinement and interaction-generated evidence; the mathematical audit uses the frozen A2-V0 model.

[Pinned model.py](https://github.com/bjoern-janson/matrix/blob/1a73502759a308f99d09de88aca67f0dfdcfd412/experiments/a2_v0/implementation/a2_v0/model.py)

- Model Git blob: `f3aab0759b994aa06e961c62e7dfc27e8573fcf3`.
- Model SHA-256: `6ab7a3a27d7be6aed5f7743f6b302e1264c958eef8f1c45b367562613f850eef`.
- The locally retained source matches both identities.

Write states as column vectors in \(\mathbb F_2^3\), with integer encoding `000` through `111`, most significant bit first. The implementation defines

\[
T_{\sigma,b}(x)_j=x_{\sigma(j)}\oplus b_j.
\]

Hypotheses are lexicographically ordered by `permutations(range(3))`, then `product((0,1), repeat=3)`. Thus \(h^{(0)}=(\mathrm{id},000)\) and \(h^{(7)}=(\mathrm{id},111)\).

Define multiplication by **function composition**: \(T_{a*b}=T_a\circ T_b\). For \(a=(\sigma,b)\), \(d=(\tau,c)\), the tuple convention gives

\[
a*d=(\tau\circ\sigma,\ b\oplus(c\circ\sigma)).
\]

In particular, the tuple permutation appears in reversed order relative to the written function composition. This is a convention to preserve explicitly in any implementation.

The inverse is

\[
(\sigma,b)^{-1}=(\sigma^{-1},\ b\circ\sigma^{-1}).
\]

These 48 bijections are closed under composition and inverse, with the stated identity. They form \(G=\mathbb F_2^3\rtimes S_3\), the group of affine coordinate permutations and bit flips. The audit independently compares tuple multiplication with composition of the eight-state permutation tables, then checks all 110,592 associativity triples.

## 2. Exact conjugation formula and identity preservation

For \(g=(\rho,a)\), \(h=(\sigma,b)\), put \(\sigma'=\rho^{-1}\circ\sigma\circ\rho\). Then

\[
c_g(h)=ghg^{-1}=(\sigma',b'),\qquad
b'_j=b_{\rho(j)}\oplus a_j\oplus a_{\sigma'(j)}.
\]

Generate the ordered list

\[
P_g=(c_g(h^{(0)}),\ldots,c_g(h^{(47)})).
\]

Conjugation is a bijection and fixes the identity, so each list is a permutation of all 48 original hypotheses and \(P_g[0]=h^{(0)}\).

For a live set \(L\), selection means choosing the member with smallest **rank in this list**. Explicitly,

\[
\operatorname{rank}_{P_g}(h)=\operatorname{index}(g^{-1}hg),\qquad
S_{P_g}(L)=\arg\min_{h\in L}\operatorname{rank}_{P_g}(h).
\]

Original hypothesis IDs, environment maps, and decoders must keep their meanings. The intervention changes a rank function; it does not relabel the actual hidden world or decoder semantics. Numeric hypothesis indices need not increase along V1 learning; priority ranks do.

## 3. Center, stabilizer, and the 24 orders

Let \(z=T_{\mathrm{id},111}\), the all-bit complement. Both \(e\) and \(z\) commute with every member of \(G\).

Conversely, a central \(T_{\sigma,b}\) must commute with every translation \(t_v\). This requires \(x_{\sigma(\cdot)}\) to fix every vector \(v\), hence \(\sigma=\mathrm{id}\). Commuting with every coordinate permutation then requires all coordinates of \(b\) to be equal. Therefore

\[
Z(G)=\{e,z\}=\{h^{(0)},h^{(7)}\}.
\]

Since the base priority lists every hypothesis exactly once, preserving this *ordered list* requires fixing every hypothesis individually. Thus its stabilizer under conjugation is exactly \(Z(G)\), with no further stabilizer elements.

\[
P_g=P_{g'}\iff g'^{-1}g\in Z(G),\qquad
|\mathcal P|=|G|/|Z(G)|=48/2=24.
\]

Each duplicate pair consists of \((\rho,a)\) and \((\rho,a\oplus111)\). A deterministic representation is to retain the smaller original index in each pair and order the resulting representatives increasingly. This yields representatives

`0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27,32,33,34,35,40,41,42,43`.

The manifest numbers these priorities `P0` through `P23`. `P0` is the exact A2-V0 lexicographic list. These are audited candidate IDs, not a claim that preregistration has already been finalized.

All 48 generated lists, all 24 deduplicated lists, their generating pairs, and their inverse rank arrays appear in `PRIORITY_FAMILY_AUDIT.json`. Distinct lists need not generate distinct outcomes on the assay's reachable live sets; no behavioral deduplication has been assumed or performed.

## 4. Untreated-baseline invariance

The control arm ignores noninformative feedback, so \(L_t^-=G\). Since every priority ranks \(e\) first, its active hypothesis is always \(e\), regardless of priority or rotation. Constructor input is therefore always `(SWITCHBOARD_3, 0)`.

With environment, policy realization, and budget held fixed,

\[
\Phi_h^-(P,k)=\Phi_h^-\quad\text{for all }h,P,k.
\]

This proves the intended baseline separation. Priority belongs to the frozen learner configuration and does not need to enter the evaluation constructor. A future implementation must preserve the same full 48-hypothesis processing scan and abstract charge convention, including selection work. The audit makes no claim of equal wall-clock cost.

For a fixed baseline, the proposed contrast \(\Gamma=(\Delta^+,\Delta^-)\) retains the entire treatment frontier because

\[
\Phi_h^+=(\Phi_h^-\setminus\Delta_h^-)\cup\Delta_h^+.
\]

Thus equality of these ordered difference pairs is a valid exact sensitivity criterion. The proposed directed set-difference interaction is also well-defined if the orientation of \((k,k')\) is held constant across priorities.

## 5. Restrictions that survive every priority intervention

The translation subgroup \(N=\{(\mathrm{id},b):b\in\mathbb F_2^3\}\) is normal, and

\[
c_{(\rho,a)}(\mathrm{id},b)=(\mathrm{id},b\circ\rho).
\]

Consequently all eight translations remain in the first eight positions under every priority. Translation Hamming weight is preserved. There are only six distinct initial eight-hypothesis orders:

```
0 1 2 3 4 5 6 7
0 1 4 5 2 3 6 7
0 2 1 3 4 6 5 7
0 2 4 6 1 3 5 7
0 4 1 5 2 6 3 7
0 4 2 6 1 5 3 7
```

Both index 0 at rank 0 and index 7 at rank 7 are universally fixed. These are the only hypotheses fixed at their original rank across every list. The only preserved original prefix sets have lengths 1, 7, 8, and 48.

More generally, conjugation preserves the conjugacy class of the hypothesis occupying each rank. The ten classes have sizes `1,3,3,1,6,6,6,6,8,8`; full memberships are recorded in the manifest. Permutation blocks remain blocks, and their cycle-type pattern remains the original one.

Therefore this design tests the **conjugation orbit of the frozen priority**, which is much narrower than all identity-first rankings. Loss under all 24 variants means unavoidable within this family. It does not establish unavoidable loss under arbitrary identity-first priorities or other search mechanisms. This restriction does not invalidate the proposed factorial; it defines its interpretation.

Also distinguish two statements at a fixed \((h,k)\):

\[
\forall P:\Delta_h^-(P,k)\ne\varnothing
\quad\text{and}\quad
\bigcap_P\Delta_h^-(P,k)\ne\varnothing.
\]

The first says every priority loses something. The second says there is a particular correction opportunity every priority loses. The second implies the first; the converse does not hold in general. The user's proposed priority-invariant-loss criterion is the first, and should retain that meaning.

## 6. Extension of the theorem controls

For a true translation \(t_b\), every different translation decoder \(t_a^{-1}\) is wrong on every state:

\[
t_a^{-1}t_b(x)=x\oplus a\oplus b\ne x\quad(a\ne b).
\]

All translations precede all nontranslations in every audited priority. At a wrong translation prediction, incorrectness feedback eliminates exactly that one translation from the translation subgroup; other nontranslations may also be eliminated. The true translation survives.

If the true translation has priority rank \(r\in\{0,\ldots,7\}\), the learner incurs exactly \(r\) failures before selecting it. Subsequent predictions are correct and retain that active hypothesis. Eight episodes suffice independently of encounter order.

Thus the 64 A2-V0 control signatures extend to all 24 priorities:

| True hypothesis | Units | Predicted result | Control frontier | Treatment frontier |
|---|---:|---|---|---|
| Identity | 192 | NULL | \(2^\Omega\) | \(2^\Omega\) |
| Nonzero translation | 1,344 | EXPANSION | empty set and singletons | \(2^\Omega\) |

For expansion controls, \(|\Phi^-|=9\), \(|\Phi^+|=256\), \(|\Delta^+|=247\), and \(\Delta^-=\varnothing\). For null controls, both differences are empty. All treatment active hypotheses equal truth. `THEOREM_CONTROL_PREDICTIONS.json` records all 1,536 predicted signatures and the exact predicted failure count.

These are **mathematical predictions**. Zero of these V1 controls have been executed. They provide an available validation gate for a future implementation; the audit does not create execution authorization.

## 7. A second reference slice is already determined by symmetry

The full eight-rotation schedule family is not invariant under every group element. Exhaustive enumeration gives exactly two state transformations that preserve that literal family: \(e\) and

\[
q=h^{(4)}=(\mathrm{id},100),\qquad q(x)=x\oplus4=(x+4)\bmod8.
\]

This matters for what can be learned from a new run. Simultaneously conjugate the true and candidate hypotheses by \(q\), relabel states and observations by \(q\), and transport the priority accordingly. The decoder identity

\[
T_{c_q(\hat h)}^{-1}(T_q(y))=T_q(T_{\hat h}^{-1}(y))
\]

preserves correctness. It also preserves the update predicate, because applying a bijection preserves equality of the candidate prediction and attempted repair. Priority selection commutes with this relabeling:

\[
c_q(S_{P_g}(L))=S_{P_{qg}}(c_q(L)).
\]

Starting from the full live set, induction over the eight episodes gives covariance of the entire learner trajectory. The constructor still exposes only the transported active hypothesis. Success sets and frontiers transport by the same state bijection. Primitive action counts and query/repair budgets remain the same.

Because \(P_q=P_{h^{(3)}}\), the deterministic family IDs call this transported lexicographic order **P3**. Specifically,

\[
(h,P0,k)\longmapsto(c_q(h),P3,(k+4)\bmod8),
\]

and

\[
\Phi_{c_q(h)}^+(P3,k+4)
=\{q(S):S\in\Phi_h^+(P0,k)\}.
\]

The baseline and both difference sets transport likewise. Conjugation preserves the nontranslation world set, and the mapping covers each of the 320 noncontrol world/rotation pairs exactly once.

Therefore the existing A2-V0 records determine **320 further noncontrol endpoints** at P3 without a new scientific run. This audit proves that relation; it does not read the old trajectory archive, materialize those endpoints, or execute them. They can become transported reference checks. A future mismatch with them would require localizing an implementation or covariance-proof discrepancy.

This does not assert that individual world/rotation endpoints are unchanged: their state labels and world indices are transported. Nor does it make the full design symmetry-invariant, since most group elements map the cyclic schedules outside the chosen encounter-order family.

## 8. Exact grid size and standing

If the original 48-world, eight-rotation universe and its translation-control split are carried forward, then:

| Part | Paired units | Standing before any V1 run |
|---|---:|---|
| Full \(48\times24\times8\) grid | 9,216 | Defined candidate factorial |
| Translation controls | 1,536 | Theorem-predicted |
| Noncontrol \(40\times24\times8\) grid | 7,680 | Includes reference slices below |
| Original P0 noncontrol slice | 320 | Already observed in A2-V0 |
| Transported P3 noncontrol slice | 320 | Determined from P0 by covariance |
| Other 22 noncontrol priority slices | 7,040 | Not run; not certified wholly analytically unresolved |

These are counts of finite paired units, not independent statistical samples. The 7,040-cell remainder must not acquire an unproved residual-existence null or an automatic claim that every cell is analytically unresolved. The audit does not attempt an exhaustive pre-solution of that remainder.

The group family is independent of observed losses: all 48 conjugators were generated and deduplicated by exact list equality only. The overall V1 question was motivated by V0 results, so it is prospective with respect to V1 execution, not historically blind to V0.

## 9. Reproducibility and stopping state

`audit_priority_family.py` uses only Python's standard library. It imports no assay modules, creates no learner, consumes no scientific-run archive, and contains no training loop. It checks 16 groups of algebraic/enumeration assertions, including two independent representations of composition and conjugation. It writes the full candidate family and predicted control signatures with exclusive creation.

To reproduce into a new directory:

```bash
python3 audit_priority_family.py --output-dir reproduced
```

Optionally pass `--source-path /path/to/the/pinned/model.py` to verify the reference model bytes without importing that module. The local audit used this check successfully.

Expected canonical JSON hashes:

- `PRIORITY_FAMILY_AUDIT.json`: `a11c989c0a72d4d0363077ce353fd5642f708933adedee475ca2c1678497bb2c`
- `THEOREM_CONTROL_PREDICTIONS.json`: `aa274d3038c9a6633a35a3ef66395773bb27413e8768f0956b878667941deaf5`

**Completed:** group-convention audit, all 48 conjugations, exact 24-order deduplication, identity-first and stabilizer proofs, structural restrictions, extended control proof, covariance-derived reference slice, and candidate grid accounting.

**Not performed:** final preregistration, assay implementation, V1 control execution, V1 scientific execution, or repository mutation. No MATRIX1 claim is made.
