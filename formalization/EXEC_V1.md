# EXEC_V1 — System-relative closed-loop execution semantics

**Status:** audited Attack 1 repair for MATRIX₀.

> **This document repairs the execution contract exposed by review of `EXEC_V0`. It does not modify the MATRIX conceptual kernel.**

Repository ancestry for this artifact:

```text
121f71090a01b6d049fadb2596172cff8aad3896  EXEC_V0 historical artifact
ad42cbe4bdba0b67b66e26d5ec7e753b264377d5  initial EXEC_V1 draft
```

`formalization/EXEC_V0.md` remains unchanged as the historical artifact that exposed the defects. The README remains intentionally unchanged.

The repaired semantics address:

```text
A1R  exact residual-response jurisdiction
A1M  infeasible memory/coloring theorem domain
A1P  system-relative, non-oracular policy realization
```

The two attack-earned anti-oracle invariants are:

```math
\boxed{\text{hidden from policy}\neq\text{absent from execution}}
```

and

```math
\boxed{\text{describable by analyst}\neq\text{realizable by system}.}
```

The protected capability distinctions are:

```math
\boxed{
\text{policy exists}
\neq
\text{policy is realizable}
\neq
\text{policy succeeds}
\neq
\text{policy is affordable}.
}
```

---

## 1. Scope and claim ceiling

This artifact asks whether the existing MATRIX roles can represent robust closed-loop correction once policy availability is made system-relative.

It does **not** claim:

```text
- that feedback empirically improves Π, Q, g, Avail, or Φ_B;
- that semantic sensitivity is evidence of learning;
- that every real system satisfies these realization contracts;
- that frontier expansion implies future-viability gain;
- that future-viability gain implies frontier preservation;
- a general theory of intelligence or corrigibility;
- empirical validation of MATRIX.
```

The corrective-frontier pathway is:

```math
\boxed{
(\Pi,\mathcal U,i_0)
\rightarrow
\mathrm{Avail}
\rightarrow
\Phi_B
\rightarrow
\Delta_B^{\pm}
}
```

while the viability pathway remains separate:

```math
\boxed{F\rightarrow C_{\mathrm{improve}}^{(h)}.}
```

The protected non-implications are:

```math
\boxed{\Delta_B^+\neq\varnothing\not\Rightarrow C_{\mathrm{improve}}>0}
```

and:

```math
\boxed{
C_{\mathrm{improve}}>0
\not\Rightarrow
\left(\Delta_B^+\neq\varnothing\land\Delta_B^-=\varnothing\right)
}
```

with:

```math
\boxed{C_{\mathrm{improve}}>0\not\Rightarrow\Delta_B^-=\varnothing.}
```

---

## 2. Existing execution roles

Let `x\in\Omega` be the latent episode state and `G_t` the complete mutable execution state.

`G_t` may contain hidden environment state, instrument state, adversarial memory, realized-policy state, or resource debt. The policy receives only its declared visible history `h_t`.

For deterministic policies:

```math
\boxed{
h(\tau_1)=h(\tau_2)
\Rightarrow
\pi(h(\tau_1))=\pi(h(\tau_2)).
}
```

Thus:

```math
\boxed{\text{state existence}\neq\text{state observability}.}
```

Let `\mathcal U` be the primitive executable affordances, `R` the valid-repair relation, `c` the grounded resource model, `B` the corrective budget, and `\mathcal R` the environment-response jurisdiction.

Closed-loop execution is:

```math
\mathrm{Exec}(\pi,x;G_0,\rho),
```

with policy actions determined only by policy-visible history. Hidden state may affect transition, admissibility, repair, and cost without becoming policy information.

Illegal execution, invalid terminal repair, or nontermination is failure under the zero-error frontier.

---

## 3. Constructor-visible information and policy realization

Policy realization has a separate information boundary.

Define:

```math
\boxed{i_\Pi:G\rightarrow I_\Pi}
```

and write:

```math
i_0=i_\Pi(G).
```

`i_0` may contain persistent learned state readable by `\Pi`, retained messages, declared task information, compiler state, or other explicitly exposed realization inputs.

