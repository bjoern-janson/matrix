# Expansion without exact hypothesis recovery — post-execution analysis V0

**Standing:** POST-EXECUTION / DERIVED / NON-PREREGISTERED.  
**Scope:** sealed A2-V0 records and the complete already-executed A2-V1 factorial.  
**Source checkpoint:** `c2b99a917b6d7ca54a4eea8f22e59646fd23fbb9`.

This analysis studies strict frontier expansion when the final selected hypothesis differs from the hidden truth. It performs no learner runs, prospective execution, new assay, or result-dependent alteration of the historical endpoints. The additional certificates below are post-execution mathematical checks, not preregistered V1 endpoints and not a new MATRIX kernel object.

## 1. Inputs and provenance

The sealed V1 output archive is repository-resident at [../execution/artifacts/a2-v1-prospective-output.tar.gz](../execution/artifacts/a2-v1-prospective-output.tar.gz). Its SHA-256 is `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7`.

| Input | SHA-256 |
|---|---|
| V1 final receipt | `4b41b91ea06af7d5f9b77ee33b523bdb178f7c321c17af8aa33dcdd546aa44f2` |
| V1 primary | `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076` |
| V1 raw evidence | `6e3188b33a2640133cbdd4b9d91b48513cbd2dfc80c96c21efb561932961c1d1` |
| V0 scientific ZIP | `cb9e444d1264b68013ead4c895fc5717b70bd310d6523cd6f091460c748021ff` |
| V0 trajectories | `aad6a6782c55f74537d274f78e53668daafddc6834a929ca4efde8018c0795b7` |

The mining script verifies these receipt/primary/evidence and V0 ZIP/trajectory identities, compares all 9,216 raw V1 endpoint rows to the sealed primary, and compares each reconstructed success set against the recorded diagnostic executions and full frontier. It also matches all 320 V0 analyses exactly against V1's historical P0 slice. The V0 source archive is the historical package identified in [../../a2_v0/CUSTODY.md](../../a2_v0/CUSTODY.md); its bytes were already retained locally for this pass.

The V1 P0 and P3 reference slices each reproduce the 52-case V0 pattern. They retain historical/covariance provenance; they are not two fresh replications. The 7,040 PROSPECTIVE_TARGET cells below were prospective at the V1 freeze and have already been executed. Mining them now is retrospective analysis.

## 2. The phenomenon extends across V1

For final active hypothesis \(a\), actual truth \(h^\star\), and original baseline decoder 0, retain the established reduction

\[
A_0=\operatorname{Fix}(T_0^{-1}T_{h^\star}),\qquad
A_1=\operatorname{Fix}(T_a^{-1}T_{h^\star}),\qquad
\Phi_5(A)=\{S:|S|\le1\}\cup2^A.
\]

A non-exact expansion here means \(a\ne h^\star\) and strict frontier inclusion. In this architecture, its three possible success-set transitions are empty-to-line, empty-to-plane, and line-to-containing-plane.

| Success-set transition | V0 / historical P0 | Covariance P3 | V1 prospective stratum |
|---|---:|---:|---:|
| Empty to 2-state line | 18 | 18 | 408 |
| Empty to 4-state plane | 27 | 27 | 670 |
| 2-state line to containing 4-state plane | 7 | 7 | 198 |
| **Non-exact expansions** | **52** | **52** | **1,276** |
| All strict expansions | 254 | 254 | 5,376 |
| Final selected hypothesis equals truth | 202 | 202 | 4,100 |

Thus the combined noncontrol map contains 1,380 non-exact expansions among 5,884 expansions. These are finite census counts, not population estimates. Translation theorem controls contribute none: their final selected hypothesis is always true.

## 3. Actual improvement versus a certificate from the final live set

The sealed trajectories retain the final survivor set \(L=L_8\), with \(h^\star\in L\) and \(a\in L\). For an arbitrary surviving hypothesis \(h\), define analysis-local families

\[
F_a(h)=\Phi_5\!\left(\operatorname{Fix}(T_a^{-1}T_h)\right),\qquad
F_0(h)=\Phi_5\!\left(\operatorname{Fix}(T_0^{-1}T_h)\right).
\]

These are algebraic evaluations of a fixed final decoder against the retained candidate operators. No alternative training trajectory is executed.

Compute two different properties:

