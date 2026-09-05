# A2-PREREG-V0 — Paired feedback → corrective-frontier assay

**Program:** MATRIX₀  
**Attack:** 2 — causal identification  
**Status:** FROZEN / EXECUTED WITHOUT POST-HOC ENDPOINT REVISION  
**Scientific role:** finite causal assay for treatment sensitivity of the system-realizable corrective frontier  
**Conceptual kernel revision:** NONE  
**README revision:** NONE

This document records the preregistered A2-V0 assay after its pre-execution mathematical audit. It distinguishes the scientific contract frozen before unresolved-unit execution from one operational accounting completion made during implementation and frozen before the scientific run.

The governing methodological rule is:

\[
\boxed{\text{analytically determined}\neq\text{empirically unresolved}.}
\]

The assay therefore does not treat theorem-derived outcomes as discoveries.

---

## 1. Claim ceiling

A2-V0 asks:

\[
\boxed{
\text{Under matched exogenous conditions and fixed primitive affordances, does feedback cause a counterfactually attributable change in }\Phi_B?
}
\]

The primary causal object is unit-indexed:

\[
\Phi_{B,u}(a)=\Phi_B(G_u(a)),\qquad a\in\{0,1\},
\]

with paired frontier changes

\[
\Delta^+_{B,u}=\Phi_{B,u}(1)\setminus\Phi_{B,u}(0),
\]

\[
\Delta^-_{B,u}=\Phi_{B,u}(0)\setminus\Phi_{B,u}(1).
\]

The primary computational object is the exact mapping

\[
\boxed{
u\mapsto
\left(
\Phi_{B,u}(0),
\Phi_{B,u}(1),
\Delta^+_{B,u},
\Delta^-_{B,u}
\right),}
\]

where the declared unit universe has 384 elements.

A2-V0 does **not** test general intelligence, open-ended self-improvement, general corrigibility, unfamiliar-error discovery, population-level generalization, or universal monotonicity of feedback effects.

---

## 2. Identification contract

Attack 2 freezes the distinction

\[
\boxed{\text{matched exogenous process}\neq\text{matched realized post-treatment trajectory}.}
\]

The four-way experimental partition is:

\[
\boxed{
\begin{array}{ll}
\text{exogenous difference} &\rightarrow \text{control},\\
\text{ordinary stochastic variation} &\rightarrow \text{estimate / pair},\\
\text{treatment-induced difference} &\rightarrow \text{allow},\\
\text{analyst-added post-assignment difference} &\rightarrow \text{prohibit}.
\end{array}}
\]

A unit is defined under an isolated treatment replica:

\[
\boxed{G_u(a)\text{ has no cross-arm or cross-unit learned-state contamination}.}
\]

Within-arm post-treatment divergence is permitted; cross-arm learned-state leakage is not. If shared learning were scientifically intentional, the experimental unit would have to be enlarged rather than pretending unit-level isolation held.

The assay separately distinguishes:

\[
F\rightsquigarrow\Phi_B
\]

as the frontier effect,

\[
F\rightarrow(g,Q,\Pi,G_{\mathrm{learned}})\rightarrow\mathfrak{Real}\rightarrow\operatorname{Avail}\rightarrow\Phi_B
\]

as a mechanism hypothesis, and

\[
F\rightsquigarrow C_{\mathrm{improve}}
\]

as a separate performance/viability question. No endpoint authorizes inference about another merely because it moved.

---

## 3. Finite world

Let

\[
\Omega=\{0,1\}^3,
\qquad |\Omega|=8.
\]

States are represented as integers `0..7` corresponding to `000..111` in lexicographic order.

The primitive interface is frozen as

\[
\mathcal U=\{q_0,q_1,q_2\}\cup\{r_x:x\in\Omega\}.
\]

Each `q_j` returns one binary observation. Repair `r_z` succeeds iff the hidden state is exactly `z`:

\[
R(x,r_z)=1\iff x=z.
\]

The environment response is deterministic in V0.

---

## 4. Hidden environment law and hypothesis class

Each environment is indexed by

\[
h=(\sigma,b),
\qquad \sigma\in S_3,
\qquad b\in\{0,1\}^3.
\]

Query `q_j` returns

\[
y_j=x_{\sigma(j)}\oplus b_j.
\]

There are exactly

\[
3!\,2^3=48
\]

hypotheses.

They are ordered lexicographically as the six permutations of `(0,1,2)`, each followed by masks `000..111`.