By default it does **not** contain hidden `x` and does **not** contain an analyst-only description of the tested uncertainty set `S`.

If task information is genuinely supplied to the system, it may enter `i_0` through a declared interface.

### 3.1 Temporal realization boundary

Availability is evaluated at the declared realization point from assay-time machinery and constructor-visible information:

```math
\boxed{\text{realizable now}\neq\text{may become realizable later}.}
```

Capabilities acquired through observations after assay start are not credited to initial availability in advance.

If online synthesis uses episode observations, that synthesis belongs inside executable episode semantics, with its observations, state transitions, and costs represented explicitly.

### 3.2 Realization relation

Let `\mathcal P_{\mathcal U}` be policies executable through `\mathcal U`.

Define:

```math
\boxed{
\mathfrak{Real}_{\Pi,\mathcal U}(i)
\subseteq
\Delta\times\mathcal P_{\mathcal U}.
}
```

A pair:

```math
(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i)
```

means `\delta` is a valid provenance-bearing route through the system's own policy machinery that constructs or selects executable policy `\pi` from `(\Pi,\mathcal U,i)`.

Write:

```math
\boxed{\delta\xRightarrow[\Pi,\mathcal U,i]{}\pi.}
```

Define the available policy set as its policy projection:

```math
\boxed{
\mathrm{Avail}(\Pi,\mathcal U;i)
=
\{\pi:\exists\delta,\;(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i)\}.
}
```

Full hidden `G` influences realization only through the declared projection:

```math
\boxed{
\mathrm{Avail}(G,\Pi,\mathcal U;i_\Pi(G))
:=
\mathrm{Avail}(\Pi,\mathcal U;i_\Pi(G)).
}
```

### 3.3 No hidden realization query

A pre-execution realization derivation may inspect `i_0` and the specification of `\mathcal U`; it may not interact with hidden episode state and still call that interaction realization.

```math
\boxed{
\text{interaction capable of revealing }x
\Rightarrow
\text{episode execution, not hidden pre-policy realization}.
}
```

### 3.4 Controlled realization convention

The existential `\exists\delta` credits only realization branches deliberately reachable/selectable by the declared system machinery from `(\Pi,\mathcal U,i)`.

A merely lucky uncontrolled stochastic constructor outcome is not existentially credited. Stochastic realization requires an explicit future probability/robustness contract.

This artifact measures reachable policy space, not autonomous policy discoverability beyond the declared `\Pi` machinery.

---

## 4. A1P1 — constructor-information factorization

### Contract

```math
\boxed{
\begin{aligned}
&i_\Pi(G_1)=i_\Pi(G_2),\\
&\Pi_1=\Pi_2,\\
&\mathcal U_1=\mathcal U_2
\end{aligned}
\Rightarrow
\mathfrak{Real}_{\Pi_1,\mathcal U_1}(i_\Pi(G_1))
=
\mathfrak{Real}_{\Pi_2,\mathcal U_2}(i_\Pi(G_2)).
}
```

Therefore:

```math
\boxed{
\mathrm{Avail}(\Pi_1,\mathcal U_1;i_\Pi(G_1))
=
\mathrm{Avail}(\Pi_2,\mathcal U_2;i_\Pi(G_2)).
}
```

### Proof

`\mathfrak{Real}` is defined only from `(\Pi,\mathcal U,i)`. Hidden `x`, analyst set `S`, and components of `G` outside `i_\Pi(G)` are not realization inputs. Equal declared inputs therefore induce equal realization relations and equal policy projections. `\square`

### Standing

```text
A1P1: PROVED BY FACTORIZATION / NONINTERFERENCE CONTRACT.
```

The symmetry is:

```math
\boxed{
\begin{aligned}
\text{realization: }&\text{same constructor-visible information}
\Rightarrow\text{same realizable-policy set},\\
\text{execution: }&\text{same policy-visible history}
\Rightarrow\text{same policy action}.
\end{aligned}
}
```

---

## 5. A1P2 — realization cost

A realization witness may have cost:

```math
C_{\mathrm{real}}(\delta),
```

which is the realization/selection portion of the existing resource model `c`, not a new kernel primitive.

Two assay conventions are admissible.

### 5.1 In-scope realization

If realization occurs after assay start:

```math
\boxed{
C_{\mathrm{charged}}
=
C_{\mathrm{real}}(\delta)+C_{\mathrm{exec}}.
}
```

If realization changes persistent machinery or resource state, let `G^\delta` denote the post-realization state from which episode execution begins.

### 5.2 Pre-realized policy

If realization genuinely occurred before assay start, its cost may be explicitly sunk for that assay only if the realized policy state and provenance are already present in the initial system state.

Then:

```math
\boxed{C_{\mathrm{charged}}=C_{\mathrm{exec}}.}
```

Any realization or selection work performed after assay start remains charged.

### Standing

```text
A1P2: CLOSED UNDER AN EXPLICIT CHARGING CONVENTION.
```

---

## 6. System-relative corrective frontier

Fix all assay contracts other than the realization witness, including `\Omega`, `\Pi`, `\mathcal U`, `R`, `c`, `B`, `\mathcal R`, and initial constructor-visible information `i_0`.

Define:

```math
\boxed{
\Phi_B(G;i_0)
=
\left\{
S\subseteq\Omega:
\exists(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i_0)
\;\forall x\in S
\;\forall\rho\in\mathcal R(\pi,x,G^\delta),
\begin{array}{l}
\mathrm{Success}(\mathrm{Exec}(\pi,x;G^\delta,\rho))=1,\\[1mm]
C_{\mathrm{charged}}(\delta,\pi,x,\rho)\le B
\end{array}
\right\}.
}
```

For a pre-realized assay, `G^\delta` denotes the already-realized initial execution state and realization cost is sunk according to Section 5.2.

The crucial order is:

```math
\boxed{\exists(\delta,\pi)\;\forall x\;\forall\rho.}
```

It is not:

```math
\forall x\;\exists(\delta,\pi),
```

and analyst set `S` is not a hidden realization input.

Thus:

```math
\boxed{
\exists\pi
\quad\longrightarrow\quad
\exists(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i_\Pi(G)).
}
```

`\Phi_B` is now system-relative rather than oracle-relative.

---

## 7. A1P3 — semantic sensitivity under fixed primitive affordances

A1P3 tests whether changing `\Pi` can change the repaired frontier while `\mathcal U` remains fixed.

Let:

```math
\Omega=\{0,1\},
```

and hold fixed:

```math
\boxed{\mathcal U^+=\mathcal U^-=\{q,r_0,r_1\}.}
```

Diagnostic action `q` returns the latent bit. Terminal repair `r_i` is valid exactly when `x=i`.

Let:

```math
c(q)=1,
\qquad
c(r_i)=1,
\qquad
B=2.
```

Use the same trivial response jurisdiction, same latent domain, same constructor-visible information, and same cost/repair contracts in both arms.

For this **semantic witness only**, declare in-assay realization cost:

```math
\boxed{C_{\mathrm{real}}(\delta)=0}
```

for every realization branch in both arms. This isolates realization-set sensitivity from realization cost; it is not an empirical resource claim.

Let untreated machinery realize exactly:

```math
\mathrm{Avail}^-=\{\pi_0,\pi_1\},
```

where `\pi_i` immediately performs `r_i`.

No untreated available policy queries `q` and branches on the observation, so:

```math
\boxed{\{0,1\}\notin\Phi_B^-.}
```

Now change only realization machinery:

```math
\Pi^+\neq\Pi^-
```

so the treated realization relation additionally contains:

```math
\pi^\star:
q
\rightarrow
\begin{cases}
r_0,&o=0,\\
r_1,&o=1.
\end{cases}
```

Therefore:

```math
\mathrm{Avail}^+
=
\mathrm{Avail}^-\cup\{\pi^\star\}.
```

For either latent state, `\pi^\star` succeeds at execution cost `2=B`, so:

```math
\boxed{\{0,1\}\in\Phi_B^+.}
```

