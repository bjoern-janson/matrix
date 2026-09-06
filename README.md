# MATRIX

**Status:** `MATRIX_0` kernel frozen; Attack 1 closed / assumption-scoped; A2-V0 complete; A2-V1 complete / scientific interpretation admitted; `MATRIX_1` not earned.

## Current program state

The conceptual kernel below remains frozen. The repository has since completed its first formal attack and two finite causal assays without earning a kernel promotion:

| Stage | Current standing |
|---|---|
| `MATRIX_0` conceptual kernel | **FROZEN** |
| Attack 1 / `EXEC_V1` | **CLOSED / ASSUMPTION-SCOPED** |
| A2-V0 | **COMPLETE**; post-execution structural analysis archived |
| A2-V1 | **COMPLETE / SCIENTIFIC INTERPRETATION ADMITTED** |
| `MATRIX_1` | **NOT EARNED** |

Current navigation: [`formalization/EXEC_V1.md`](formalization/EXEC_V1.md), [`experiments/a2_v0/README.md`](experiments/a2_v0/README.md), [`experiments/a2_v1/README.md`](experiments/a2_v1/README.md), [`experiments/a2_v1/CURRENT_STATE.md`](experiments/a2_v1/CURRENT_STATE.md), and [`experiments/A2_V1_RESULT.md`](experiments/A2_V1_RESULT.md).

This status block is navigational. It does not amend the frozen kernel, retroactively rewrite preregistrations, or promote post-execution findings into stronger claims.

MATRIX studies a narrow question:

> **Can feedback causally improve an adaptive system's future ability to discover, diagnose, and correct unfamiliar errors without silently destroying protected corrective capacity?**

The project is not currently trying to add another general theory of intelligence. Its job is to formalize a small kernel, translate only what genuinely maps from earlier work, attack the kernel mathematically and empirically, and revise it only when a concrete failure forces revision.

```text
formalize -> translate -> test -> revise only if forced
```

Research discipline:

```text
derive what follows | translate only what maps | test what remains
```

and:

```text
No new concept without a concrete missing argument.
```

The methodological priority is:

```text
surviving falsification > accumulating conceptual elegance
```

---

## 1. Frozen conceptual kernel

### 1.1 Representation

Let

```math
g_t : \Omega_t \to M_t
```

be a representation or encoder over a declared state space `\Omega_t`.

For retained message `m`, the induced uncertainty cell is

```math
S_m^{(t)} = g_t^{-1}(m).
```

The representation determines which underlying states are currently conflated. It does **not** by itself determine whether that ambiguity is safe.

---

### 1.2 Primitive affordances, diagnostics, and policy machinery

Keep the following causal objects distinct:

```text
\mathcal U_t = primitive executable observation/intervention affordances
Q_t          = diagnostic procedures constructible from \mathcal U_t
\Pi_t        = policy-generation / policy-selection machinery
\mathcal T_t = declared task family
R_t          = valid-repair relation
c_t          = grounded cost model
B_t          = corrective resource budget
```

An observed change in correction does not identify which of these changed. Mechanism attribution must be earned separately.

In particular, a treatment arm is not credited with adaptive diagnostic improvement merely because it was handed a stronger primitive interface.

---

### 1.3 Corrective frontier

For a fixed system state `G` and budget `B`, define the jointly correctable frontier

```math
\Phi_B(G)
=
\left\{
S\subseteq\Omega:
\exists\pi,
\mathrm{cost}(\pi)\le B,
\ \forall x\in S,
\ \pi\text{ diagnoses and validly repairs }x
\right\}.
```

The quantifier order is essential. The object is not merely

```math
\forall x\ne y\;\exists q_{xy},
```

but whether **one executable policy**, starting from uncertainty over the whole set `S`, can choose its own diagnostics and achieve valid repair within budget.

`\Phi_B(G)` is downward closed in the finite setting: if `S` is jointly correctable, every subset of `S` is also jointly correctable.

Its minimal excluded sets therefore form a minimal-obstruction hypergraph

```math
H_B(G)=\mathrm{Min}\left(2^\Omega\setminus\Phi_B(G)\right).
```

These are the smallest uncertainty configurations for which bounded correction fails.

---

### 1.4 Representation safety

A representation is corrigibly adequate at budget `B` exactly when every ambiguity cell it induces lies inside the corrective frontier:

```math
\boxed{
\mathrm{Safe}_B(g\mid G)
\iff
\forall m\in\mathrm{im}(g),
\quad
g^{-1}(m)\in\Phi_B(G)
}
```

This separates three objects:

```text
representation != uncertainty induced by representation != ability to correct that uncertainty
```

A useful compression of the result is:

```text
g determines the ambiguity.
\Phi_B determines whether the ambiguity is recoverable.
```

