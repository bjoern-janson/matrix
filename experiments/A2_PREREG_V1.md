# A2-V1 — Active-Survivor Priority × Encounter-Order Factorial

**Protocol ID:** `A2-PREREG-V1`. **Standing:** FROZEN at the commit introducing this file. **Date:** 2026-09-06.

This is a prospective factor-separation protocol, motivated by the completed A2-V0 analysis. It freezes the design and reference authorities before V1 implementation or execution. This commit contains neither a V1 assay implementation nor any V1 validation/scientific execution. The archived Python script performs group mathematics only.

## 1. Scientific question and non-null framing

Separate the effects of cyclic encounter order and active-survivor priority on the corrective frontier, and identify whether the consequence of encounter order depends on survivor priority, while holding the environment, feedback/update rule, realization boundary, and resource contract fixed.

A2-V0 already shows encounter-order outcome-class sensitivity in 35 of 40 noncontrol worlds under the original priority. Therefore universal encounter-order invariance is already falsified. V1 is **not** a fresh existence test for order sensitivity. No global no-effect null, residual-existence null, significance threshold, weighted deployment endpoint, or post-hoc rescue criterion is registered.

The prospective targets concern the complete finite pattern across the other priorities and its effect modification. A null or an absence of a particular derived structure remains an admissible result. Previously observed and theorem/covariance-determined endpoints retain their provenance when included in the complete map.

## 2. Authorities and frozen artifacts

The source state is `bjoern-janson/matrix@1a73502759a308f99d09de88aca67f0dfdcfd412`. The V0 execution was archived at `67232842a213fa33f5a8568baa772c82c2b032af`; the intervening structural analysis does not change its implementation or endpoints.

Authoritative inputs:

| Input | Binding |
|---|---|
| Frozen model | V0 `implementation/a2_v0/model.py`, Git blob `f3aab0759b994aa06e961c62e7dfc27e8573fcf3` |
| V0 scientific source digest | `dd454df0cf646b44a11f91bc965ab5a40de1e62c860dacdf0e988d32205dc02d` |
| Priority family audit JSON | `a11c989c0a72d4d0363077ce353fd5642f708933adedee475ca2c1678497bb2c` |
| Theorem-control prediction JSON | `aa274d3038c9a6633a35a3ef66395773bb27413e8768f0956b878667941deaf5` |
| Historical V0 compact endpoint | Git blob `e8d98cc19a80a1308410559df8386eddcea96ab7` at the source state |
| Reconstructed historical full primary JSON | SHA-256 `3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117` |

The audit files are archived under [`a2_v1/audit/`](a2_v1/audit/). The typo correction and both package identities are documented in [`a2_v1/audit/ERRATUM.md`](a2_v1/audit/ERRATUM.md) and [`a2_v1/CUSTODY.md`](a2_v1/CUSTODY.md). The historical audit JSON correctly retains its original `AUDITED_CANDIDATE_NOT_PREREGISTRATION` standing. **This protocol adopts its exact priority arrays as frozen inputs**; the archive's historical labels are not rewritten.

[`a2_v1/PREREG_CONTRACT.json`](a2_v1/PREREG_CONTRACT.json) records constants, phases, output encoding, and identities. It is a machine-readable companion, not a replacement for the formulas and proofs here. Any substantive discrepancy between these frozen authorities invalidates execution pending a recorded pre-execution amendment; an implementation may not silently choose the convenient interpretation.

## 3. Fixed environment, learning, and realization

States are \(\Omega=\{0,\ldots,7\}\), encoding three bits most significant first. Hypotheses are the 48 affine coordinate permutations

\[
T_{\sigma,b}(x)_j=x_{\sigma(j)}\oplus b_j,
\]

in V0 lexicographic order: permutations of `(0,1,2)`, followed by masks `000` through `111`. Identity is original hypothesis index 0.

Each episode queries coordinates 0, 1, and 2 once in that order, yielding \(y=T_{h^\star}(x_t)\), then repairs the state predicted by the selected active decoder. Training lasts exactly eight episodes with \(x_t=(k+t)\bmod8\), \(t=0,\ldots,7\). Every rotation uses the same eight states once each.

Initial live set is \(L_0=\mathcal H\). Let \(\hat x_t=d_{\hat h_t}(y_t)\). Treatment receives `(True, s_t)` with \(s_t=\mathbf1[\hat x_t=x_t]\). Control receives `(False, False)`. With informative feedback, the update is exactly