All untreated realization witnesses remain treated witnesses. Hence:

```math
\boxed{
\mathcal U^+=\mathcal U^-,
\qquad
\mathrm{Avail}^+\supsetneq\mathrm{Avail}^-,
\qquad
\Phi_B^+\supsetneq\Phi_B^-.
}
```

### Standing

```text
A1P3: PROVED AS A FINITE SEMANTIC SENSITIVITY WITNESS.
```

This proves only that the formalism can represent a `\Pi`-mediated frontier expansion under fixed primitive affordances. It is not evidence that feedback causes such a change.

---

## 8. Reachable prefixes and A1R

Fix one realized frontier witness `(\delta,\pi)` for `S\in\Phi_B(G;i_0)`.

A full reachable prefix `\tau` contains enough verifier-visible information to reconstruct latent state, mutable execution state, response-strategy state required by the jurisdiction, realized-policy/provenance state, visible history, and charged path debt.

Let `h(\tau)` be the policy-visible projection and define:

```math
\boxed{
\mathcal K(h)
=
\{\tau:\tau\text{ is reachable under the fixed witness }(\delta,\pi),\;h(\tau)=h\}.
}
```

The policy may not select among compatible hidden prefixes.

The canonical residual domain:

```math
\boxed{\Omega^h=\mathcal K(h)}
```

is an encoding construction, not an ontology.

### 8.1 Exact residual-response jurisdiction

For an admissible original response strategy `\rho` that realizes prefix `\tau`, let `\mathrm{Res}_\tau(\rho)` retain its complete admissible continuation, including response-strategy memory needed for future behavior.

Define:

```math
\boxed{
\mathcal R_h(\tau)
=
\left\{
\mathrm{Res}_\tau(\rho):
\begin{array}{l}
\rho\in\mathcal R(\pi,x(\tau),G^\delta),\\
\tau\text{ is a prefix of }\mathrm{Exec}(\pi,x(\tau);G^\delta,\rho)
\end{array}
\right\}.
}
```

This equality prevents both adding residual adversarial powers and deleting original continuation powers.

The weaker extension direction suffices for P3a. Exact equality is used by P3b.

### Standing

```text
A1R: REPAIRED BY EXACT RESTRICTION EQUALITY.
```

---

## 9. P1 — downward closure

### Theorem

```math
S\in\Phi_B(G;i_0),\quad S'\subseteq S
\quad\Rightarrow\quad
\boxed{S'\in\Phi_B(G;i_0).}
```

### Proof

Let `(\delta,\pi)` witness `S`. The realization relation does not take analyst set `S` as input, so the same pair remains realizable when the verifier restricts attention to `S'`.

Every `x\in S'` is already covered by the robust success and budget guarantee for `S`. Thus the same pair witnesses `S'`. `\square`

### Standing

```text
P1: PROVED under system-relative realization and restriction-monotone feasibility.
```

---

## 10. P3a — same-realized-policy suffix viability

Define the suffix policy:

```math
\boxed{\pi|_h(\bar h)=\pi(h\mathbin{\|}\bar h).}
```

Let `D(\tau)` be the charged debt already incurred by prefix `\tau`, including any in-scope realization cost already paid. Explicitly sunk pre-assay realization cost is outside the assay budget and is not added.

Assume:

```text
A1. (δ,π) witnesses S ∈ Φ_B(G;i_0).
A2. Residual continuations have admissible original extensions, as implied by A1R.
A3. Charged pathwise cost is additive across prefix and continuation.
```

Then for every reachable `h`, every `\tau\in\mathcal K(h)`, and every `\rho'\in\mathcal R_h(\tau)`, the same already-realized suffix policy succeeds and:

```math
\boxed{
D(\tau)+C_{\mathrm{suffix}}(\pi|_h,\tau,\rho')\le B.
}
```

### Proof

By A1R, `\rho'` is the restriction of a globally admissible response strategy that realizes `\tau`. Global frontier membership gives successful total execution within `B`. Deterministic policy behavior after visible history `h` is exactly `\pi|_h`; additive charged accounting gives the inequality. `\square`

