# EXEC_V1 — System-relative closed-loop execution semantics

**Status:** repaired Attack 1 formalization for MATRIX₀.

> **This document repairs the execution contract exposed by review of `EXEC_V0`. It does not modify the MATRIX conceptual kernel.**

Repository pre-state for this artifact:

```text
main = 121f71090a01b6d049fadb2596172cff8aad3896
```

`formalization/EXEC_V0.md` is intentionally preserved as the historical artifact that exposed the contract gaps. The README is intentionally unchanged.

The repaired semantics close three local defects:

```text
A1R  exact residual-response jurisdiction
A1M  extended-value treatment of infeasible memory/coloring cases
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

The central four-way distinction is:

```math
\boxed{
\text{policy exists}
\neq
\text{policy is realizable}
\neq
\text{policy succeeds}
\neq
\text{policy is affordable}
}
```

---

## 1. Scope and claim ceiling

This artifact tests whether the existing MATRIX roles are sufficient for robust closed-loop correction once policy availability is made system-relative.

It does **not** claim:

```text
- that feedback empirically improves policy machinery;
- that every real system satisfies the declared realization contract;
- that semantic frontier sensitivity is evidence of learning;
- that frontier expansion implies future-viability gain;
- that future-viability gain implies frontier preservation;
- a general theory of intelligence or corrigibility;
- empirical validation of MATRIX.
```

The corrective-frontier pathway remains:

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

and

```math
\boxed{
C_{\mathrm{improve}}>0
\not\Rightarrow
\left(\Delta_B^+\neq\varnothing\land\Delta_B^-=\varnothing\right)
}
```

with the especially important consequence:

```math
\boxed{C_{\mathrm{improve}}>0\not\Rightarrow\Delta_B^-=\varnothing.}
```

No result below turns either causal observable into a definition of the other.

---

## 2. Existing execution roles

Let:

```math
x\in\Omega
```

be the latent episode state.

Let:

```math
G_t
```

be the complete mutable execution state at interaction step `t`.

`G_t` may contain future-relevant hidden distinctions such as environment state, instrument state, adversarial memory, realized-policy state, or resource debt.

The policy receives only its declared visible history:

```math
h_t=(q_0,o_0,\ldots,q_{t-1},o_{t-1}).
```

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

Let `\mathcal U` be the declared primitive executable affordances. Every executable policy is typed by `\mathcal U`.

Let `R` be the declared valid-repair relation, `c` the declared resource model, `B` the corrective budget, and `\mathcal R` the declared environment-response jurisdiction.

---

## 3. Constructor-visible information

Policy realization has its own information boundary.

Define the constructor-visible projection:

```math
\boxed{i_\Pi:G\rightarrow I_\Pi.}
```

For an initial system state `G`, write:

```math
i_0=i_\Pi(G).
```

`i_0` may include information legitimately available to the realization machinery, such as:

```text
- persistent learned state readable by Π;
- a retained representation message;
- declared task information;
- compiler or selection state;
- other explicitly exposed realization inputs.
```

By default it does **not** include:

```math
x
```

and it does **not** include an analyst-only description of the tested uncertainty set `S`.

If a task description is genuinely supplied to the system, it may be part of `i_0`; the requirement is that it cross a declared interface rather than appear because the analyst knows it.

### 3.1 Temporal boundary

Availability is evaluated at the declared realization point from the system's assay-time realization machinery and constructor-visible information.

```math
\boxed{\text{realizable now}\neq\text{may become realizable later}.}
```

Capabilities acquired through observations after assay start are not credited to initial availability in advance.

If online synthesis uses observations gathered during correction, that synthesis is represented inside the executable process, with its observations, state transitions, and charged costs represented explicitly. It is not retroactively inserted into the initial available-policy set.

---

## 4. Policy realization relation

Let `\mathcal P_{\mathcal U}` be the policies executable through the declared primitive affordances `\mathcal U`.

Define the realization relation:

```math
\boxed{
\mathfrak{Real}_{\Pi,\mathcal U}(i)
\subseteq
\Delta\times\mathcal P_{\mathcal U}.
}
```

A pair

```math
(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i)
```

means that `\delta` is a valid realization provenance by which the system's own policy machinery can construct or select executable policy `\pi` from `\Pi`, `\mathcal U`, and constructor-visible information `i`.

Write:

```math
\boxed{\delta\xRightarrow[\Pi,\mathcal U,i]{}\pi.}
```

Define the available policy set as the policy projection:

```math
\boxed{
\mathrm{Avail}(\Pi,\mathcal U;i)
=
\left\{
\pi:\exists\delta,\;(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i)
\right\}.
}
```

When older notation mentions full state `G`, it is shorthand for factorization through the visible projection:

```math
\boxed{
\mathrm{Avail}(G,\Pi,\mathcal U;i_\Pi(G))
:=
\mathrm{Avail}(\Pi,\mathcal U;i_\Pi(G)).
}
```

The full `G` is not an undeclared constructor input.

### 4.1 No realization-by-environment-query loophole

A pre-execution realization derivation may inspect `i_0` and the specification of `\mathcal U`; it may not interact with hidden episode state and still call that interaction realization.

Any interaction capable of revealing `x` belongs to executable episode semantics.

Therefore:

```math
\boxed{
\text{interaction that can reveal }x
\Rightarrow
\text{episode execution, not hidden pre-policy realization}.
}
```

### 4.2 Controlled realization convention

The existential `\exists\delta` does not credit a merely lucky uncontrolled constructor outcome.

For `EXEC_V1`, membership in `\mathfrak{Real}` means the realization branch is deliberately reachable/selectable by the declared system machinery from `(\Pi,\mathcal U,i)`.

If future work admits stochastic or adversarial realization outcomes, their probability or robustness quantifiers must be declared separately. They are not silently existentially credited here.

---

## 5. A1P1 — constructor-information factorization

### Contract

For fixed realization machinery and primitive affordances:

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

Taking policy projections yields:

```math
\boxed{
\mathrm{Avail}(\Pi_1,\mathcal U_1;i_\Pi(G_1))
=
\mathrm{Avail}(\Pi_2,\mathcal U_2;i_\Pi(G_2)).
}
```

### Proof

By definition, `\mathfrak{Real}` is indexed only by `(\Pi,\mathcal U,i)`.

Hidden `x`, analyst set `S`, and components of `G` outside `i_\Pi(G)` are not arguments to the realization relation.

Equal `(\Pi,\mathcal U,i)` therefore induces the same realization pairs `(\delta,\pi)`, and hence the same policy projection. `\square`

### Standing

```text
A1P1: PROVED BY FACTORIZATION / NONINTERFERENCE CONTRACT.
```

The symmetry with execution is deliberate:

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

Hidden distinctions may affect world dynamics, repair validity, admissibility, or cost. They may not secretly steer constructor or policy choice.

---

## 6. A1P2 — realization cost and post-realization state

A realization witness `\delta` may have a derived resource cost:

```math
C_{\mathrm{real}}(\delta).
```

This is not a new kernel primitive. It is the portion of the already-declared resource model `c` attributable to realization/selection.

There are two admissible assay conventions.

### 6.1 In-scope realization

If realization occurs after the measured assay begins, charge:

```math
\boxed{
C_{\mathrm{charged}}
=
C_{\mathrm{real}}(\delta)
+
C_{\mathrm{exec}}.
}
```

If realization changes persistent machinery or consumes resources that affect later execution, let:

```math
G^\delta
```

be the resulting post-realization execution state. Episode execution begins from `G^\delta`.

### 6.2 Pre-realized policy

If policy realization genuinely occurred before assay start, the realization cost is explicitly sunk for that assay and the realized policy state/provenance must already be present in the initial system state.

Then:

```math
\boxed{C_{\mathrm{charged}}=C_{\mathrm{exec}}.}
```

Any selection or construction work performed after assay start remains charged.

### Standing

```text
A1P2: CLOSED UNDER AN EXPLICIT CHARGING CONVENTION.
```

There is no admissible third case in which measured realization occurs but its cost silently disappears.

---

## 7. Closed-loop execution

For a realized policy `\pi`, latent state `x`, initial execution state `G^\delta`, and admissible response strategy `\rho`, define:

```math
\mathrm{Exec}(\pi,x;G^\delta,\rho)
```

as the complete recursively generated closed-loop execution until valid repair or failure.

At each nonterminal step:

```math
q_t=\pi(h_t),
```

and the environment transition may depend on hidden execution state while returning only the declared observation to the policy.

Terminal success is evaluated by the declared repair relation `R`.

Illegal execution, invalid terminal repair, or nontermination is failure under the zero-error frontier.

Pathwise execution cost is additive under this artifact's Attack 1 contract.

---

## 8. System-relative corrective frontier

Fix all assay contracts other than the realization witness, including `\Omega`, `\Pi`, `\mathcal U`, `R`, `c`, `B`, `\mathcal R`, and constructor-visible initial information `i_0`.

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

For pre-realized policy assays, the realization cost term is sunk according to Section 6.2 and the initial execution state is the already-realized state.

The crucial quantifier order is:

```math
\boxed{
\exists(\delta,\pi)
\;\forall x
\;\forall\rho.
}
```

It is not:

```math
\forall x\;\exists(\delta,\pi),
```

and the tested uncertainty set `S` is not supplied as a hidden constructor input.

The repaired replacement is therefore:

```math
\boxed{
\exists\pi
\quad\longrightarrow\quad
\exists(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i_\Pi(G)).
}
```

This makes `\Phi_B` system-relative rather than oracle-relative.

---

## 9. A1P3 — semantic sensitivity to policy machinery under fixed primitives

A1P3 asks whether the repaired frontier can change when policy machinery changes even though primitive affordances remain fixed.

### Construction

Let:

```math
\Omega=\{0,1\}.
```

Hold primitive affordances fixed:

```math
\boxed{
\mathcal U^+=\mathcal U^- = \{q,r_0,r_1\}.
}
```

The diagnostic action `q` returns the latent bit. Terminal repair `r_i` is valid exactly when `x=i`.

Let:

```math
c(q)=1,
\qquad
c(r_i)=1,
\qquad
B=2.
```

Use a trivial response jurisdiction for this witness.

Take pre-realized policy sets so realization cost is explicitly sunk in both arms.

In the untreated system:

```math
\mathrm{Avail}^-=\{\pi_0,\pi_1\},
```

where `\pi_i` immediately performs repair `r_i`.

No available untreated policy uses `q` and then branches on its result.

Therefore:

```math
\boxed{\{0,1\}\notin\Phi_B^-.}
```

Now change only policy machinery so that:

```math
\Pi^+\neq\Pi^-,
```

while preserving every declared primitive affordance.

Let the treated system additionally realize:

```math
\pi^\star:
q
\rightarrow
\begin{cases}
r_0,&o=0,\\
r_1,&o=1.
\end{cases}
```

Then:

```math
\boxed{
\mathrm{Avail}^+
=
\mathrm{Avail}^-\cup\{\pi^\star\}.
}
```

For either latent state, `\pi^\star` succeeds at total execution cost `2=B`.

Hence:

```math
\boxed{\{0,1\}\in\Phi_B^+.}
```

Every untreated realization witness remains available in the treated arm, so:

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

This proves only that the repaired formalism can represent a `\Pi`-mediated frontier expansion under fixed primitives.

It is **not** evidence that feedback changes `\Pi`, `Q`, `g`, `\mathrm{Avail}`, or `\Phi_B` in any actual system.

---

## 10. Reachable prefixes

Fix a frontier witness `(\delta,\pi)` for some `S\in\Phi_B(G;i_0)`.

A full reachable execution prefix `\tau` records enough verifier-visible state to reconstruct the latent episode state, mutable execution state, realized policy/provenance state, environment-response state required by the declared jurisdiction, visible history, and charged path debt.

Let:

```math
h(\tau)
```

be the policy-visible projection.

For a reachable visible history `h`, define:

```math
\boxed{
\mathcal K(h)
=
\{\tau:\tau\text{ is reachable under the fixed realized witness }(\delta,\pi),\;h(\tau)=h\}.
}
```

Multiple prefixes in `\mathcal K(h)` may have different hidden execution states, adversarial memory, and charged resource debt.

The policy may not select among them.

The canonical residual domain:

```math
\boxed{\Omega^h=\mathcal K(h)}
```

is an encoding construction, not an ontological claim.

---

## 11. A1R — exact residual-response jurisdiction

For an original admissible response strategy `\rho` that realizes prefix `\tau`, let:

```math
\mathrm{Res}_\tau(\rho)
```

be its complete continuation strategy after `\tau`, including any response-strategy memory needed to preserve future admissibility.

Define the residual response jurisdiction by equality:

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

This exact equality provides both directions:

```text
- no residual response power is added;
- no original continuation power is silently removed.
```

The weaker one-way splice condition is sufficient for P3a, but full equality is required for faithful P3b residualization.

### Standing

```text
A1R: REPAIRED BY EXACT RESTRICTION EQUALITY.
```

---

## 12. P1 — downward closure under system-relative realization

### Theorem P1

If:

```math
S\in\Phi_B(G;i_0)
```

and:

```math
S'\subseteq S,
```

then:

```math
\boxed{S'\in\Phi_B(G;i_0).}
```

### Proof

Let `(\delta,\pi)` witness `S\in\Phi_B(G;i_0)`.

The realization relation is independent of analyst set `S`, so the same `(\delta,\pi)` remains realizable when the verifier restricts attention to `S'`.

For every `x\in S'`, we also have `x\in S`. Therefore the same realized policy succeeds within the same charged budget against every admissible response because it already does so for every `x\in S`.

Thus `(\delta,\pi)` witnesses `S'\in\Phi_B(G;i_0)`. `\square`

### Standing

```text
P1: PROVED under system-relative realization and restriction-monotone feasibility.
```

Finiteness of `\Omega` is not required.

---

## 13. P3a — same-realized-policy suffix viability

For visible prefix `h`, define:

```math
\boxed{
\pi|_h(\bar h)=\pi(h\mathbin{\|}\bar h).
}
```

Let `D(\tau)` be the total charged debt already incurred by prefix `\tau`, including any in-scope realization cost paid before the prefix. Pre-assay sunk realization cost is not included because it is outside the assay budget by declaration.

### Theorem P3a

Assume:

```text
A1. (δ,π) witnesses S ∈ Φ_B(G;i_0).
A2. Residual responses satisfy the one-way extension consequence of A1R.
A3. Charged pathwise cost is additive across realized prefix and continuation.
```

Then for every reachable visible history `h`, every compatible prefix `\tau\in\mathcal K(h)`, and every residual continuation `\rho'\in\mathcal R_h(\tau)`, the same already-realized suffix policy `\pi|_h` succeeds and:

```math
\boxed{
D(\tau)
+
C_{\mathrm{suffix}}(\pi|_h,\tau,\rho')
\le B.
}
```

### Proof

Fix arbitrary `h`, `\tau`, and `\rho'`.

By A1R, `\rho'` is the restriction of some globally admissible original response strategy whose execution realizes `\tau`.

Because `(\delta,\pi)` globally witnesses frontier membership, the complete execution against that original response succeeds and has total charged cost at most `B`.

After visible history `h`, deterministic behavior is exactly `\pi|_h`. The residual continuation is therefore the suffix of that globally valid execution.

Success is inherited, and additive charged accounting gives the displayed budget inequality. `\square`

### Standing

```text
P3a: PROVED under A1–A3 after system-relative realization repair.
```

---

## 14. A1P4 and P3b — residualization transports earned realization

The residual construction must not obtain a fresh unrestricted realization grant merely because the analyst has changed mathematical viewpoint.

### 14.1 Transport rule

The global witness `(\delta,\pi)` has already realized policy state before the reachable prefix.

Residualization transports that earned state:

```math
\boxed{
(\delta,\pi,h)
\longmapsto
(\delta^h,\pi^h),
}
```

where:

```math
\pi^h(\bar h)=\pi(h\mathbin{\|}\bar h)
```

and `\delta^h` is a provenance transport witness saying that `\pi^h` is available because `\pi` was already realized by `\delta` before the prefix.

`\delta^h` is not a new synthesis event.

The residual constructor-visible state contains only the already-earned realized-policy state required to continue that policy. It does not contain hidden prefix identity merely because the verifier knows it.

### 14.2 No re-granting

The residual realization relation is restricted to continuations reachable from the transported realized-policy state. It is not evaluated as a fresh search over policies an analyst could describe after seeing `\mathcal K(h)`.

Therefore:

```math
\boxed{
\text{residualization transports an earned policy state; it does not recreate it.}
}
```

### 14.3 Residual latent domain and transition

Use:

```math
\boxed{\Omega^h=\mathcal K(h).}
```

A residual latent state `z=\tau` carries the actual future-relevant hidden execution state and charged prefix debt.

The residual transition delegates to the original continuation operator from the state carried by `z` while exposing only the common visible suffix history to `\pi^h`.

### 14.4 Residual cost

Keep the original total budget:

```math
\boxed{B^h=B.}
```

Define residual initial debit:

```math
\boxed{c^h_{\mathrm{init}}(z)=D(z).}
```

Subsequent costs delegate to the original continuation cost model.

Hence:

```math
\boxed{
C_h(z,\rho')
=
D(z)+C_{\mathrm{suffix}}(z,\rho').
}
```

No realization cost is charged twice.

### 14.5 Trace and success preservation

For every `z=\tau\in\Omega^h` and every `\rho'\in\mathcal R_h(\tau)`, the residual execution under transported policy `\pi^h` has exactly the same action/observation continuation, hidden continuation dynamics, terminal repair judgment, and charged total as the original suffix from `\tau`.

This follows inductively because:

```text
- the residual policy is the original suffix policy;
- A1R gives exactly the original residual response jurisdiction;
- the residual transition delegates to the actual original continuation state;
- charged prefix debt is retained exactly;
- no new realization event occurs.
```

Therefore:

```math
\boxed{
\mathrm{Success}_{h}(z,\rho')
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

### Theorem P3b

Under the latent-complete execution contract, constructor-information factorization, A1R exact response restriction, additive charged pathwise accounting, and the transport rule above, every reachable information-conditioned residual game for a fixed realized frontier witness admits a faithful instance of the same MATRIX execution roles.

The construction does not reveal latent prefix identity to the policy and does not erase distinctions still used by dynamics or accounting.

### Standing

```text
A1P4: PROVED under the residual-transport contract.
P3b:  PROVED under the repaired A1R + A1P execution contract.
```

The canonical residual domain remains a proof encoding, not an ontology.

---

## 15. P4a — finite minimal-obstruction representation

Assume from here that `\Omega` is finite.

Define:

```math
\boxed{
H_B(G;i_0)
=
\mathrm{Min}\left(2^\Omega\setminus\Phi_B(G;i_0)\right),
}
```

where `\mathrm{Min}` means inclusion-minimal elements.

### Theorem P4a

For finite `\Omega` and downward-closed `\Phi_B(G;i_0)`:

```math
\boxed{
S\in\Phi_B(G;i_0)
\iff
\nexists H\in H_B(G;i_0)\text{ with }H\subseteq S.
}
```

### Proof

If `S` is feasible and contains excluded `H`, downward closure would make `H` feasible, contradiction.

Conversely, if `S` is infeasible, the finite family of excluded subsets of `S` has an inclusion-minimal member `H`; then `H\in H_B` and `H\subseteq S`. `\square`

### Standing

```text
P4a: PROVED for finite Ω after the system-relative P1 repair.
```

---

## 16. A1M and P4b — infeasible memory/coloring cases

P4b remains scoped to the finite deterministic partition-memory model.

Assume:

```text
M1. Ω is finite and nonempty.
M2. A retained representation is a deterministic encoder g: Ω → M.
M3. Arbitrary encoder-induced partitions are admissible.
M4. The decoder receives retained message m and may use the declared future execution machinery.
M5. Safety means every nonempty encoder cell lies in Φ_B(G;i_0).
M6. Memory cost counts used message symbols; fixed-width binary memory costs ceil(log2 |M_used|) bits. Encoder/decoder program complexity is not charged as instance-specific retained memory in this theorem.
```

Define:

```math
M_B^*
```

as the minimum number of nonempty message cells among safe encoders if one exists, and:

```math
\boxed{M_B^*=+\infty}
```

otherwise.

Define:

```math
m_B^*
```

as the corresponding minimum fixed-width retained bits, with:

```math
\boxed{m_B^*=+\infty}
```

when no safe encoder exists.

Treat `H_B` as a hypergraph on vertex set `\Omega`.

A weak proper coloring is a coloring for which every hyperedge contains at least two vertices of distinct colors. Thus an empty or singleton obstruction makes proper coloring impossible.

Define:

```math
\chi(H_B)
```

as the minimum number of colors in a weak proper coloring when one exists, and:

```math
\boxed{\chi(H_B)=+\infty}
```

when none exists.

Adopt:

```math
\left\lceil\log_2(+\infty)\right\rceil:=+\infty.
```

### Lemma — safe encoders and proper colorings

A deterministic encoder is safe iff its used message labels define a weak proper coloring of `H_B`.

#### Proof

If an encoder is safe and some minimal obstruction `H\in H_B` were monochromatic, `H` would lie inside one safe cell. Downward closure would then make `H` feasible, contradiction.

Conversely, if a coloring has no monochromatic obstruction but some encoder cell were infeasible, P4a supplies an `H\in H_B` contained in that cell. Every vertex of `H` would share the cell's message label, contradiction.

If `H_B` contains an empty or singleton obstruction, no weak proper coloring exists and no safe encoder can exist: every encoder has a nonempty cell containing the affected singleton, while an empty obstruction already certifies the frontier has no feasible subset. Both minima are therefore `+\infty`. `\square`

### Theorem P4b

Under M1–M6 and the extended-value convention:

```math
\boxed{M_B^*=\chi(H_B)}
```

and:

```math
\boxed{
m_B^*=\left\lceil\log_2\chi(H_B)\right\rceil.
}
```

### Proof

When a safe encoder exists, the lemma gives a bijection at the level of feasible message-cell partitions and weak proper colorings, so minimizing used messages equals minimizing colors.

When no safe encoder exists, the lemma gives no weak proper coloring; both quantities equal `+\infty` by definition.

The fixed-width bit identity follows from the declared storage model and the extended convention. `\square`

### Standing

```text
A1M: REPAIRED by explicit +∞ convention.
P4b: PROVED under M1–M6 with extended values.
```

This is not a universal theorem about memory.

---

## 17. Audit of the repaired contract

The repair is accepted only if the following checks hold simultaneously.

### 17.1 Oracle checks

```text
PASS  hidden x is not a realization input;
PASS  analyst-only S is not a realization input;
PASS  full hidden G affects realization only through i_Π(G);
PASS  uncontrolled lucky constructor outcomes are not existentially credited;
PASS  future online learning is not pre-credited to assay-time Avail;
PASS  residualization does not invoke a fresh policy constructor.
```

### 17.2 Resource checks

```text
PASS  measured realization cost is charged;
PASS  pre-assay realization cost may be sunk only when explicitly declared;
PASS  realized-policy state changes caused by realization survive into G^δ;
PASS  charged prefix debt is preserved pathwise during residualization;
PASS  no realization cost is charged twice after residualization.
```

### 17.3 Jurisdiction checks

```text
PASS  residual response jurisdiction is exact restriction equality;
PASS  no adversarial response powers are added;
PASS  no original response continuations are silently removed.
```

### 17.4 Claim-ceiling checks

```text
PASS  A1P3 is semantic sensitivity, not learning evidence;
PASS  no feedback-to-Π causal result is claimed;
PASS  no frontier-to-viability implication is claimed;
PASS  no viability-to-frontier-preservation implication is claimed;
PASS  no new MATRIX kernel object is introduced.
```

---

## 18. Re-run of Attack 1 obligations

Under the repaired definitions:

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
      PROVED under exact/one-way splice consequence + additive charged cost

P3b   faithful information-conditioned residualization
      PROVED under repaired A1R + A1P latent-state contract

P4a   finite minimal-obstruction representation
      PROVED for finite Ω once P1 holds

P4b   hypergraph coloring / memory characterization
      PROVED under M1–M6 with +∞ extended values
```

---

## 19. Attack 1 standing

The repaired formalization supports the attack-local statement:

```math
\boxed{
\mathrm{MATRIX}_0
\text{ survives Attack 1 under the declared system-relative, closed-loop EXEC_V1 semantics.}
}
```

This means only that the hostile closed-loop/adversarial construction and the policy-realization oracle challenge have been representable using existing MATRIX roles after explicit contract repair.

It does **not** establish universal correctness of MATRIX, empirical validity, general corrigibility, or that feedback actually improves policy machinery.

The result is narrower:

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

No MATRIX₁ is earned by Attack 1.

No new frontier object is introduced.

No new scalar is introduced.

No README theory change is implied.

---

## 20. Conditions that would reopen Attack 1

Attack 1 should be reopened only by a concrete failure witness against an explicit contract or proof, for example:

```text
- two states with equal i_Π, Π, and U but different realizable-policy sets caused only by hidden state leakage;
- a required online realization process that cannot be represented inside declared execution semantics without oracle access;
- a residual response continuation that violates the exact restriction equality;
- a path-dependent resource model for which additive charged accounting is false;
- a residualization counterexample showing that earned realization cannot be transported without capability re-granting;
- a P4b counterexample while retaining every assumption M1–M6 and the extended-value convention.
```

Any such result must first be localized to information boundary, resource contract, response jurisdiction, theorem domain, or kernel before conceptual revision is authorized.