Given candidate hypothesis `h`, decoder `d_h` inverts that candidate transformation.

The true `h^\star` is never supplied to the learner or policy constructor.

---

## 5. Experimental units

A unit is

\[
\boxed{u=(h^\star,k)},
\]

where `k∈{0,…,7}` determines a cyclic rotation of the eight training states.

Thus

\[
\boxed{\mathcal U_{\mathrm{unit}}=\mathcal H\times\{0,\ldots,7\}},
\qquad
|\mathcal U_{\mathrm{unit}}|=48\times8=384.
\]

Every unit has two exact pre-treatment clones:

\[
G_u(1),\qquad G_u(0).
\]

The assay fully enumerates this finite unit universe. It makes no sampling or population-extrapolation claim.

---

## 6. Initial learner state

The learner maintains a surviving hypothesis set

\[
L_t\subseteq\mathcal H,
\qquad
L_0=\mathcal H.
\]

The active hypothesis is always the minimum surviving hypothesis in the frozen ordering:

\[
\hat h_t=\min L_t.
\]

Treatment and control begin from the same `L_0`, active hypothesis, code, primitive interface, task information, cost contract, latent-state schedule, and true environment law.

---

## 7. Training episode

Training lasts exactly eight episodes, visiting the rotated sequence

\[
x_k,x_{k+1},\ldots,x_{k+7}
\]

modulo 8.

Each episode executes exactly:

1. `q_0`,
2. `q_1`,
3. `q_2`,
4. decode with the current active hypothesis,
5. attempt the predicted repair.

Let the attempted repair be `\hat x` and define actual correctness

\[
s_t=\mathbf 1[\hat x=x].
\]

There is no adaptive extension beyond eight episodes if learning remains incomplete.

---

## 8. Sole treatment

Treatment receives informative feedback:

\[
F=1:\quad (\mathrm{valid}=1,s_t).
\]

Control receives a matched noninformative token:

\[
F=0:\quad (\mathrm{valid}=0,0).
\]

Both arms execute the same complete 48-hypothesis processing pass. The control pass does not update `L_t`.

No hidden state `x`, true hypothesis `h^\star`, or analyst-selected uncertainty set `S` crosses the feedback interface.

---

## 9. Learning update

With valid treatment feedback, retain exactly previously surviving hypotheses whose candidate prediction agrees with whether the attempted repair was correct:

\[
\boxed{
L_{t+1}
=
\left\{h\in L_t:
\mathbf1[d_h(y)=\hat x]=s_t
\right\}.
}
\]

Then set

\[
\hat h_{t+1}=\min L_{t+1}.
\]

The true hypothesis must survive every valid update.

For control,

\[
L_{t+1}=L_t.
\]

---

## 10. Post-training freeze and constructor-visible state

After episode 8, learning is disabled in both arms. Evaluation supplies no feedback and admits no online improvement.

The constructor-visible state is exactly

\[
\boxed{i_\Pi(G)=(\texttt{SWITCHBOARD\_3},\hat h_8).}
\]

It contains neither the full version set, true hypothesis, latent state, nor tested uncertainty set.

The full learned state may be logged for audit, but it is not supplied to policy realization.

---

## 11. System-realizable policies

Evaluation admits exactly nine policy forms:

- eight immediate-repair policies `\pi_z^{\mathrm{imm}}`, one for each `z∈Ω`;
- one diagnostic policy generated from the current constructor-visible active hypothesis.

Therefore

\[
\boxed{
\operatorname{Avail}(G)
=
\{\pi_z^{\mathrm{imm}}:z\in\Omega\}
\cup
\{\pi_{\hat h_8}\}.
}
\]

No analyst-known alternative decoder is available unless the system actually realizes it through the declared constructor state.

This instantiates the Attack-1 boundary:

\[
\boxed{\text{describable by analyst}\neq\text{realizable by system}.}
\]

---

## 12. Evaluation costs and budget

Primitive query and repair actions each cost one unit:

\[
c(q_j)=1,
\qquad
c(r_z)=1.
\]

Every evaluation policy realization costs one unit:

\[
C_{\mathrm{real}}=1.
\]

Thus an immediate policy costs 2 total and the three-query diagnostic policy costs 5 total.

Freeze

\[
\boxed{B=5.}
\]

No evaluation policy receives free synthesis.

---

## 13. Exact frontier measurement

For every unit and arm, enumerate all 256 subsets of `Ω` and all nine realized policies.