### Standing

```text
P3a: PROVED under A1–A3 after system-relative realization repair.
```

---

## 11. A1P4 and P3b — residualization transports earned realization

Residualization must not receive a fresh realization opportunity merely because the analyst changes mathematical viewpoint.

### 11.1 Transport rule

The original pair `(\delta,\pi)` has already realized the policy before the reachable prefix.

Transport:

```math
\boxed{(\delta,\pi,h)\longmapsto(\delta^h,\pi^h)}
```

where:

```math
\pi^h(\bar h)=\pi(h\mathbin{\|}\bar h)
```

and `\delta^h` is a provenance restriction recording that `\pi^h` is available because `\pi` was already realized by `\delta`.

`\delta^h` is not a new synthesis event.

The residual constructor-visible state contains only the common earned policy/runtime state needed to continue `\pi`; it does not receive hidden prefix identity merely because the verifier knows it.

Thus:

```math
\boxed{
\text{residualization transports an earned policy state; it does not recreate it.}
}
```

### 11.2 Residual execution and cost

Use `\Omega^h=\mathcal K(h)`. Each residual latent state `z=\tau` carries the actual future-relevant hidden execution state and charged prefix debt.

The residual transition delegates to the original continuation operator while exposing only common suffix history to `\pi^h`.

Keep:

```math
\boxed{B^h=B}
```

and define residual initial debit:

```math
\boxed{c^h_{\mathrm{init}}(z)=D(z).}
```

Therefore:

```math
\boxed{
C_h(z,\rho')=D(z)+C_{\mathrm{suffix}}(z,\rho').
}
```

No realization cost is charged twice.

### 11.3 Trace-preservation theorem

For every `z=\tau\in\Omega^h` and `\rho'\in\mathcal R_h(\tau)`, residual execution under transported policy `\pi^h` has the same action/observation continuation, hidden continuation dynamics, terminal repair judgment, response jurisdiction, and charged total as the original suffix.

The induction uses:

```text
- the same suffix policy;
- exact A1R response restriction;
- delegation to the actual hidden continuation state;
- exact path-specific prefix debt;
- no fresh realization event.
```

Hence:

```math
\boxed{
\mathrm{Success}_h(z,\rho')
\iff
\mathrm{Success}_{\mathrm{orig\ suffix}}(z,\rho')
}
```

and:

```math
\boxed{
C_h(z,\rho')\le B
\iff
D(z)+C_{\mathrm{suffix}}(z,\rho')\le B.
}
```

### Standing

```text
A1P4: PROVED under the residual-transport contract.
P3b:  PROVED under repaired A1R + A1P latent-state semantics.
```

---

## 12. P4a — finite minimal obstructions

Assume `\Omega` is finite and define:

```math
\boxed{
H_B(G;i_0)
=
\mathrm{Min}\left(2^\Omega\setminus\Phi_B(G;i_0)\right).
}
```

### Theorem

```math
\boxed{
S\in\Phi_B(G;i_0)
\iff
\nexists H\in H_B(G;i_0)\text{ with }H\subseteq S.
}
```

### Proof

If feasible `S` contained excluded `H`, downward closure would make `H` feasible, contradiction. If `S` is infeasible, finiteness supplies an inclusion-minimal excluded subset `H\subseteq S`. `\square`

### Standing

```text
P4a: PROVED for finite Ω once repaired P1 holds.
```

---

## 13. A1M and P4b — memory theorem with explicit decoder-composability scope

The initial `EXEC_V1` draft still hid one oracle/composition assumption: individual cell policies need not automatically compose into one message-conditioned decoder under system-relative realization.

P4b is therefore scoped explicitly.

Assume:

```text
M1. Ω is finite and nonempty.
M2. A retained representation is a deterministic encoder g: Ω → M.
M3. Arbitrary encoder-induced partitions of Ω are admissible.
M4. The decoder receives retained message m through a declared selection interface; m may influence policy selection, but hidden x and analyst-only S may not.
M5. Operational safety requires one decoder/selector that, for every used message m, selects a system-realizable corrective witness for cell g^{-1}(m) and succeeds within B.
M6. Retained-memory cost counts only used message symbols; fixed-width binary storage costs ceil(log2 |M_used|) bits. Decoder/encoder program complexity is not charged as instance-specific retained memory under this theorem, and any decoder realization cost is handled by the declared assay convention.
M7. Finite decoder composability: whenever every nonempty cell of a finite encoder partition individually belongs to Φ_B(G;i_0), the declared realization machinery can jointly realize one message-conditioned decoder that selects corresponding available witnesses for all cells without hidden-state access and without changing their episode success/budget judgments. Literal message labels are semantically renamable.
```

`M7` is an explicit theorem-domain assumption. It is **not** implied by A1P. If decoder composability fails, the ordinary chromatic-number theorem does not apply; that is a memory-model limitation, not automatically a MATRIX-kernel failure.

### 13.1 Extended infeasibility convention

Define `M_B^*` as the minimum number of nonempty message cells among operationally safe encoders if one exists, and:

```math
\boxed{M_B^*=+\infty}
```

otherwise.

Define `m_B^*` analogously, with:

```math
\boxed{m_B^*=+\infty}
```

when no safe encoder exists.

Treat `H_B` as a hypergraph on vertex set `\Omega`.

A weak proper coloring is one in which every hyperedge contains at least two vertices of distinct colors. Thus an empty or singleton obstruction makes proper coloring impossible.

Let `\chi(H_B)` be the minimum number of colors when a weak proper coloring exists, and:

```math
\boxed{\chi(H_B)=+\infty}
```

otherwise. Adopt:

```math
\left\lceil\log_2(+\infty)\right\rceil:=+\infty.
```

### 13.2 Operational safety lemma

Under M4–M7, an encoder is operationally safe iff every nonempty encoder cell lies in `\Phi_B(G;i_0)`.

#### Proof

If one decoder safely handles every used message, each message-conditioned branch supplies a system-realizable frontier witness for its corresponding cell, so every cell lies in `\Phi_B`.

Conversely, if every cell lies in `\Phi_B`, choose one realization witness per finite cell. M7 guarantees that these individually system-realizable witnesses compose into one non-oracular message-conditioned decoder without altering their success/budget judgments. Therefore the encoder is operationally safe. `\square`

### 13.3 Coloring lemma

Under M1–M7, an encoder is operationally safe iff its used message labels form a weak proper coloring of `H_B`.

#### Proof

By the operational safety lemma, safety is equivalent to every cell lying in the downward-closed family `\Phi_B`.

If a minimal obstruction were monochromatic, it would lie inside one feasible cell, contradicting downward closure.

Conversely, if some cell were infeasible, P4a supplies a minimal obstruction contained in that cell, which would be monochromatic. `\square`

If `H_B` contains an empty or singleton obstruction, no weak proper coloring exists. By downward closure, the corresponding infeasibility also prevents any operationally safe encoder. Both minima are `+\infty`.

### 13.4 Theorem P4b

Under M1–M7 and the extended-value convention:

```math
\boxed{M_B^*=\chi(H_B)}
```

and:

```math
\boxed{
m_B^*=\left\lceil\log_2\chi(H_B)\right\rceil.
}
```

#### Proof

When safe encoders exist, the coloring lemma equates operationally safe message partitions with weak proper colorings, so minimizing message cells equals minimizing colors. When no safe encoder exists, both minima equal `+\infty` by the proved equivalence and explicit convention. Fixed-width bit cost then gives the second identity. `\square`

### Standing

```text
A1M: REPAIRED by explicit +∞ convention.
P4b: PROVED under M1–M7, including explicit decoder composability.
```

This remains an assumption-scoped memory theorem, not a universal statement about memory or decoder realizability.

---

## 14. Audit

The audited repair must satisfy all checks below.

### Oracle boundary

```text
PASS  hidden x is not a realization input
PASS  analyst-only S is not a realization input
PASS  hidden G affects realization only through i_Π(G)
PASS  uncontrolled lucky constructor outcomes are not existentially credited
PASS  future online learning is not pre-credited to assay-time Avail
PASS  residualization does not invoke a fresh constructor
PASS  P4b decoder selection receives only declared message m, not hidden x/S
```