\[
\forall h\in L:\ F_0(h)\subseteq F_a(h)
\quad\text{(preservation for every surviving hypothesis),}
\]

\[
J=\bigcap_{h\in L}\bigl(F_a(h)\setminus F_0(h)\bigr)
\quad\text{(particular gains shared across surviving hypotheses).}
\]

Also check strict expansion separately for every \(h\in L\). Universal strict expansion need not in general imply that the same gain is shared; the census explicitly checks both. In the selected non-exact-expansion cases here, every universal strict-expansion case has \(J\ne\varnothing\).

| Within actual non-exact expansions | V0 / P0 | P3 | V1 prospective stratum |
|---|---:|---:|---:|
| Strict expansion under every survivor, with a common gain | **34** | 34 | **580** |
| Common gain, but some survivor permits loss | **2** | 2 | **60** |
| Preservation under every survivor, but some survivor gives a null | **2** | 2 | **36** |
| Some survivor permits loss, and no common gain | **14** | 14 | **600** |
| **Total** | **52** | **52** | **1,276** |

Consequently:

- 34/52 V0 and 580/1,276 prospective-stratum non-exact expansions have a strict-expansion certificate from the retained survivor set.
- 36/52 and 640/1,276 have at least one particular newly correctable uncertainty set shared across every survivor.
- 16/52 and 660/1,276 still admit a loss-bearing candidate operator.

All 1,276 prospective-stratum cases remain genuine strict expansions in their actual recorded worlds. A failure of the universal check does not relabel their historical outcome; it limits what the retained survivor set alone establishes.

These certificates are conditional on the frozen hypothesis class, truthful feedback, truth retention, and fixed nine-policy semantics. The retained \(L\) is the learner's explicit surviving set, not a claim to exhaust all information an analyst could extract from the full schedule and trajectory. Additional information might narrow uncertainty further.

The existing learner does not compute these certificates. Its evaluation constructor does not receive \(L\). This analysis shows that the retained data suffice for the stated mathematical checks; it does not show that the system recognizes, selects on, or deploys a certified improvement.

## 4. Why one successful correction can establish a joint gain

Define the analysis-local guaranteed diagnostic success set

\[
K(a,L)=\bigcap_{h\in L}\operatorname{Fix}(T_a^{-1}T_h).
\]

Truth retention immediately gives \(K(a,L)\subseteq A_1\).

Suppose an episode attempts repair \(z\), receives correct feedback, and observed vector is \(y\). Every surviving hypothesis then satisfies

\[
d_h(y)=z,\qquad T_h(z)=y.
\]

The final selected \(a\in L\) satisfies the same equality. Thus the final decoder is correct on \(z\) under every \(h\in L\).

Every signed coordinate permutation commutes with bitwise complementation:

\[
T_h(z\oplus111)=T_h(z)\oplus111.
\]

Therefore the same diagnostic is correct on both \(z\) and \(\bar z=z\oplus111\) under every survivor. This is a two-state joint success guarantee, even when only one of those states was predicted correctly during training.

If \(y\ne z\), the identity baseline is wrong on both states under every survivor. No immediate-repair policy can jointly repair two distinct states. Consequently

\[
\boxed{\{z,\bar z\}\in J.}
\]

One correct nonidentity repair therefore suffices to establish a particular new joint correction opportunity under the frozen contracts. Exact recovery of \(h^\star\) is unnecessary. This says nothing about preserving other baseline opportunities.

In the non-exact-expansion census:

| Property | V0 / P0 | V1 prospective stratum |
|---|---:|---:|
| At least one correct nonidentity training repair | 36 | 640 |
| A common guaranteed gain \(J\ne\varnothing\) | 36 | 640 |
| Zero correct predictions in all eight training episodes | 16 | 636 |
| \(K(a,L)=\varnothing\) | 16 | 636 |

The equalities between these census counts are observed properties of these records, not a universal converse to the sufficient condition.

If \(C\) is the set of correctly predicted training states, the same reasoning gives \(C\subseteq K\), including their complements. Each relative fixed set is affine, so the affine hull of \(C\cup\bar C\) is also contained in \(K\). In 10 V0 cases and 92 prospective-stratum cases, the complete final survivor set yields a larger \(K\) than that positive-example affine closure. This is an additional descriptive comparison, not a separately identified causal effect of one feedback type.