Representation safety is therefore relational, not intrinsic.

A coarser representation can remain safe when lost distinctions are affordably recoverable later. A fixed representation can become unsafe if diagnostic or repair access is lost.

---

### 1.5 Graded performance remains separate from zero-error feasibility

Do not collapse safe correction into one average success number.

For uncertainty set `S`, define graded bounded performance separately:

```math
P_B^*(S\mid G)
=
\sup_{\pi:\mathrm{cost}(\pi)\le B}
P(\text{successful correction}\mid S,\pi,G).
```

A useful corrective profile may include

```math
C_B(S\mid G)
=
\left(
\mathbf 1[S\in\Phi_B(G)],
P_B^*(S\mid G),
\mathrm{cost}^*(S\mid G)
\right).
```

A system with `99%` average success can still fail the zero-error safety condition on a protected uncertainty cell.

---

## 2. Feedback-dependent improvement

The original program-level improvement object remains counterfactual:

```math
\boxed{
C_{\mathrm{improve}}^{(h)}(G_t,F)
=
\mathbb E\!\left[
V(G_{t+h}^{+F})-V(G_{t+h}^{-F})
\mid G_t
\right]
}
```

and the working research relation remains

```math
I_t\propto C_{\mathrm{improve}}^{(h)}.
```

This asks whether feedback caused greater future viability than the matched no-feedback counterfactual.

It does **not** by itself establish preserved corrective capacity.

```math
\boxed{
C_{\mathrm{improve}}>0
\not\Rightarrow
\text{preserved corrective capacity}
}
```

Viability improvement and corrective-frontier change are separate observables.

---

## 3. Corrective-frontier change

Under a declared common jurisdiction, compare feedback and matched counterfactual frontiers:

```math
\Delta_B^+
=
\Phi_B(G^{+F})\setminus\Phi_B(G^{-F})
```

```math
\Delta_B^-
=
\Phi_B(G^{-F})\setminus\Phi_B(G^{+F}).
```

Interpretation:

```text
\Delta_B^+ = newly jointly correctable uncertainty sets
\Delta_B^- = previously jointly correctable uncertainty sets that were lost
```

Keep the sets themselves primary. Cardinalities or ratios are derived summaries and can hide incomparable changes.

Define corrective dominance over a protected budget range `\mathcal B_*` by

```math
G_1\succeq_{\mathrm{corr}}G_0
\iff
\forall B\in\mathcal B_*:
\Phi_B(G_0)\subseteq\Phi_B(G_1).
```

Strict inclusion for at least one protected budget gives strict corrective improvement under this ordering.

---

## 4. Strong safe-improvement witness

The current strongest target is:

```math
\boxed{
C_{\mathrm{improve}}^{(h)}>0
\ \land\ 
\Delta_B^+\ne\varnothing
\ \land\ 
\Delta_B^-=\varnothing
\ \land\ 
\text{a fresh subsequent corrective challenge succeeds}
}
```

The four components are:

```text
gain         : future viability improves because of feedback
preservation : protected corrective capacity is not silently lost
expansion    : at least one new uncertainty set becomes jointly correctable
continuation : corrective capacity remains usable after it is exercised
```

The continuation clause prevents a one-use correction mechanism from masquerading as persistent corrigibility.

This is a strong witness, not a universal normative law. In settings where corrective tradeoffs are permitted, losses must be represented explicitly rather than absorbed into a scalar objective.

---

## 5. Matched jurisdiction and resource discipline

Direct frontier comparison requires a common typed domain. Unless one variable is explicitly the intervention, freeze or explicitly transport:

```math
\Omega^+=\Omega^-,
\qquad
\mathcal T^+=\mathcal T^-,
\qquad
R^+=R^-,
```

```math
\mathcal U^+=\mathcal U^-,
\qquad
B^+=B^-,
\qquad
c^+=c^-.
```

For the strongest adaptive diagnostic experiment, hold primitive affordances fixed:

```math
\boxed{\mathcal U^{+F}=\mathcal U^{-F}}
```

while allowing feedback to causally alter objects such as

```math
g_t,\quad Q_t,\quad \Pi_t.
```

The causal hypothesis is then of the form

```text
same primitive affordances
        ->
different feedback
        ->
changed representation / diagnostic repertoire / policy machinery
        ->
changed jointly correctable frontier
        ->
better externally relevant future outcome
        ->
correction remains possible again afterward
```

No component receives credit for a transition it did not implement and experimentally identify.

---

## 6. The first finite witness: diagnostic memory

The immediate mathematical motivation is a finite separation:

> Two systems can preserve the same minimum diagnostic cost for every supplied pair of possible faults while having exponentially different ability to diagnose an unknown fault under a bounded adaptive policy.

