# EXEC_V0 — Closed-loop execution semantics

**Status:** Attack 1 formalization for MATRIX₀.

> **This document tests whether the existing `\Phi_B` remains sufficient once execution is given fully closed-loop semantics. It does not modify the MATRIX kernel.**

Repository pre-state for this artifact:

```text
main = 5f900c1853f072aaeb8389c02d1f8da0cdd2d930
```

The README is intentionally unchanged by this artifact.

The attack asks whether a globally robust corrective policy remains well-defined under interactive, adaptive, and adversarial execution, and whether information-conditioned residual problems can be faithfully re-expressed using the existing MATRIX semantic roles.

The governing information invariant is:

```math
\boxed{\text{hidden from policy}\neq\text{absent from execution semantics}}
```

and, for deterministic policies,

```math
\boxed{
h(\tau_1)=h(\tau_2)
\Rightarrow
\pi(h(\tau_1))=\pi(h(\tau_2))
}
```

The canonical residual construction used below,

```math
\Omega^h=\mathcal K(h),
```

is an **encoding construction**, not an ontological claim about the "real" state of the world.

---

## 1. Scope and claim ceiling

This document does **not** claim:

```text
- a general theory of intelligence
- a general theory of corrigibility
- that every real environment satisfies the EXEC_V0 assumptions
- that feedback invents diagnostics
- that interactive success implies between-episode persistence
- that MATRIX is empirically validated
```

It tests one narrower question:

```math
\boxed{
\text{Can the existing }\Phi_B\text{ semantics represent robust closed-loop correction without adding a new kernel object?}
}
```

The attack-local outcomes are:

```text
proof obligations close
→ MATRIX₀ survives Attack 1 under the declared EXEC_V0 contract

semantic/type underspecification
→ repair EXEC contract/type
→ MATRIX₀ unchanged

faithful representation remains impossible after sufficient typing
→ explicit counterexample
→ candidate MATRIX₁
```

---

## 2. Execution primitives

### 2.1 Latent state and mutable execution state

Let

```math
x\in\Omega
```

be the latent episode state over which the corrective guarantee is quantified.

Let

```math
G_t
```

be the complete mutable execution state at interaction step `t`.

`G_t` may contain future-relevant hidden distinctions such as environment state, instrument state, adversarial memory, or resource state. The policy does not receive `G_t` merely because the execution semantics contain it.

Thus:

```math
\boxed{G_t\not\equiv h_t}
```

and:

```math
\boxed{\text{state existence}\neq\text{state observability}.}
```

### 2.2 Primitive action boundary

Let

```math
\mathcal U
```

be the declared set of primitive executable actions/interventions available in the episode.

State-dependent legality or consequences are evaluated by the execution semantics. A policy that selects an action whose execution is invalid on a compatible latent path fails on that path; hidden state is not exposed merely to help the policy choose a legal action.

### 2.3 Policy-visible history

Let

```math
h_0=\epsilon
```

and, after `t` nonterminal interactions,

```math
h_t=(q_0,o_0,\ldots,q_{t-1},o_{t-1}).
```

A deterministic policy is a causal map

```math
\pi:h_t\mapsto q_t\in\mathcal U.
```

The policy may condition on its visible history and on nothing else unless the declared interface explicitly places that information into the history.

Therefore, for any two execution prefixes with the same visible history,

```math
h(\tau_t^{(1)})=h(\tau_t^{(2)})
\Rightarrow
\pi(h(\tau_t^{(1)}))=\pi(h(\tau_t^{(2)})).
```

This is the formal nonleakage constraint.

---

## 3. Environment response jurisdiction

A response strategy `\rho` is a causal strategy for the responding environment under a declared information boundary.

For compactness, write the response at step `t` as

```math
r_t=\rho(G_t,h_t,q_t;x),
```

with the understanding that the actual arguments observable to `\rho` are part of the declared response jurisdiction. An assay may allow the environment to know `x`, public history, current world state, and the current action while withholding other information. Future policy actions are never available causally.

Let

```math
\mathcal R(\pi,x,G_0)
```

denote the globally admissible response strategies against policy `\pi` from latent state `x` and initial execution state `G_0`.

The zero-error adversarial semantics quantify over every strategy in this set.