Define

\[
\boxed{
\Phi_{B,u}(a)
=
\left\{
S\subseteq\Omega:
\exists\pi\in\operatorname{Avail}(G_u(a))
\;\forall x\in S,
\;\pi\text{ succeeds within }B
\right\}.
}
\]

Then retain the complete set-valued endpoint:

\[
\Delta^+_{B,u}
=
\Phi_{B,u}(1)\setminus\Phi_{B,u}(0),
\]

\[
\Delta^-_{B,u}
=
\Phi_{B,u}(0)\setminus\Phi_{B,u}(1).
\]

JSON subset values use integer bitmasks solely as an exact encoding of sets. They are not scalar frontier scores.

Each unit is classified descriptively as:

- `NULL`: `Δ+=∅`, `Δ-=∅`;
- `EXPANSION`: `Δ+≠∅`, `Δ-=∅`;
- `TRADEOFF`: `Δ+≠∅`, `Δ-≠∅`;
- `CONTRACTION`: `Δ+=∅`, `Δ-≠∅`.

All four are admissible outcomes wherever not ruled out analytically.

---

## 14. Theorem-derived control family

Pre-execution analysis showed that the first eight hypotheses share the same permutation and enumerate all eight masks:

\[
h^{(j)}=(\sigma_{\min},b^{(j)}),
\qquad j=0,\ldots,7.
\]

For a fixed observation, these eight decoders predict eight different states. If truth is `h^(j)`, every earlier mask is wrong on every state. Each failure removes the current minimum wrong mask, while the true mask survives. After exactly `j` failures, the active hypothesis becomes the truth and remains there. Since `j≤7`, the eight-episode schedule is sufficient for every rotation.

### 14.1 Expansion controls

For `j=1..7` and all eight rotations:

\[
A_+=\Omega,
\qquad
A_-=\varnothing,
\]

so

\[
\boxed{\Phi^+=2^\Omega,}
\qquad
\boxed{\Phi^-=\{S\subseteq\Omega:|S|\le1\}.}
\]

Therefore

\[
\boxed{
\Delta^+=\{S\subseteq\Omega:|S|\ge2\},
\qquad
\Delta^-=\varnothing.
}
\]

The exact cardinalities are

\[
|\Phi^+|=256,
\qquad
|\Phi^-|=9,
\qquad
|\Delta^+|=247.
\]

There are

\[
\boxed{7\times8=56}
\]

such theorem-derived expansion controls.

### 14.2 Null controls

For `j=0` and all eight rotations, the initial active hypothesis is already true:

\[
\boxed{
\Phi^+=\Phi^-=2^\Omega,
\qquad
\Delta^+=\Delta^-=\varnothing.
}
\]

There are

\[
\boxed{8}
\]

such theorem-derived null controls.

### 14.3 Unresolved set

The remaining

\[
\boxed{384-64=320}
\]

units were unresolved by the pre-execution analysis.

There is **no residual all-null hypothesis**. The scientific run is tasked with determining their exact unit-level frontier map, not rejecting an already-undermined existence null.

---

## 15. Secondary weighted deployment-performance endpoint

For state `x_i`, define the fixed weight

\[
p_i=\frac{2^i}{255}.
\]

For the default diagnostic policy success set `A`, define

\[
V(A)=\sum_{x_i\in A}\frac{2^i}{255}.
\]

Equivalently,

\[
\boxed{255V(A)=\sum_{x_i\in A}2^i,}
\]

which is exactly the bitmask encoding of the success set.

Thus these weights remove the earlier cardinality collapse, but they do **not** make deployment performance independent of corrective-frontier topology in V0. This endpoint is therefore recorded only as a **secondary weighted deployment-performance endpoint**. A2-V0 does not claim to empirically separate future viability from the corrective frontier.

Define the paired deployment contrast

\[
C_{\mathrm{improve},u}=V_u(1)-V_u(0).
\]

Its sign does not authorize a frontier conclusion, and frontier topology does not authorize a general viability conclusion.

---

## 16. Information-boundary transplant

For units whose primary frontier changes, the implementation may transplant the constructor-visible learned state between matched evaluation replicas in both directions while holding the rest of evaluation fixed.

This is **not** a discovery-of-mediation experiment in V0. Because the realization contract already declares that evaluation availability depends on the constructor-visible active hypothesis, the transplant is an information-boundary validation check:

\[
\boxed{
\text{frontier follows transplanted declared constructor state}
\Rightarrow
\text{implementation respects the declared V0 boundary}.
}
\]