\[
L_{t+1}=\{h\in L_t:\mathbf1[d_h(y_t)=\hat x_t]=s_t\}.
\]

With invalid/noninformative feedback, the computed proposal is discarded and the live set remains unchanged. Both arms still process all 48 hypotheses on every episode. No additional feedback, labeled training examples, selected experiments, memory transfer, or post-assignment analyst help is allowed.

The only learner intervention is the fixed priority used to choose \(\hat h_t\) from the live set. It may not change decoding, updates, feedback validity, the training corpus, or the available repair policy menu. All original hypothesis IDs preserve their meanings.

After training, learning freezes. Constructor-visible state remains exactly `(SWITCHBOARD_3, active_hypothesis_index)`. It exposes neither priority, version space, hidden truth, training trace, nor the uncertainty set under evaluation. Exactly nine policies are realized: eight immediate repairs and the one diagnostic decoder generated by that active hypothesis.

Each query and repair costs 1; each evaluation policy realization costs 1. Evaluation budget remains \(B=5\): immediate repairs cost 2 and diagnostic execution costs 5. Training charges remain 4 primitive action units plus 1 complete 48-hypothesis processing-batch unit per episode: **40 charged units and 384 hypothesis checks per arm**. Selection work is included in that fixed abstract batch convention. This is not a wall-clock equivalence claim.

## 4. Frozen priority factor

Multiplication means composition of transformations, with the source's tuple convention. Generate \(c_g(h)=ghg^{-1}\) for all 48 \(g\) and apply it elementwise to the original ordered list. Deduplicate by exact list equality. The stabilizer is \(Z(G)=\{e,(\mathrm{id},111)\}\), yielding exactly 24 distinct lists.

For each duplicate pair, use its smaller original hypothesis index as representative. Sort representatives increasingly and assign IDs `P0..P23`:

`0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27,32,33,34,35,40,41,42,43`.

For representative \(g\), selection is

\[
\hat h_t=S_{P_g}(L_t)=\arg\min_{h\in L_t}\operatorname{rank}_{P_g}(h),
\qquad \operatorname{rank}_{P_g}(h)=\operatorname{index}(g^{-1}hg).
\]

Rank is unique. `P0` is the original lexicographic priority. `P3` is represented by original hypothesis 3; its conjugation equals that of hypothesis 4 because they differ by the central complement.

Every priority puts identity first. Since \(L_t^-=\mathcal H\), the untreated decoder is always identity, hence

\[
\Phi_h^-(P,k)=\Phi_h^-\quad\forall P,k.
\]

Every list retains the eight translations first and preserves conjugacy class at each rank. The hypothesis at rank 7 remains the all-bit complement. No rank outside this 24-member family is included. Distinct lists are not presumed behaviorally distinct, and no outcome-based deduplication is permitted.

## 5. Units and four epistemic strata

A paired cell is \(u=(h,P,k)\), with original hypothesis index \(h\in\{0,\ldots,47\}\), priority ID \(P\in\{0,\ldots,23\}\), and rotation \(k\in\{0,\ldots,7\}\). Every cell contains two isolated potential systems sharing its world, priority, schedule, initial live set, and charged resources; feedback validity is the arm difference.

| Stratum code | Membership | Paired cells | Epistemic standing |
|---|---|---:|---|
| `THEOREM_CONTROL` | \(h<8\), all \(P,k\) | 1,536 | Analytically predicted |
| `HISTORICAL_P0` | \(h\ge8,P=0\), all \(k\) | 320 | Previously observed in V0 |
| `COVARIANCE_P3` | \(h\ge8,P=3\), all \(k\) | 320 | Determined from P0 by covariance |
| `PROSPECTIVE_TARGET` | \(h\ge8,P\notin\{0,3\}\), all \(k\) | 7,040 | Not executed; not certified wholly analytically unresolved |
| **Complete factorial** | all cells | **9,216** | Provenance-stratified map |

The strata are disjoint and exhaustive. “Prospective” concerns planned execution relative to this freeze, not proof that every endpoint lacks an analytic solution. No residual null is inferred from the count 7,040. These are finite census cells, not IID draws or population probability estimates.