A stochastic assay may later replace universal response quantification with an explicitly declared probability law for graded performance. That does not weaken the robust zero-error frontier defined here.

---

## 4. Transition recursion

The environment transition is

```math
\boxed{
(G_{t+1},o_t)
=
\mathsf{Step}(G_t,x,q_t,r_t).
}
```

Therefore a nonterminal closed-loop interaction has the form

```text
visible history h_t
      ↓ π
primitive action q_t
      ↓ ρ
response r_t
      ↓ Step
new execution state G_{t+1} + observation o_t
      ↓
visible history h_{t+1}
```

The important point is that diagnostic action may alter the future diagnostic landscape:

```math
q_t\rightarrow G_{t+1}\rightarrow q_{t+1}.
```

A reactive or strategic Smith-like environment is therefore inside `Exec`; it does not require a new frontier object.

---

## 5. Terminal repair and success

Let

```math
\mathsf{Term}(q_t)=1
```

mean that `q_t` is a declared terminal repair action.

Its validity is determined by the existing repair relation:

```math
R(x,q_t,G_t)=1.
```

Execution succeeds iff it reaches some finite terminal time `T` such that

```math
\mathsf{Term}(q_T)=1
```

and

```math
R(x,q_T,G_T)=1.
```

Illegal execution, an invalid terminal repair, or nontermination is failure under the zero-error frontier.

If a concrete assay requires the environment to react to a proposed repair before validity can be judged, that repair is modeled as a nonterminal primitive action and the terminal predicate is applied only after the resulting transition. No new semantic role is required.

---

## 6. Pathwise cost

Cost belongs to an execution path, not to a policy in isolation.

The single existing cost model `c` may contain:

```text
- an initial debit
- per-step execution costs
- terminal costs
```

For a fresh episode the initial debit is normally zero.

For a finite successful execution path `\tau_T`, define additive total cost

```math
C(\tau_T)
=
c_{\mathrm{init}}(x,G_0)
+
\sum_{t<T} c_{\mathrm{step}}(G_t,h_t,q_t,r_t,o_t)
+
c_{\mathrm{term}}(x,G_T,h_T,q_T).
```

All charged resources must be declared by the assay. If policy synthesis, diagnostic compilation, working memory, wall-clock time, or another resource is treated as free, that is an explicit model assumption rather than an implicit loophole.

The initial debit is included inside the existing cost model because residual executions may need to retain hidden prefix-specific resource debt without exposing that debt to the policy.

This prevents the invalid replacement of pathwise accounting by a single information-conditioned residual budget such as

```math
B-C_{\max}(h).
```

Two compatible prefixes may have different debts and different suffix costs while both complete exactly within the same original total budget.

---

## 7. Closed-loop `Exec`

For declared `\pi`, `x`, `G_0`, and `\rho`, define

```math
\mathrm{Exec}(\pi,x;G_0,\rho)
```

as the recursively generated trajectory obtained by repeatedly applying Sections 2–6 until success or failure.

A full finite execution records enough information for the verifier to reconstruct at least:

```text
latent state x
mutable states G_0,...,G_T
visible histories h_0,...,h_T
policy actions q_0,...,q_T
environment responses r_0,...,r_{T-1}
observations o_0,...,o_{T-1}
pathwise cost
terminal status
```

The policy itself receives only the declared visible history.

Write

```math
\mathrm{Success}(\mathrm{Exec}(\pi,x;G_0,\rho))=1
```

for finite valid-repair termination.

---

## 8. Robust zero-error corrective frontier

With all assay contracts other than the policy fixed, define

```math
\boxed{
\Phi_B(G_0)
=
\left\{
S\subseteq\Omega:
\exists\pi\;
\forall x\in S\;
\forall\rho\in\mathcal R(\pi,x,G_0),
\begin{array}{l}
\mathrm{Success}(\mathrm{Exec}(\pi,x;G_0,\rho))=1,\\[1mm]
C(\mathrm{Exec}(\pi,x;G_0,\rho))\le B
\end{array}
\right\}.
}
```

The crucial quantifier order is

```math
\boxed{\exists\pi\;\forall x\;\forall\rho.}
```

It is not

```math
\forall x\;\forall\rho\;\exists\pi.
```

One policy must work without being handed the true latent state or the environment's future response strategy.

---