Failure is a contract discrepancy, not evidence for an unexpected mediator.

---

## 17. Isolation and matching invariants

Across arms, freeze:

\[
\mathcal U^+=\mathcal U^-,
\quad
B^+=B^-,
\quad
c^+=c^-,
\quad
R^+=R^-,
\quad
\mathcal T^+=\mathcal T^-.
\]

Also match the true environment, rotation, initial learner state, training latent-state schedule, external task information, and implementation.

Allowed to diverge causally downstream of feedback are learned state, active hypothesis, constructor-visible state, chosen repairs, and visible histories.

Forbidden are post-assignment analyst information, resource changes, shared mutable learning state, or any other cross-arm/cross-unit contamination.

---

## 18. Validation gate

No unresolved scientific interpretation is admitted until the implementation reproduces all 64 theorem-derived signatures and passes the remaining invariants.

A theorem-control mismatch yields:

```text
CONTROL_MISMATCH
→ STOP
→ no scientific interpretation
→ localize implementation/proof discrepancy
```

Any other required invariant failure yields:

```text
INVALID_NO_SCIENTIFIC_RESULT
→ STOP
→ no scientific interpretation
```

The implementation must validate, at minimum, the 48-hypothesis universe, 384-unit construction, pre-treatment clone equality, identical arm contracts, isolation, true-hypothesis survival, control nonlearning, constructor information boundary, exactly nine realized policies, frozen evaluation costs, no evaluation learning, all-256-subset enumeration, downward closure, and absence of result-dependent thresholds or training extensions.

The science command must rerun the gates in its own process rather than accepting a saved PASS receipt.

---

## 19. Pre-execution operational accounting completion

The scientific design required equal processing charges but did not numerically define one complete hypothesis-processing batch.

During implementation, **before unresolved-unit execution**, the following convention was made explicit and then frozen:

\[
\boxed{
\text{one complete 48-hypothesis processing batch}=1\text{ abstract training-cost unit}.
}
\]

Each training episode therefore records 4 primitive-action units plus 1 processing-batch unit, for 40 abstract units per arm across eight episodes. The loop always checks all 48 hypotheses and neither the charge nor loop length depends on outcome or version-set size.

This is an operational accounting completion, not a demonstrated scientific effect. It does not alter the fixed eight-episode learning trajectory or the evaluation frontier feasibility relation.

The validated scientific source digest after this completion is:

```text
dd454df0cf646b44a11f91bc965ab5a40de1e62c860dacdf0e988d32205dc02d
```

---

## 20. Execution and interpretation order

The frozen sequence is:

\[
\boxed{
\text{preregister}
\rightarrow
\text{implement}
\rightarrow
\text{implementation validation}
\rightarrow
\text{execute}
\rightarrow
\text{frozen-rule interpretation}.
}
\]

For A2-V0 specifically:

\[
\boxed{
\text{implement frozen assay}
\rightarrow
\text{reproduce all 64 theorem controls}
\rightarrow
\text{validate remaining invariants}
\rightarrow
\text{execute the 320 unresolved units}.
}
\]

The analysis order is:

\[
\boxed{
\text{primary frontier endpoint}
\rightarrow
\text{secondary weighted deployment endpoint}
\rightarrow
\text{information-boundary transplant check}
\rightarrow
\text{secondary trajectory observations}.
}
\]

No secondary story may rescue or rewrite the primary frontier result.

---

## 21. Frozen scientific claim ceiling

Even a maximal positive execution may establish at most:

> In this finite exhaustive assay, informative feedback causally changes learned system state in ways that can change the system-realizable corrective frontier under fixed primitive affordances.

A2-V0 cannot establish general self-improvement, general corrigibility, open-ended policy invention, unfamiliar-error discovery, population-level claims beyond the declared 384-unit universe, universal monotonicity, or a unique causal decomposition through `g`, `Q`, or `Π`.

The experimental design is explicitly allowed to return expansion, null, contraction, and tradeoff structure.

---

## 22. Custody

The validated implementation source, tests, protocol, provenance, result-bearing records, and byte identities of the original standalone packages are preserved under `experiments/a2_v0/` and indexed by `experiments/a2_v0/CUSTODY.md`.

The implementation was built against MATRIX repository commit:

```text
b006a581161be65ea34df39ba9558facddac386b
```

No README or MATRIX₀ kernel change is implied by this preregistration.