Within each phase, iterate cells lexicographically by `(h, priority_id, rotation)`. The archived theorem-prediction table has a different column order; consume its named columns and match by unit identity, not by row position. Both arms must be freshly initialized per cell. No live state, mutable cache, or learned information may cross cells or arms.

## 6. Exact pre-science reference authorities

### 6.1 Translation theorem controls

Use the frozen `THEOREM_CONTROL_PREDICTIONS.json`. A true translation of priority rank \(r\le7\) produces exactly \(r\) failed predictions before becoming active. Every different translation is wrong on every training state, and each failure removes exactly the active translation from that subgroup. All treatment endpoints therefore use the exact true decoder within eight episodes, independently of rotation.

- Identity: 192 NULL signatures; both frontiers are \(2^\Omega\), both difference sets empty.
- Other translations: 1,344 EXPANSION signatures; control frontier is the empty set plus eight singletons; treatment frontier is \(2^\Omega\); \(\Delta^+\) is all 247 nonsingleton subsets and \(\Delta^-=\varnothing\).

Match every full signature, final active hypothesis, and theorem-predicted failure count. Aggregate class counts alone do not suffice.

### 6.2 Historical P0 references

Use `a2_v0/results/primary_compact.json` at the pinned source state. For each recorded diagnostic success mask \(A\), reconstruct

\[
\Phi(A)=\{S\subseteq\Omega:|S|\le1\}\cup2^A.
\]

Match both arm frontiers and both directed differences for every historical cell. The reconstruction of the full historical primary JSON must reproduce its sealed SHA-256 above, using V0's canonical serialization and schema. The V0 utility columns are historical custody only and are not V1 endpoints or gate criteria.

### 6.3 Covariance P3 references

Let \(q=h^{(4)}=(\mathrm{id},100)\), so \(q(x)=x\oplus4\). For each historical `(h,P0,k)`, the target reference identity is

\[
(c_q(h),P3,(k+4)\bmod8).
\]

Transport each set \(S\) by \(q(S)=\{x\oplus4:x\in S\}\), and transport every member of each frontier and difference family. This gives all 320 distinct P3 expected endpoints. The model's composition convention, not a guessed numeric index mapping, defines \(c_q(h)\).

The covariance proof preserves decoder equality, feedback, updates, selection, and the shifted schedule. P3 references must be generated solely from the pinned historical records and this map, not from a V1 learner run. Reference compilation must be hash-bound before any V1 paired execution. It is deterministic reference preparation, not scientific execution. It may not inspect or generate prospective target trajectories/endpoints.

## 7. Strict validation and execution order

Before any V1 execution, verify all source/reference identities, the 24 rank arrays, unit partition, immutable priority configuration, and expected-reference compilation. A future implementation must have a separate source digest recorded before its scientific command begins.

The science command must then, in its own process, perform these phases in order:

1. Execute all **1,536 theorem-control pairs** and match every predicted signature.
2. Execute all **320 historical P0 pairs** and reproduce every endpoint.
3. Execute all **320 covariance P3 pairs** and match every transported endpoint.
4. Finish all required invariant checks on these validation records and seal a validation receipt.
5. Only after all of the above pass, execute exactly the **7,040 prospective target pairs**.
6. Check all prospective execution invariants and complete the output seals described below.

A failure at any point sets `INVALID_NO_SCIENTIFIC_RESULT`, records the reason and last completed phase, and stops. Specific reasons include `THEOREM_CONTROL_MISMATCH`, `P0_REPLAY_MISMATCH`, `P3_COVARIANCE_MISMATCH`, and `INVARIANT_MISMATCH`. The 2,176 reference executions remain validation, not new scientific discoveries.

Any mismatch before step 5 must leave the prospective execution counter at zero. A failure during or after prospective execution invalidates that entire attempted scientific run; partial rows may be retained as diagnostic evidence but cannot be scientifically interpreted. No failed cell may be omitted, repaired in place, or replaced by a convenient subset.

A validation-only command may perform steps 1–4 but must execute zero prospective cells. A stored PASS receipt cannot substitute for the science command's fresh gate. A resumed process or software revision must begin a new immutable attempt with a fresh gate, not continue an interrupted attempt under the old receipt. This protocol specifies the eventual order; **this preregistration commit authorizes no execution**.

## 8. Required execution invariants

The future implementation must verify all of the following, without importing V0's old count of 19 checks as an unexamined target:

1. Exact frozen hypothesis/state/priority arrays and disjoint, complete unit strata.
2. Matched initial state, world, priority, schedule, query slots, feedback opportunities, resources, and isolated mutable state within each pair; no cross-pair leakage.
3. Exactly eight episodes, three ordered queries and one repair per episode, 48 candidate checks per update, 384 checks and charge 40 per arm.
4. Correct treatment token; control token exactly `(False, False)`; no extra channel into the learner.
5. Truth retained after every treatment update; live set only shrinks; the control live set stays full.
6. Active hypothesis is exactly the least-ranked live original hypothesis; active **rank** never decreases. Numeric original hypothesis index is not required to be monotone under a nonlexicographic priority.
7. Update results agree with the stated equality predicate. On informative feedback, correctness preserves active selection and incorrectness removes it; noninformative feedback leaves selection unchanged. Independent checking must not merely call the same update implementation.
8. Constructor input has exactly the frozen task and active hypothesis fields; policies cannot read priority, hidden truth, full live set, or evaluation uncertainty set.
9. Exactly nine realized policies, declared actions only, same policy witness for all states in a jointly correctable set, and correctly charged realization/query/repair costs.
10. Evaluate all nine policies on all eight states and all 256 subsets; independent algebraic success/frontier checks agree with execution. Frontiers are downward closed and include every singleton and the empty set.
11. Evaluation does not change learner state; control frontier is invariant over priority and rotation for each true world.
12. Every measured \(\Delta^+\) and \(\Delta^-\) is the exact directed set difference of the recorded arm frontiers; no scalar substitute.
13. For every changed-frontier pair, bidirectional active-constructor-state transplantation reproduces the donor's frontier within that pair's same world. This is a contract check only; failure is an invariant violation, not a new mediation finding.
14. Phase ordering, execution counters, source/reference identities, seals, and output unit uniqueness/coverage agree with the declared run mode. Validation and reference compilers cannot touch prospective cells.

No learned-state or success-set information from later cells may help earlier selections. Priority is fixed before training and cannot be selected retrospectively based on outcomes.

## 9. Primary output and serialization

For each cell define

\[
\Gamma_h(P,k)=\bigl(\Delta_h^+(P,k),\Delta_h^-(P,k)\bigr),
\quad
\Delta_h^+=\Phi_h^+(P,k)\setminus\Phi_h^-,
\quad
\Delta_h^-=\Phi_h^-\setminus\Phi_h^+(P,k).
\]

The primary scientific object is the complete map \((h,P,k)\mapsto\Gamma_h(P,k)\), retaining all four provenance strata. Store both arm frontiers alongside the two difference families, permitting exact reconstruction and verification. Each row contains `unit=[h,priority_id,k]`, `stratum`, `phi_control`, `phi_treatment`, `delta_plus`, and `delta_minus`.

Encode a state subset by its eight-bit mask: bit \(x\) indicates membership of state \(x\). Encode each family as an ascending list of these subset masks. These integers encode sets, not a scalar valuation. Store rows in lexicographic unit order. Control baselines must agree across the rows for each \(h\).

Canonical JSON uses UTF-8, `sort_keys=True`, separators `(',', ':')`, no nonfinite numbers, and one trailing newline. No weighted utility, cardinality objective, or preferred scalar tradeoff resolution is a V1 endpoint. Class labels EXPANSION/NULL/CONTRACTION/TRADEOFF may be derived from emptiness of the two difference sets and reported as descriptive finite counts with stratum labels; they cannot replace the primary map.

## 10. Preregistered exact derived structures

Define the scientific reporting domain \(H_N=\{h^{(8)},\ldots,h^{(47)}\}\). The full map still includes all control worlds, but their corresponding sensitivity structures are analytically empty and must not inflate prospective findings.

Encounter-order sensitivity:

\[
\mathcal E_K=\{(h,P)\in H_N\times\mathcal P:
\exists k,k'\;\Gamma_h(P,k)\ne\Gamma_h(P,k')\}.
\]

Priority sensitivity:

\[
\mathcal E_P=\{(h,k)\in H_N\times K:
\exists P,P'\;\Gamma_h(P,k)\ne\Gamma_h(P',k)\}.
\]

Define the directed encounter contrast with fixed orientation:

\[
D_K(h,P;k,k')=(\Phi_h^+(P,k)\setminus\Phi_h^+(P,k'),
                 \Phi_h^+(P,k')\setminus\Phi_h^+(P,k)).
\]

Priority × encounter-order effect modification:

\[
\mathcal E_{PK}=\{h\in H_N:\exists P,P',k,k'\;
D_K(h,P;k,k')\ne D_K(h,P';k,k')\}.
\]

Comparisons may use \(P<P'\) and \(k<k'\) for deterministic enumeration without changing these existential definitions. Retain exact memberships and, for each positive membership, the lexicographically first witness using the displayed variable order. Counts are secondary summaries of these exact structures. These definitions identify conditional sensitivity/effect modification; they do not imply a unique additive decomposition or percentages of causal attribution.

Because \(\Phi_h^-\) is fixed, \(\Phi_h^+=(\Phi_h^-\setminus\Delta_h^-)\cup\Delta_h^+\); thus the complete primary map determines all contrasts without an added endpoint.

## 11. Two distinct loss-persistence structures

Across priorities at fixed \((h,k)\), define

\[
L_{\rm any}^{P}=\{(h,k):\forall P,\Delta_h^-(P,k)\ne\varnothing\},
\qquad
C_{h,k}^{P}=\bigcap_P\Delta_h^-(P,k),
\qquad
L_{\rm common}^{P}=\{(h,k):C_{h,k}^{P}\ne\varnothing\}.
\]

Across encounters at fixed \((h,P)\), define

\[
L_{\rm any}^{K}=\{(h,P):\forall k,\Delta_h^-(P,k)\ne\varnothing\},
\qquad
C_{h,P}^{K}=\bigcap_k\Delta_h^-(P,k),
\qquad
L_{\rm common}^{K}=\{(h,P):C_{h,P}^{K}\ne\varnothing\}.
\]

Use \(h\in H_N\) throughout. Report both exact membership sets and the actual common-loss families \(C^P,C^K\), including empty families. “Every priority loses something” does not mean “the same correction opportunity is lost under every priority.” Common loss implies loss everywhere; the converse is not assumed. The analogous distinction holds over encounter rotations.

## 12. Custody, output order, and interpretation

Before any execution, seal the implementation source identity, this preregistration's identity, the frozen artifact identities, the unit manifest, and deterministic expected references. A successful fresh validation receipt must bind its 2,176 per-unit records and all invariant results.

After prospective execution, finish all mandatory invariants and transplantation checks before admitting a completed primary result. Seal the complete primary map first. Only then compute and seal the registered sensitivity/effect-modification and loss-persistence structures, each bound to the primary hash. Preserve both arms' training trajectories, constructor states, evaluation evidence, phase/call counters, and contract-check records in immutable artifacts. Seal a final receipt binding all artifacts, code/protocol/reference identities, runtime version, and phase status. Successful completion requires exactly 7,040 prospective paired cells and all 9,216 cells accounted for once in the combined map.

Reference observations keep their original epistemic labels even when reexecuted. Do not present 9,216 new discoveries, or count a P0/P3 reference reproduction as new existence evidence. No rows, priorities, worlds, or rotations may be removed based on observed outcomes. No result-dependent stopping is allowed except invalidation on a contract failure. Any additional interpretation not specified here must be labeled post-execution and cannot amend the primary record.

A semantic change to priorities, strata, references, learner, resources, endpoints, gating, or interpretation rules requires a separately identified amendment before the affected execution. Preserve the original protocol and any failed receipts; neither a fix nor a rerun may overwrite them. No implementation may silently weaken a required check to obtain PASS.

## 13. Claim ceiling and terminal state of this commit

The study concerns this finite signed-permutation environment, these 24 conjugation-generated identity-first priorities, these eight cyclic rotations, and this version-space elimination learner with its nine-policy realization architecture.

It does not establish results for arbitrary identity-first rankings, all \(8!\) encounter orders, arbitrary search policies, active experiment choice, other learners/environments, general corrigibility, or general self-improvement. The transplantation result remains a constructor-boundary contract check. The set-valued effect-modification criterion is not an ANOVA model or a general mechanism law. **MATRIX1 remains unearned.**

At this preregistration commit: mathematical audit complete; exact priority family adopted; references specified; protocol frozen; V1 implementation absent; V1 validation not run; V1 prospective execution not run; no V1 scientific result.