## 9. Reachable prefixes and residual jurisdiction

Fix a set `S`, a witnessing policy `\pi`, and an initial state `G_0`.

A full execution prefix at time `t` is written

```math
\tau_t=(x,G_0,q_0,r_0,o_0,\ldots,G_t),
```

with visible projection

```math
h(\tau_t)=h_t.
```

For a reachable visible history `h`, define the compatible-prefix class

```math
\boxed{
\mathcal K(h)
=
\left\{
\tau_t:
\begin{array}{l}
\tau_t\text{ is reachable under }\pi\text{ from some }x\in S,\\
\text{under some globally admissible response strategy, and}\\
h(\tau_t)=h
\end{array}
\right\}.
}
```

Multiple elements of `\mathcal K(h)` may contain different hidden `G_t`, different response memory, and different accumulated cost.

The policy may not select among them.

### 9.1 Suffix policy

For visible prefix `h`, define the same-policy suffix

```math
\boxed{
\pi|_h(\bar h)
=
\pi(h\mathbin{\|}\bar h),
}
```

where `\bar h` is the visible history generated after the prefix and `\|` denotes history concatenation.

### 9.2 Residual response strategies

For a compatible full prefix `\tau\in\mathcal K(h)`, let

```math
\mathcal R_h(\tau)
```

be exactly the response-strategy continuations that are admissible after `\tau`.

The required restriction-consistency contract is:

```math
\boxed{
\forall\tau\in\mathcal K(h),\;
\forall\rho'\in\mathcal R_h(\tau),\;
\exists\widehat\rho\in\mathcal R(\pi,x(\tau),G_0)
}
```

such that execution under `\widehat\rho` has prefix `\tau` and continuation `\rho'`.

Equivalently: restarting the mathematical description at a reachable prefix neither creates new environment powers nor silently removes powers that were part of the original response jurisdiction.

This is the Attack 1 restriction-consistency condition.

---

## 10. P3a — same-policy suffix viability

### Theorem P3a

Assume:

```text
A1. π witnesses S ∈ Φ_B(G_0).
A2. Residual response jurisdiction is restriction-consistent as in Section 9.2.
A3. Pathwise cost is additive across prefix and continuation.
```

Then for every reachable visible history `h`, every compatible prefix `\tau\in\mathcal K(h)`, and every residual response continuation `\rho'\in\mathcal R_h(\tau)`, the same suffix policy `\pi|_h` succeeds and remains globally budget-valid:

```math
\boxed{
\mathrm{Success}(\mathrm{Exec}(\pi|_h,\tau,\rho'))=1
}
```

and

```math
\boxed{
C(\tau)
+
C_{\mathrm{suffix}}(\pi|_h,\tau,\rho')
\le B.
}
```

Here `\mathrm{Exec}(\pi|_h,\tau,\rho')` means continuation from the complete execution prefix `\tau`, not a fresh episode that forgets the prefix.

### Proof

Fix arbitrary reachable `h`, compatible `\tau\in\mathcal K(h)`, and `\rho'\in\mathcal R_h(\tau)`.

By restriction consistency, `\rho'` can be spliced onto `\tau` to form a globally admissible response strategy `\widehat\rho` for the original episode.

Because `\pi` witnesses `S\in\Phi_B(G_0)`, the complete execution against `\widehat\rho` must terminate in a valid repair and have total path cost at most `B`.

After visible history `h`, deterministic policy behavior is exactly

```math
\pi|_h(\bar h)=\pi(h\mathbin{\|}\bar h).
```

Therefore the continuation generated by `\rho'` from `\tau` is the suffix of the globally valid execution generated by `\widehat\rho`.

The suffix must therefore terminate successfully. By additive pathwise accounting,

```math
C_{\mathrm{total}}
=
C(\tau)
+
C_{\mathrm{suffix}}(\pi|_h,\tau,\rho')
\le B.
```

Since `h`, `\tau`, and `\rho'` were arbitrary, the theorem holds for every reachable information class and every compatible residual continuation. `\square`

### Standing

```text
P3a: PROVED under A1–A3.
```

P3a is behavioral closure. It does **not** yet assert that the residual game can be packaged as a fresh ordinary `\Phi_B(G)` instance.

---

## 11. P3b — faithful information-conditioned residualization

