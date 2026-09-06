# A2-V0 Post-Execution Structural Analysis V0

**Status:** POST-EXECUTION / DERIVED / NON-PREREGISTERED ANALYSIS  
**Program:** MATRIX₀  
**Source repository state:** `67232842a213fa33f5a8568baa772c82c2b032af`  
**Scientific-run archive SHA-256:** `cb9e444d1264b68013ead4c895fc5717b70bd310d6523cd6f091460c748021ff`  
**Raw primary SHA-256:** `3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117`  
**Raw trajectories SHA-256:** `aad6a6782c55f74537d274f78e53668daafddc6834a929ca4efde8018c0795b7`

This document analyzes the already-sealed A2-V0 execution. It does **not** alter the preregistration, reclassify theorem-derived controls as empirical discoveries, change the MATRIX₀ kernel, or authorize MATRIX₁.

The frozen primary result remains:

\[
\boxed{
254\ \mathrm{EXPANSION},\quad
32\ \mathrm{NULL},\quad
18\ \mathrm{CONTRACTION},\quad
16\ \mathrm{TRADEOFF}.
}
\]

The purpose here is narrower: determine the exact finite structure that generated those four classes.

---

## 1. Epistemic partition

Three kinds of statements are kept separate.

1. **Architecture-derived statements** follow mathematically from the frozen signed-permutation world, policy architecture, and learner implementation.
2. **Execution-census statements** are exact facts of the sealed 320-unit scientific run.
3. **Interpretive statements** are finite-assay explanations constrained by the first two and do not generalize beyond A2-V0.

No post-execution observation is retroactively promoted into the preregistration.

---

## 2. Exact reduction to relative fixed sets

For a true hidden transformation \(h^\star\) and final active hypothesis \(\hat h\), define

\[
A(\hat h,h^\star)
=
\{x\in\Omega:d_{\hat h}(T_{h^\star}(x))=x\}.
\]

Equivalently,

\[
\boxed{
A(\hat h,h^\star)
=
\operatorname{Fix}(T_{\hat h}^{-1}T_{h^\star}).
}
\]

Every transformation has the form

\[
T_h(x)=P_\sigma x\oplus b.
\]

For the relative map \(g=T_{\hat h}^{-1}T_{h^\star}\), write

\[
g_i(x)=x_{p(i)}\oplus c_i,
\]

with

\[
p=\sigma^\star\circ\hat\sigma^{-1},
\qquad
c_i=(b^\star\oplus\hat b)_{\hat\sigma^{-1}(i)}.
\]

The fixed-point equations are \(x_i=x_{p(i)}\oplus c_i\). For each cycle \(C\) of \(p\), consistency requires

\[
\bigoplus_{i\in C}c_i=0.
\]

If any cycle violates this parity condition, the fixed set is empty. If all cycles are consistent, there is one free bit per cycle:

\[
\boxed{|\operatorname{Fix}(g)|=2^{\#\mathrm{cycles}(p)}}.
\]

For three bits:

\[
\boxed{|A|\in\{0,2,4,8\}.}
\]

Thus the relative-map cases are:

- identity relative permutation: \(A=\Omega\) only for zero relative mask; otherwise \(A=\varnothing\);
- transposition relative permutation: \(A\) is empty or a four-state plane;
- 3-cycle relative permutation: \(A\) is empty or a two-state antipodal line.

The sealed run agrees with this classification for every control and treatment success set.

---

## 3. Complete fixed-set catalogue

Only **12** diagnostic success sets can occur in A2-V0:

- one empty set;
- four antipodal two-state lines;
- six four-state parity planes;
- the full eight-state cube.

The four lines are

\[
\{0,7\},\quad\{1,6\},\quad\{2,5\},\quad\{3,4\}.
\]

The six planes are

\[
\begin{aligned}
\{0,1,6,7\}&:x_0\oplus x_1=0,\\
\{2,3,4,5\}&:x_0\oplus x_1=1,\\
\{0,2,5,7\}&:x_0\oplus x_2=0,\\
\{1,3,4,6\}&:x_0\oplus x_2=1,\\
\{0,3,4,7\}&:x_1\oplus x_2=0,\\
\{1,2,5,6\}&:x_1\oplus x_2=1.
\end{aligned}
\]

Each line lies in exactly three planes; each plane contains exactly two lines.

The 320-unit endpoint therefore lives in a small inclusion geometry rather than an arbitrary 256-subset space.

---

## 4. Exact frontier reduction

The eight unconditional repair policies make the empty set and every singleton feasible in every arm. The diagnostic policy adds every subset of its success set \(A\). Therefore

\[
\boxed{\Phi_5(A)=\{S\subseteq\Omega:|S|\le1\}\cup2^A.}
\]

Since the first family has size 9 and intersects \(2^A\) in \(1+|A|\) sets,

\[
\boxed{|\Phi_5(A)|=8+2^{|A|}-|A|.}
\]

Hence the only frontier cardinalities are

\[
\boxed{
|A|=0\Rightarrow9,\quad
|A|=2\Rightarrow10,\quad
|A|=4\Rightarrow20,\quad
|A|=8\Rightarrow256.
}
\]

Let

\[
A_0=A(h^{(0)},h^\star),
\qquad
A_1=A(\hat h_8,h^\star).
\]

Then the primary classes reduce exactly to set relations:

\[
\boxed{
\begin{aligned}
\mathrm{NULL}&\iff A_1=A_0,\\
\mathrm{EXPANSION}&\iff A_0\subsetneq A_1,\\
\mathrm{CONTRACTION}&\iff A_1\subsetneq A_0,\\
\mathrm{TRADEOFF}&\iff A_0\not\subseteq A_1\land A_1\not\subseteq A_0.
\end{aligned}}
\]

All 320 sealed classifications agree with this reduction.

---

## 5. Baseline geometry before feedback

The unresolved scientific universe contains 40 non-identity-permutation true transformations, each under eight cyclic training rotations.

Analytically, the 40 true transformations divide into

\[
\boxed{26\ \mathrm{EMPTY},\quad8\ \mathrm{LINE2},\quad6\ \mathrm{PLANE4}.}
\]

Across eight rotations each, the 320 units therefore start from

\[
\boxed{208\ \mathrm{EMPTY},\quad64\ \mathrm{LINE2},\quad48\ \mathrm{PLANE4}.}
\]

If \(A_0=\varnothing\), the control frontier is already the nine-set minimum created by immediate repair policies, so no nontrivial diagnostic frontier exists to lose. Thus

\[
A_0=\varnothing\Rightarrow\Delta^-=\varnothing.
\]

Corrective loss was structurally possible in only

\[
64+48=\boxed{112}
\]

of the 320 units.

---

## 6. Complete decomposition of 254 / 32 / 18 / 16

The sealed run reduces to the following 14 transition rows.

The count is literal: **4 EMPTY-origin rows + 5 LINE2-origin rows + 5 PLANE4-origin rows = 14**. The two distinct `PLANE4 → PLANE4` tradeoff geometries are separate rows because one has a line intersection and the other is disjoint.

| Control geometry | Treatment geometry | Relation | Class | Units | \(|\Delta^+|\) | \(|\Delta^-|\) |
|---|---|---|---|---:|---:|---:|
| EMPTY | EMPTY | equal | NULL | **32** | 0 | 0 |
| EMPTY | LINE2 | strict gain | EXPANSION | **18** | 1 | 0 |
| EMPTY | PLANE4 | strict gain | EXPANSION | **27** | 11 | 0 |
| EMPTY | FULL8 | strict gain | EXPANSION | **131** | 247 | 0 |
| LINE2 | EMPTY | strict loss | CONTRACTION | **11** | 0 | 1 |
| LINE2 | distinct LINE2 | incomparable | TRADEOFF | **2** | 1 | 1 |
| LINE2 | containing PLANE4 | strict gain | EXPANSION | **7** | 10 | 0 |
| LINE2 | disjoint PLANE4 | incomparable | TRADEOFF | **6** | 11 | 1 |
| LINE2 | FULL8 | strict gain | EXPANSION | **38** | 246 | 0 |
| PLANE4 | EMPTY | strict loss | CONTRACTION | **5** | 0 | 11 |
| PLANE4 | contained LINE2 | strict loss | CONTRACTION | **2** | 0 | 10 |
| PLANE4 | distinct PLANE4, line intersection | incomparable | TRADEOFF | **4** | 10 | 10 |
| PLANE4 | distinct disjoint PLANE4 | incomparable | TRADEOFF | **4** | 11 | 11 |
| PLANE4 | FULL8 | strict gain | EXPANSION | **33** | 236 | 0 |

These rows recover exactly

\[
\boxed{254\ \mathrm{EXPANSION},\ 32\ \mathrm{NULL},\ 18\ \mathrm{CONTRACTION},\ 16\ \mathrm{TRADEOFF}.}
\]

This is the smallest exact structural explanation currently earned for the frozen primary result.

---

## 7. Exact identification versus functional expansion

Treatment ends on the exact true hidden hypothesis in

\[
\boxed{202/320}
\]

units. Exact identification makes the relative map identity, so \(A_1=\Omega\). Every exact-identification unit is therefore an expansion.

The other

\[
254-202=\boxed{52}
\]

expansions occur without exact hidden-transform recovery. They decompose exactly as

\[
\boxed{18\ (\varnothing\to L)+27\ (\varnothing\to P)+7\ (L\to P,\ L\subset P)=52.}
\]

No PLANE4 baseline can expand non-exactly because the only allowed strict superset of a four-state plane is \(\Omega\).

Thus, in A2-V0,

\[
\boxed{\hat h_8\neq h^\star\land A_0\subsetneq A_1}
\]

is possible: correction-relevant fixed-set inclusion is coarser than exact recovery of the hidden generative transformation. This does not establish a general theory of approximate representation.

---

## 8. Where the 34 loss-bearing units come from

All corrective loss occurs among the 112 units with nonempty baseline success sets.

| Baseline | Units | Expansion | Contraction | Tradeoff | Loss-bearing |
|---|---:|---:|---:|---:|---:|
| LINE2 | 64 | 45 | 11 | 8 | **19** |
| PLANE4 | 48 | 33 | 7 | 8 | **15** |
| **Total** | **112** | **78** | **18** | **16** | **34** |

So the finite conditional census is

\[
\boxed{34/112}
\]

among units that had something nontrivial to lose. This is not a population probability.

The 18 contractions are

\[
11(L\to\varnothing)+5(P\to\varnothing)+2(P\to L,\ L\subset P).
\]

The 16 tradeoffs are

\[
2(L\to L')+6(L\to P,\ L\cap P=\varnothing)+8(P\to P').
\]

---

## 9. Frontier cardinality is not an adequate substitute

All 16 tradeoffs demonstrate information that frontier cardinality alone loses.

- **10** tradeoffs preserve cardinality: 2 LINE2→distinct LINE2 and 8 PLANE4→distinct PLANE4.
- **6** tradeoffs increase cardinality from 10 to 20: LINE2→disjoint PLANE4, while losing the old line-specific jointly correctable set.

Therefore A2-V0 establishes both

\[
\boxed{|\Phi_1|=|\Phi_0|\not\Rightarrow\Phi_1=\Phi_0}
\]

and

\[
\boxed{|\Phi_1|>|\Phi_0|\not\Rightarrow\Phi_0\subseteq\Phi_1.}
\]

A scalar frontier size would call the six 10→20 tradeoffs positive while suppressing \(\Delta^-\neq\varnothing\). The set-valued topology is doing real scientific work.

---

## 10. Exact learner-dynamics constraints

The true hypothesis remains in the treatment version set, the active hypothesis is the minimum live index, and the live set only shrinks. Therefore

\[
\boxed{0=\hat h_0\le\hat h_1\le\cdots\le h^\star.}
\]

At a correct episode the active hypothesis survives and stays active. At an incorrect episode it is eliminated and the minimum live index strictly increases. Hence

\[
\boxed{\#\text{incorrect treatment predictions}=\#\text{active-hypothesis changes}.}
\]

Let \(C_u\) be the set of training states on which treatment predicted correctly. Correct feedback forces every later survivor to remain correct on those states, so

\[
\boxed{C_u\subseteq A_1.}
\]

Every nonexact relative transform has at most four fixed states, therefore

\[
\boxed{|C_u|\ge5\Rightarrow\hat h_8=h^\star.}
\]

The sealed trajectories satisfy these implications exactly.

### 10.1 Version-space refinement is not corrective-frontier monotonicity

In all 320 unresolved units, informative treatment feedback truth-preservingly refines the learner's candidate set: the true hypothesis remains live while the final treatment version space is a strict subset of the initial 48-hypothesis set. Yet the treatment frontier can be a strict superset of, equal to, a strict subset of, or incomparable with the control frontier.

Thus A2-V0 contains the exact finite separation

\[
\boxed{
L^{+F}_8\subsetneq L_0
\;\not\Rightarrow\;
\Phi_5(G^{+F})\supseteq\Phi_5(G^{-F}).
}
\]

The safer interpretation is **version-space refinement**, not a general scalar notion of "progress in identification." In this assay,

\[
\boxed{
\text{epistemic narrowing of candidate transformations}
\neq
\text{monotone improvement of executable correction}.
}
\]

The distinction is possible because the version space records which transformations remain admissible, whereas the evaluation constructor exposes only the current minimum surviving hypothesis as the active decoder. Removing false hypotheses can therefore change the selected realizable policy without requiring preservation of the previous policy's success set.

### 10.2 Correctness evidence is interaction-generated

The eight rotations expose exactly the same eight latent states once each, but they need not expose the same sequence of correctness evidence. At training episode \(t\),

\[
x_t,\hat h_t
\rightarrow
\hat x_t
\rightarrow
s_t=\mathbf 1[\hat x_t=x_t]
\rightarrow
L_{t+1},
\]

and \(\hat h_t\) already depends on earlier feedback. Therefore

\[
\boxed{
\text{same state corpus in a different order}
\rightarrow
\text{different active hypothesis at encounter}
\rightarrow
\text{different attempted repair}
\rightarrow
\text{different correctness evidence}
\rightarrow
\text{different later learner state}.
}
\]

This is compatible with the frozen causal contract: the exogenous world and state corpus are matched, while treatment-induced post-assignment interaction trajectories are allowed to diverge.

The inclusion \(C_u\subseteq A_1\) sharpens the asymmetry. Correct feedback on a training state imposes a constraint that every later survivor must preserve correctness on that state. Incorrect feedback instead eliminates hypotheses that would make the same attempted repair on that observation; it does not impose preservation of the old active decoder's successes elsewhere.

The resulting A2-V0-local mechanism statement is therefore

\[
\boxed{
\text{truth-preserving version-space elimination}
+
\text{single active-hypothesis selection}
+
\text{interaction-generated evidence}
\not\Rightarrow
\text{preservation of the prior diagnostic success set}.
}
\]

This localizes how informative adaptation can redistribute correction capacity in A2-V0. It does not establish a general mechanism law outside the assay.

---

## 11. Positive and negative feedback are asymmetric in the frozen learner

For any observation vector and target repair, exactly one mask for each of the six permutations decodes to that target. From the initial 48 hypotheses, exactly six predict any particular repair.

Thus on the first episode:

\[
\boxed{48\to6\quad\text{if the active prediction is correct},}
\]

while

\[
\boxed{48\to42\quad\text{if it is incorrect}.}
\]

The sealed run contains exactly 40 first-episode-correct units and 280 first-episode-incorrect units.

All 40 first-correct units end with

\[
\boxed{\hat h_8=h^\star,\quad|L_8|=1,\quad\mathrm{EXPANSION}.}
\]

This is an exact A2-V0 census property, not a universal law of feedback.

---

## 12. Zero-correct-prediction regime

There are

\[
\boxed{72}
\]

units in which treatment is wrong on all eight training episodes. Their outcomes are

\[
\boxed{22\ \mathrm{EXPANSION},\quad32\ \mathrm{NULL},\quad18\ \mathrm{CONTRACTION},\quad0\ \mathrm{TRADEOFF}.}
\]

Six of those 72 reach the exact true hypothesis only after the eighth failure. Therefore, in this assay,

\[
\boxed{\text{an observed correct training prediction is not necessary for frontier expansion or exact final identification}.}
\]

Negative correctness feedback alone can move the final frontier upward, downward, or leave it unchanged because it still eliminates incompatible prediction classes. This does not imply that failure itself is beneficial.

All 18 contractions and all 32 nulls occur in this zero-correct regime.

---

## 13. Tradeoffs follow sparse correctness outside the baseline set

The 16 tradeoff units have either one or two correct treatment predictions:

\[
4\text{ units with }|C|=1,
\qquad
12\text{ units with }|C|=2.
\]

For every tradeoff unit,

\[
\boxed{C_u\subseteq A_1\setminus A_0.}
\]

Every training state on which treatment is actually correct lies outside the baseline diagnostic success set. The final policy gains correctness outside the old fixed set while failing to preserve all of the old set.

This is descriptive of the sealed finite trajectories; it does not identify a general mediator for loss.

---

## 14. Learned-state change is not frontier change

In all 320 unresolved units, informative feedback changes the learned state relative to control: treatment finishes with active hypothesis greater than zero and a reduced version set, while control remains at active 0 with all 48 hypotheses live.

Yet 32 units are frontier nulls:

\[
\boxed{A_0=A_1=\varnothing,\qquad\Phi_0=\Phi_1.}
\]

Therefore A2-V0 contains a direct finite witness that

\[
\boxed{\text{feedback-induced learned-state change}\not\Rightarrow\text{corrective-frontier change}.}
\]

The nulls are fixed-point-free→fixed-point-free transitions: internal state changes while both diagnostic policies remain wrong on every latent state and induce the same minimal frontier.

---

## 15. Training order is a major path variable

For each hidden transformation, the eight rotations visit the same eight latent states exactly once. They differ only in cyclic order.

Across the 40 unresolved hidden transformations,

\[
\boxed{35/40}
\]

produce more than one frontier class across their eight rotations.

The exact true-world partition is

\[
\boxed{
40
=
5\ \text{order-invariant all-expansion worlds}
+
22\ \text{expansion/null order-sensitive worlds}
+
13\ \text{expansion/loss order-sensitive worlds}.
}
\]

Among the 26 baseline-EMPTY worlds, 22 have both expansion and null rotations; four expand under every rotation.

Among the 14 baseline-nonempty worlds, 13 have at least one loss-bearing rotation and at least one expansion rotation; only one expands under every rotation. Therefore

\[
\boxed{13/14}
\]

of hidden worlds with something nontrivial to lose are loss-capable under some cyclic order in the frozen learner.

These are finite census facts, not external probabilities.

---

## 16. Concrete order witness: h^(22)

A clean witness is

\[
h^{(22)}=(\sigma=(1,0,2),\ b=(1,1,0)).
\]

Its baseline success set is

\[
A_0=\{2,3,4,5\}.
\]

The eight rotations yield:

| Rotation | Class | Final active | \(A_1\) |
|---:|---|---:|---|
| 0 | TRADEOFF | 6 | \(\{0,1,6,7\}\) |
| 1 | TRADEOFF | 6 | \(\{0,1,6,7\}\) |
| 2 | EXPANSION | 22 | \(\Omega\) |
| 3 | EXPANSION | 22 | \(\Omega\) |
| 4 | EXPANSION | 22 | \(\Omega\) |
| 5 | EXPANSION | 22 | \(\Omega\) |
| 6 | CONTRACTION | 18 | \(\varnothing\) |
| 7 | CONTRACTION | 10 | \(\varnothing\) |

Thus one fixed hidden world, primitive interface, eight-state corpus, and feedback rule yield expansion, contraction, and tradeoff solely through cyclic ordering.

This is the clearest finite witness that the observed non-monotonicity is path-dependent rather than attributable only to heterogeneity across hidden worlds.

---

## 17. Frozen hypothesis ordering breaks transformation symmetry

The signed-permutation environment has abstract group symmetries, but the learner chooses the minimum surviving hypothesis under a fixed lexicographic enumeration. That search rule is not invariant under group relabeling.

For the two 3-cycle permutation blocks, restricting to baseline-nonempty line worlds:

| True permutation block | Units | Expansion | Contraction | Tradeoff |
|---|---:|---:|---:|---:|
| \((1,2,0)\) | 32 | 21 | **11** | 0 |
| \((2,0,1)\) | 32 | 24 | 0 | **8** |

The blocks have the same permutation cycle type and fixed-set-size possibilities but different loss topology under the frozen learner. The transposition blocks likewise do not have identical class distributions.

Therefore the observed 254/32/18/16 frequencies are not intrinsic frequencies of the signed-permutation group. They arise from

\[
\boxed{\text{group geometry}+\text{lexicographic elimination}+\text{training order}.}
\]

This is a claim-ceiling constraint, not a defect repair.

---

## 18. What this analysis earns

### Earned in A2-V0

1. The four primary classes reduce exactly to inclusion relations between \(A_0\) and \(A_1\).
2. Only 12 diagnostic success-set geometries are possible.
3. The entire 254/32/18/16 result is decomposed by the 14 transition rows in Section 6.
4. The 52 non-exact expansions are exactly proper upward fixed-set moves stopping below \(\Omega\).
5. All 34 corrective losses occur where a nontrivial baseline diagnostic frontier exists to be lost.
6. Frontier cardinality fails to preserve tradeoff topology in all 16 tradeoff units.
7. Feedback changes learned state in all 320 units but the measured frontier in only 288.
8. Zero correct training predictions are compatible with expansion, null, contraction, and exact final identification.
9. Outcome class is strongly order-dependent under the frozen lexicographic learner.
10. Truth-preserving version-space refinement does not impose a monotone ordering on the corrective frontier.
11. Under the frozen learner, encounter order changes the correctness evidence because feedback evaluates predictions generated by the evolving treatment state.

### Not earned

This analysis does **not** establish:

- a general law that feedback is non-monotone in arbitrary adaptive systems;
- a general theory of approximate representation;
- a universal significance for the 34/112 conditional loss census;
- a unique causal mediator among \(g,Q,\Pi,G_{\mathrm{learned}}\);
- an ordering-invariant property of the signed-permutation environment;
- general future-viability independence;
- MATRIX₁.

The analysis localizes A2-V0. It does not promote it.

---

## 19. Current structural account

The useful causal/structural chain is now

\[
\boxed{
(h^\star,k)
\rightarrow
\text{ordered feedback trajectory}
\rightarrow
\hat h_8
\rightarrow
T_{\hat h_8}^{-1}T_{h^\star}
\rightarrow
\operatorname{Fix}(\cdot)
\rightarrow
(A_0,A_1)
\rightarrow
(\Phi_0,\Phi_1,\Delta^+,\Delta^-).
}
\]

The non-monotonic result is therefore localized to an interaction among:

1. the small fixed-set geometry of the signed-permutation environment;
2. the lexicographic version-space elimination rule;
3. the order in which the same eight training states are encountered and, through the evolving active hypothesis, the correctness evidence thereby generated.

The next legitimate scientific question, if pursued, is whether the loss/tradeoff structure survives controlled changes to **learner ordering/search policy** or **training-order convention** while keeping endpoint semantics fixed. That would be a new assay with a new preregistration.

No such follow-up is executed or authorized by this analysis.