In the concrete binary family, every distinct pair can be separated in one singleton test, so the complete pairwise minimum-cost matrix is identical across systems. Yet with `2^d` possible states and no retained state-specific bits:

```math
B_{\mathrm{singleton}}^*=2^d-1,
\qquad
B_{\mathrm{structured}}^*=d.
```

The underlying quantifier failure is

```math
\forall\{x,y\}\;\exists\text{ cheap distinguishing test}
```

not implying

```math
\exists\text{ cheap adaptive policy}\;\forall x\in S\;\text{correct repair}.
```

This motivates `\Phi_B`: pairwise accessibility alone does not determine bounded joint corrective capacity.

For a finite downward-closed feasible family, taking inclusion-minimal jointly unrepairable sets as hyperedges `H_B` gives the exact memory characterization

```math
M_B^*=\chi(H_B),
\qquad
m_B^*=\left\lceil\log_2\chi(H_B)\right\rceil,
```

using weak hypergraph coloring.

A coarsest safe representation need not exist when the decoder can perform future experiments: several incomparable compressions may each preserve affordable recovery while their common coarsening destroys it.

### Claim ceiling

This finite witness establishes a mathematical separation and a measurement target. It does **not** establish that feedback invents diagnostics, that an adaptive agent improves its diagnostic generator, recursive self-improvement, general corrigibility, or field-level novelty. Active learning, generalized binary search, action-dependent side information, and zero-error coordination contain substantial prior art.

The next scientific question is whether feedback can *cause* the kind of diagnostic-policy improvement that the finite construction simply supplies by assumption.

---

## 7. Safe forgetting

A useful interpretation is:

```math
\boxed{
\text{safe forgetting}
=
\text{moving dependence from retained state into affordable future interaction}
}
```

provided the induced ambiguity remains jointly correctable:

```math
g^{-1}(m)\in\Phi_B(G).
```

Therefore:

```text
forgotten != foreclosed
stored    != correctable
```

The relevant resource is not memory alone. Future correctability depends jointly on retained state, primitive affordances, constructible diagnostics, policy machinery, repair machinery, task family, cost model, and budget.

---

## 8. Translation discipline

MATRIX is not authorized to silently rewrite earlier repositories into this vocabulary.

Cross-program consolidation uses an explicit typed correspondence ledger:

```text
source object
target kernel object
status
conditions
preserved distinctions
lost distinctions
unresolved mismatch
evidence / witness
```

Allowed statuses:

```text
IDENTICAL
REFINEMENT
PROJECTION
ANALOGY
NO TRANSLATION EARNED
```

`NO TRANSLATION EARNED` is a result, not a blank waiting to be filled.

A failed translation is evidence about the architecture. It is not pressure to invent a more permissive abstraction.

Initial translation targets include earlier work on Future Sufficiency, Signature-Relative Equivalence, Corrigible Compression, OpenCore, White Rabbit, Reach, and CRANK. Apparent structural similarity is not identity; any such mapping must be earned locally.

---

## 9. Research program

The immediate sequence is fixed:

```text
1. FORMALIZE
   - definitions, domains, quantifiers
   - prove structural consequences
   - identify exact comparison preconditions
   - preserve claim ceilings

2. TRANSLATE
   - map earlier local objects into the kernel only where warranted
   - record partial mappings and failed mappings explicitly
   - do not let repositories redefine the kernel by analogy

3. TEST
   - freeze a causal assay
   - hold primitive affordances and relevant resources fixed
   - measure viability and corrective-frontier changes separately
   - include a fresh subsequent corrective challenge

4. REVISE ONLY IF FORCED
   - mathematics exposes a contradiction
   - translation exposes a genuine missing type
   - experiment reveals an unrepresented failure mode
```

The project should now be attacked rather than ornamented.

A positive result is not the only informative result. For example,

```math
C_{\mathrm{improve}}>0,
\qquad
\Delta_B^-\ne\varnothing
```

would show that feedback can improve expected future viability while consuming previously available corrective capacity. That would be a substantive result requiring characterization, not a failed experiment.

---

## 10. Current pressure points

Two statements carry most of the present load:

```math
\boxed{
g\text{ determines the ambiguity; }\Phi_B\text{ determines its recoverability}
}
```

and

```math
\boxed{
C_{\mathrm{improve}}>0
\not\Rightarrow
\text{preserved corrective capacity}
}
```

Everything added from here should formally derive from the kernel, map into it through an earned translation, empirically challenge it, or expose a concrete missing argument.

The current decisive question is:

```math
\boxed{
\text{Can feedback, under unchanged primitive resources, causally improve the machinery that discovers and repairs unfamiliar errors, enlarge the jointly correctable frontier without protected foreclosure, and leave that capacity usable afterward?}
}
```

Start throwing rocks at it.