P3b asks whether the same residual behavior can be faithfully re-expressed using the existing MATRIX execution roles.

### 11.1 Canonical residual domain

For reachable visible history `h`, define

```math
\boxed{
\Omega^h:=\mathcal K(h).
}
```

A residual latent state

```math
z\in\Omega^h
```

is therefore a complete compatible execution prefix `z=\tau`.

This is a proof encoding. It is **not** an ontological claim that execution prefixes are the metaphysically correct states of the system.

The residual latent state may carry distinctions that the policy cannot observe, including:

```text
- original latent episode state x(z)
- actual mutable execution state G(z)
- response-strategy memory encoded by the prefix
- accumulated path cost C(z)
```

### 11.2 Residual policy

The residual policy receives only the common visible prefix plus new visible suffix observations:

```math
\boxed{
\pi^h(\bar h)=\pi(h\mathbin{\|}\bar h).
}
```

It never receives `z`.

Therefore for any `z_1,z_2\in\Omega^h` and the same residual visible history `\bar h`,

```math
\pi^h(\bar h;z_1)
=
\pi^h(\bar h;z_2)
=
\pi(h\mathbin{\|}\bar h).
```

Latent variation may affect execution but not policy choice.

### 11.3 Residual response jurisdiction

For `z=\tau`, define

```math
\boxed{
\mathcal R^h(z):=\mathcal R_h(\tau).
}
```

Thus every residual response is exactly a continuation permitted by the original response jurisdiction after that prefix.

### 11.4 Residual transition

Let the residual episode begin from a common wrapper execution state `G_0^h=\bot_h`.

The wrapper is only an encoding device. On the first residual nonterminal action, the residual step function delegates to the actual execution state carried by `z`:

```math
\mathsf{Step}^h(\bot_h,z,q,r)
:=
\mathsf{Step}(G(z),x(z),q,r).
```

After the first residual transition, `\mathsf{Step}^h` tracks the corresponding original continuation state and continues by delegating to the original `\mathsf{Step}` with latent original state `x(z)`.

All future-relevant hidden distinctions that affect transition behavior must remain represented in `z`, the carried execution state, or another already-declared latent component of the residual execution semantics.

### 11.5 Residual success

Residual terminal success delegates to the original repair relation on the corresponding original continuation state:

```math
\boxed{
\mathrm{Success}_{h}(z,\rho')=1
\iff
\mathrm{Success}_{\mathrm{orig}}(z,\rho')=1.
}
```

The verifier may evaluate hidden latent state. The policy may not observe it unless the interface exposes it.

### 11.6 Residual cost

Keep the original total budget:

```math
\boxed{B^h:=B.}
```

Do not replace it by one artificial information-conditioned remaining budget.

The residual cost model uses its initial-debit component to retain the exact prefix debt:

```math
c^h_{\mathrm{init}}(z,\bot_h):=C(z).
```

All subsequent step and terminal costs delegate to the original cost model on the corresponding continuation.

Therefore:

```math
\boxed{
C_h(z,\rho')
=
C(z)+C_{\mathrm{suffix}}(z,\rho').
}
```

and hence:

```math
\boxed{
C_h(z,\rho')\le B
\iff
C(z)+C_{\mathrm{suffix}}(z,\rho')\le B.
}
```

This preserves path-specific resource debt without leaking that debt into policy selection.

### 11.7 Trace-preservation lemma

For every `z=\tau\in\Omega^h` and every `\rho'\in\mathcal R^h(z)`, residual execution under `\pi^h` generates the same action/observation continuation as the original execution of `\pi` after prefix `\tau`.

#### Proof

At residual history `\bar h=\epsilon`,

```math
\pi^h(\epsilon)=\pi(h),
```

which is exactly the original next policy action after prefix `\tau` because `h(\tau)=h`.

The residual response jurisdiction supplies exactly an admissible original continuation response, and `\mathsf{Step}^h` delegates to the actual original execution state carried by `z`. Therefore the first residual observation and next execution state equal the first observation and state of the original suffix.

Assume equality through residual history `\bar h_k`. Then

```math
\pi^h(\bar h_k)
=
\pi(h\mathbin{\|}\bar h_k),
```

so both executions choose the same next action. The residual response and transition again delegate to the corresponding original continuation. Therefore the next observation and state agree.