## 5. Concrete witnesses

Original hypothesis IDs and priority IDs retain their frozen meanings. State integers encode \(4x_1+2x_2+x_3\); set masks in the machine record use bit \(x\) for state \(x\).

### V0: non-exact selection with guaranteed strict expansion

For \((h^\star,P,k)=(12,0,2)\):

- final selected hypothesis \(a=7\);
- final survivors \(L=\{7,12,23,34\}\);
- \(A_0=\varnothing\), actual \(A_1=\{1,2,5,6\}\);
- only state 1 was predicted correctly during training;
- \(K=\{1,6\}\) and the common newly correctable family is exactly \(\{\{1,6\}\}\);
- all four survivors give strict expansion.

The selected operator is wrong in the actual world, yet both strict expansion and a particular joint gain follow without choosing the true operator from \(L\).

### V0: actual gain with unresolved sign

For \((17,0,1)\):

- \(a=10\), \(L=\{10,13,17,21,26,29,36,37\}\);
- \(A_0=\varnothing\), actual \(A_1=\{1,6\}\);
- all eight training predictions were incorrect;
- \(K=\varnothing\), \(J=\varnothing\);
- the eight retained candidate operators yield four expansions, two nulls and two contractions.

The actual strict expansion does not establish that the retained information certifies its sign.

### V1 prospective stratum: a two-survivor witness

For \((9,12,3)\):

- \(a=33\), \(L=\{9,33\}\);
- \(A_0=\varnothing\);
- actual \(A_1=K=\{0,2,5,7\}\);
- both survivors imply strict expansion.

The two remaining operators need not yield identical final frontiers: candidate 33 makes the selected decoder exact. What is certified is expansion and the common partial capability, not one fully identified operator or frontier.

## 6. A terminology correction: exact selection is not singleton identification

Earlier counts of exact recovery use \(a=h^\star\). This is an evaluator's exact-selected-hypothesis comparison.

It is stronger to require \(L=\{h^\star\}\). Of V0's 202 exact selections, 18 retain multiple hypotheses; only 184 have singleton \(L\). Of the prospective stratum's 4,100 exact selections, 484 retain multiple hypotheses; 3,616 have singleton \(L\).

This does not change any A2 endpoint or earlier numerical count. It makes the epistemic interpretation explicit: selecting the true model and uniquely identifying it from the retained survivor set are different events.

## 7. Artifacts, reproduction, and standing

- [NONEXACT_EXPANSION_CENSUS.json](NONEXACT_EXPANSION_CENSUS.json) — exact stratified summary.
- [NONEXACT_EXPANSION_UNITS.json.gz](NONEXACT_EXPANSION_UNITS.json.gz) — all 9,216 analysis rows, including final active/live IDs, actual/certain success sets, positive-feedback states, candidate-world class counts and exact common-gain families.
- [mine_nonexact_expansion.py](mine_nonexact_expansion.py) — standalone record analysis; imports no A2 learner or runner.
- [NONEXACT_EXPANSION_CUSTODY.json](NONEXACT_EXPANSION_CUSTODY.json) — this analysis's file identities and source bindings.

Extract the sealed V1 tarball into a temporary directory and supply the historical V0 scientific ZIP identified above. Then run:

```sh
python3 mine_nonexact_expansion.py \
  --v1-output /ABSOLUTE/RECOVERED/a2-v1-prospective-output \
  --v0-archive /ABSOLUTE/a2-v0-scientific-run.zip \
  --output /ABSOLUTE/NEW/analysis-output
```

The output directory must be new. The script writes CENSUS.json and UNIT_ANALYSIS.json.gz, corresponding to the named archival files above. JSON values are canonical where compressed; the custody record binds the exact archived gzip bytes.

**Earned:** the post-execution counts, exact partial-success geometry, conditional certificates computed from final survivor sets, and the sufficient positive-feedback/complement argument.

**Not earned:** learner awareness of these certificates, a new selection or deployment mechanism, robustness beyond the frozen class, independent future viability improvement, general corrigibility, an additional prospective result, or MATRIX_1.

The finding is that partial identification sometimes supports a mathematically certified strict corrective expansion, while other actual expansions remain compatible with losses under the retained candidate operators. No new assay is frozen by this analysis.