### Resource boundary

```text
PASS  measured realization cost is charged
PASS  pre-assay realization cost may be sunk only when explicitly declared
PASS  post-realization state G^δ preserves realization-caused state changes
PASS  charged prefix debt is retained pathwise
PASS  residualization does not double-charge realization
PASS  A1P3 isolates policy-space sensitivity with explicitly zero realization cost in both arms
```

### Jurisdiction boundary

```text
PASS  residual response jurisdiction is exact restriction equality
PASS  no adversarial powers are added
PASS  no original response continuations are removed
```

### Theorem-domain boundary

```text
PASS  P4b no longer assumes singleton feasibility
PASS  infeasible encoder/coloring cases map to +∞
PASS  P4b explicitly states decoder composability as M7
PASS  failure of M7 invalidates the ordinary χ theorem rather than being silently treated as kernel failure
```

### Claim ceiling

```text
PASS  A1P3 is semantic sensitivity, not learning evidence
PASS  no feedback-to-Π causal result is claimed
PASS  no frontier-to-viability implication is claimed
PASS  no viability-to-frontier-preservation implication is claimed
PASS  no new MATRIX kernel object or scalar is introduced
```

---

## 15. Re-run of Attack 1 obligations

Under the audited definitions:

```text
A1R   exact residual-response jurisdiction
      REPAIRED

A1M   infeasible encoder/coloring convention
      REPAIRED

A1P1  constructor-information factorization
      PROVED

A1P2  realization cost
      CLOSED UNDER EXPLICIT CHARGING CONVENTION

A1P3  Π-sensitive frontier under fixed U
      PROVED AS FINITE SEMANTIC SENSITIVITY WITNESS
      NOT LEARNING EVIDENCE

A1P4  residual transport of earned realization
      PROVED UNDER RESIDUAL-TRANSPORT CONTRACT

P1    downward closure
      PROVED under system-relative realization

P3a   same-realized-policy suffix viability
      PROVED under A1R extension consequence + additive charged cost

P3b   faithful information-conditioned residualization
      PROVED under repaired A1R + A1P latent-state contract

P4a   finite minimal-obstruction representation
      PROVED for finite Ω once P1 holds

P4b   hypergraph coloring / memory characterization
      PROVED under M1–M7 with +∞ extended values
```

---

## 16. Attack 1 standing

Under the declared, assumption-scoped `EXEC_V1` contract:

```math
\boxed{
\mathrm{MATRIX}_0
\text{ survives Attack 1 under system-relative, closed-loop semantics.}
}
```

This means only that the hostile closed-loop/adversarial construction, hidden resource-history challenge, residual-jurisdiction challenge, and policy-realization oracle challenge are representable using existing MATRIX roles after explicit contract repair.

It does **not** establish universal correctness, empirical validity, general corrigibility, or that feedback actually improves policy machinery.

The attack-local result is:

```math
\boxed{
\textbf{MATRIX measures policies the system can realize, not policies the analyst can imagine.}
}
```

and:

```math
\boxed{
\textbf{hidden from policy does not mean absent from execution semantics.}
}
```

No MATRIX₁ is earned.

No new frontier object is introduced.

No new scalar is introduced.

No README theory change is implied.

---

## 17. Reopening conditions

Attack 1 should be reopened only by a concrete failure witness against an explicit contract or proof, for example:

```text
- equal i_Π, Π, and U but different realizable-policy sets caused only by hidden state leakage;
- required online realization that cannot be represented inside declared execution semantics without oracle access;
- a residual continuation violating exact A1R restriction equality;
- non-additive resource semantics that invalidate P3a/P3b accounting;
- a residualization counterexample where earned realization cannot be transported without capability re-granting;
- a P4b counterexample while retaining M1–M7 and the extended-value convention.
```

Any such result must first be localized to information boundary, resource contract, response jurisdiction, theorem domain, or kernel before conceptual revision is authorized.