Induction gives trace equality for the whole residual execution. `\square`

### 11.8 Theorem P3b

Assume the execution contract permits:

```text
C1. latent state rich enough to preserve every distinction that can change future execution judgments;
C2. policy observation separated from latent execution state;
C3. Step, repair, cost, and response admissibility may depend on latent state without exposing it to the policy;
C4. residual response strategies are genuine restrictions of globally admissible original strategies;
C5. the cost model can retain exact prefix-specific initial debt.
```

Then every reachable policy-visible history `h` admits the canonical residual instance above, using the existing MATRIX execution roles, such that for every compatible latent prefix `z` and admissible residual response `\rho'`:

```math
\boxed{
\mathrm{Success}_{\mathrm{res}}(z,\rho')
\iff
\mathrm{Success}_{\mathrm{orig\ suffix}}(z,\rho')
}
```

and

```math
\boxed{
C_{\mathrm{res}}(z,\rho')\le B
\iff
C(z)+C_{\mathrm{suffix}}(z,\rho')\le B.
}
```

The residual policy sees only its declared visible history and never the identity of `z`.

Therefore the declared class of EXEC_V0 closed-loop correction problems is closed under information-conditioned residualization. `\square`

### Standing

```text
P3b: PROVED under C1–C5 by canonical residual construction.
```

The key localization result is:

```math
\boxed{
\text{hidden from policy}
\not\Rightarrow
\text{erased from dynamics, admissibility, repair, or accounting}.
}
```

---

## 12. P1 — downward closure

### Theorem P1

Under the frontier definition in Section 8, assume response admissibility for a fixed `(\pi,x,G_0)` does not become stronger merely because the declared uncertainty set is replaced by one of its subsets.

Then:

```math
\boxed{
S\in\Phi_B(G_0),\quad S'\subseteq S
\Rightarrow
S'\in\Phi_B(G_0).
}
```

### Proof

Let `\pi` witness `S\in\Phi_B(G_0)`.

For every `x\in S'`, we also have `x\in S`. Therefore, for every admissible `\rho\in\mathcal R(\pi,x,G_0)`, the same policy `\pi` succeeds within budget `B` because it already does so for every `x\in S`.

Thus the same `\pi` witnesses `S'\in\Phi_B(G_0)`. `\square`

### Standing

```text
P1: PROVED under restriction-monotone feasibility.
```

Finiteness of `\Omega` is **not** required for downward closure.

---

## 13. P4a — finite minimal-obstruction representation

Assume from here that `\Omega` is finite.

Define the minimal excluded family

```math
\boxed{
H_B(G_0)
=
\mathrm{Min}\left(2^\Omega\setminus\Phi_B(G_0)\right).
}
```

Here `\mathrm{Min}` means inclusion-minimal elements.

### Theorem P4a

For finite `\Omega` and downward-closed `\Phi_B(G_0)`,

```math
\boxed{
S\in\Phi_B(G_0)
\iff
\nexists H\in H_B(G_0)\text{ with }H\subseteq S.
}
```

### Proof

If `S\in\Phi_B(G_0)` and some `H\in H_B(G_0)` satisfied `H\subseteq S`, downward closure would imply `H\in\Phi_B(G_0)`, contradicting the definition of `H_B` as excluded sets.

Conversely, suppose `S\notin\Phi_B(G_0)`. Since `\Omega` is finite, the finite collection of excluded subsets of `S` contains at least one inclusion-minimal excluded member `H`. By definition `H\in H_B(G_0)` and `H\subseteq S`.

Therefore infeasibility is represented exactly by containment of a minimal obstruction. `\square`

### Standing

```text
P4a: PROVED for finite Ω once P1 holds.
```

This is a structural representation result. It does not yet imply the memory/coloring theorem.

---

## 14. P4b — hypergraph coloring / memory characterization

P4b is intentionally scoped to a specific memory model.

### 14.1 Memory model assumptions

Assume:

```text
M1. Ω is finite and nonempty.
M2. A retained representation is a deterministic encoder g: Ω → M.
M3. Arbitrary partitions of Ω induced by such encoders are admissible.
M4. The decoder receives the retained message m and may use the declared future execution machinery.
M5. Safety means every nonempty encoder cell g^{-1}(m) lies in Φ_B(G_0).
M6. Retained-memory cost counts only the number of message symbols; fixed-width binary storage costs ceil(log2 |M_used|) bits. Encoder/decoder program complexity is not charged as instance-specific retained memory in this theorem.
```

Let

```math
M_B^*
```

be the minimum number of nonempty message cells in a safe encoder, and let

```math
m_B^*
```

be the corresponding minimum fixed-width retained bits.

Treat `H_B(G_0)` as a hypergraph on vertex set `\Omega`.

A weak proper coloring is a coloring in which no hyperedge is monochromatic. Let

```math
\chi(H_B)
```

be its minimum number of colors.

### Lemma — safe encoders are exactly weak proper colorings

A deterministic encoder `g` is safe iff its message labels form a weak proper coloring of `H_B`.

#### Proof

Suppose `g` is safe. If some minimal obstruction `H\in H_B` were monochromatic, then `H` would lie inside one encoder cell `g^{-1}(m)`. Since that cell is safe and `\Phi_B` is downward closed, `H` would also be feasible, contradicting `H\in H_B`.

Conversely, suppose the coloring has no monochromatic hyperedge. If some encoder cell `C=g^{-1}(m)` were infeasible, P4a implies that `C` contains some `H\in H_B`. Every vertex of `H` would then have the same message label `m`, making `H` monochromatic. Contradiction.

Thus safety and weak proper coloring are equivalent. `\square`

### Theorem P4b

Under M1–M6:

```math
\boxed{
M_B^*=\chi(H_B)
}
```

and

```math
\boxed{
m_B^*=\left\lceil\log_2\chi(H_B)\right\rceil.}
```

### Proof

By the lemma, safe encoders with `k` nonempty message cells are exactly weak proper colorings using `k` colors. Minimizing over `k` therefore gives

```math
M_B^*=\chi(H_B).
```

Under the declared fixed-width binary memory model, representing `M_B^*` distinct messages requires exactly

```math
\left\lceil\log_2 M_B^*\right\rceil
```

bits. Substitution yields

```math
m_B^*=\left\lceil\log_2\chi(H_B)\right\rceil.
```

`\square`

### Standing

```text
P4b: PROVED under the exact M1–M6 memory/decoding model.
```

This theorem is **not** a universal statement about memory. Changing the representation class, allowing stochastic encoders, charging encoder/decoder program complexity, changing the safety predicate, or changing the storage model requires a new theorem.

---

## 15. Attack 1 verdict

The formal obligations now stand as:

```text
ATTACK 1 — CLOSED-LOOP EXECUTION

P1   downward closure
     PROVED under restriction-monotone feasibility

P3a  same-policy suffix viability
     PROVED under A1–A3

P3b  faithful information-conditioned residualization
     PROVED under C1–C5 by canonical residual construction

P4a  finite minimal-obstruction representation
     PROVED for finite Ω once P1 holds

P4b  hypergraph coloring / memory characterization
     PROVED under M1–M6
```

Therefore the attack-local verdict is:

```math
\boxed{
\mathrm{MATRIX}_0
\text{ survives Attack 1 under the declared EXEC_V0 semantics.}
}
```

This verdict means only that the first hostile closed-loop/adversarial construction has not forced a new kernel object. It does **not** establish universal correctness of MATRIX, empirical validity, general corrigibility, or any stronger causal claim.

The hostile construction instead forced a semantic clarification:

```math
\boxed{
\text{latent state may affect execution, admissibility, repair, and cost}
\neq
\text{latent state may affect policy choice}.
}
```

No MATRIX₁ is earned by Attack 1.

No new frontier is introduced.

No new scalar is introduced.

No README theory change is implied.

---

## 16. What would still break this result?

Attack 1 would have to be reopened only by a concrete counterexample to one of its explicit assumptions or proofs, for example:

```text
- a future-relevant distinction that cannot be represented in the latent execution semantics without leaking it to the policy;
- a residual response jurisdiction that cannot be represented as a faithful restriction of the original game;
- non-additive resource semantics for which the declared cost contract is inappropriate;
- a counterexample to the trace-preserving canonical residual construction under C1–C5;
- a counterexample to P4b while retaining every assumption M1–M6.
```

Such a result must first be localized to contract, type, theorem, or kernel before any conceptual revision is authorized.
