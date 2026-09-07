# A2 selector-conflict search V0

**Standing:** POST-EXECUTION / DERIVED / NEGATIVE FORMAL RECORD.  
**Terminal result:** **NO WITNESS / STRUCTURALLY IMPOSSIBLE UNDER THE DECLARED CONTRACTS AND FROZEN A2 POLICY FAMILY.**  
**Source checkpoint:** `f5b5fa13e00f528e8d79d4c671a587365acc066d`.  
**Frozen implementation checkpoint:** `2b79c73dd9ac46fd6f693fd35d63c44cbb396a40`.

This record follows
[`CERTIFICATE_ACCESSIBILITY_V0.md`](CERTIFICATE_ACCESSIBILITY_V0.md) and
[`A2_CERTIFICATE_ACCESSIBILITY_OBSTRUCTION_V0.md`](A2_CERTIFICATE_ACCESSIBILITY_OBSTRUCTION_V0.md).
It asks whether the already executed A2-V1 factorial contains a clean
information-limited selector conflict: two systems with the same
constructor-visible terminal state, each with at least one compatible policy,
but with disjoint compatible-policy sets.

No learner is rerun. No policy implementation is changed. No prospective
execution, assay, endpoint, or preregistration change occurs. The three
deployment contracts below were fixed for this read-only spike before
inspecting the selector-conflict outcome; that local ordering does **not**
make this a preregistered experiment.

The distinction governing the record is

\[
\boxed{\text{no witness found}\neq\text{witness structurally impossible}.}
\]

The exhaustive census finds zero witnesses, but the scientific authority for
the stronger negative is the structural proof in Sections 2--4.

## 1. Frozen inputs and search target

The A2 terminal constructor boundary is

\[
\sigma(i_\Pi(G))=(\texttt{SWITCHBOARD\_3},a),
\]

where \(a\) is the final active hypothesis. The frozen policy realization
machinery exposes exactly nine policies:

\[
\operatorname{Avail}_9(a)
=
\{\pi_0,\ldots,\pi_7,\pi_a\}.
\]

For \(y\in\Omega\), \(\pi_y\) is the immediate repair policy whose success set
is the singleton \(\{y\}\). The policy \(\pi_a\) is the active diagnostic
policy. Against retained candidate \(h\), its success set is

\[
\operatorname{Succ}_h(\pi_a)
=
\operatorname{Fix}(T_a^{-1}T_h).
\]

For final survivor set \(L\), retain the already defined certificate

\[
\operatorname{Cert}(a,L)
=
\bigl(K(a,L),J(a,L),P(a,L)\bigr),
\]

with

\[
K(a,L)
=
\bigcap_{h\in L}
\operatorname{Fix}(T_a^{-1}T_h),
\]

\[
J(a,L)
=
\bigcap_{h\in L}
\left(F_a(h)\setminus F_0(h)\right),
\]

and

\[
P(a,L)
=
\left[\forall h\in L,\;F_0(h)\subseteq F_a(h)\right].
\]

For a deployment contract \(Q\), write \(\mathcal C_Q(u)\) for the frozen A2
policies that satisfy \(Q\) for terminal unit \(u\), uniformly over the
relevant uncertainty set and every retained candidate \(h\in L\), within the
frozen A2 budget.

The target witness is

\[
\boxed{
\begin{aligned}
\sigma(i_\Pi(G_1))&=\sigma(i_\Pi(G_2)),\\
\mathcal C_Q(G_1)&\neq\varnothing,\\
\mathcal C_Q(G_2)&\neq\varnothing,\\
\mathcal C_Q(G_1)\cap\mathcal C_Q(G_2)&=\varnothing.
\end{aligned}
}
\]

Such a pair would isolate a policy-choice obstruction: both hidden situations
would admit a contract-compatible action, while the shared visible state
would not identify which action is compatible.

### Declared contract family

The search uses exactly three nonvacuous contracts.

1. **Common-gain contract \(Q_J\).** A policy must realize at least one
   nonempty \(S\in J(a,L)\) uniformly over every retained candidate.

2. **Guaranteed-set contract \(Q_K\).** When \(|K(a,L)|\ge2\), a policy must
   realize the whole uncertainty set \(K(a,L)\) uniformly over every retained
   candidate. Rows with \(|K|<2\) have no \(Q_K\) target.

3. **Preserved-common-gain contract \(Q_{J+P}\).** A policy must satisfy
   \(Q_J\) and the certificate must also have \(P(a,L)=\mathsf{true}\).

No fourth contract is introduced after seeing the result.

### Custody bindings

The read-only pass used the repository-resident A2-V1 scientific archive and
reproduced its canonical identities:

| Object | SHA-256 |
|---|---|
| sealed A2-V1 scientific tarball | `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7` |
| A2-V1 primary | `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076` |
| A2-V1 raw evidence | `6e3188b33a2640133cbdd4b9d91b48513cbd2dfc80c96c21efb561932961c1d1` |

The frozen source identities controlling the constructor and policy boundary
are:

| File | Frozen blob |
|---|---|
| `experiments/a2_v1/implementation/a2_v1/engine.py` | `1d6136461e5012f105957f9a7c22a6eadbdc5a5f` |
| `experiments/a2_v1/implementation/a2_v1/frozen_model.py` | `bd40559ca43d5f0ccb7c7e225e51494c74a5d292` |
| `experiments/a2_v1/implementation/a2_v1/authorities.py` | `30a069f4a0da77f8071cc20205d99ec1f32dcb71` |
| frozen original A2 model | `f3aab0759b994aa06e961c62e7dfc27e8573fcf3` |

These bindings establish source and record identity. They are not a new
prospective result.

## 2. Structural lemma: common gains have no immediate-policy witness

Under the frozen A2 frontier semantics, every baseline frontier contains the
empty set and all singletons. Therefore, for every candidate \(h\),

\[
S\in F_a(h)\setminus F_0(h)
\quad\Longrightarrow\quad
|S|\ge2.
\]

Consequently,

\[
S\in J(a,L)
\quad\Longrightarrow\quad
|S|\ge2.
\]

Every immediate policy \(\pi_y\) succeeds on only one latent state. Hence no
immediate policy can realize a target \(S\in J(a,L)\).

By definition of \(J\), however, every \(S\in J(a,L)\) belongs to \(F_a(h)\)
for every retained \(h\in L\). The active diagnostic \(\pi_a\) therefore
succeeds uniformly on every such common gain.

Thus

\[
\boxed{
J(a,L)\neq\varnothing
\Longrightarrow
\mathcal C_{Q_J}(u)=\{\pi_a\}.
}
\]

Adding the preservation predicate changes feasibility but does not create a
second compatible policy:

\[
\boxed{
J(a,L)\neq\varnothing
\land P(a,L)
\Longrightarrow
\mathcal C_{Q_{J+P}}(u)=\{\pi_a\}.
}
\]

If either antecedent fails, the corresponding compatible set is empty.

## 3. Structural lemma: the guaranteed multi-state set has the same unique policy

By definition,

\[
K(a,L)
=
\bigcap_{h\in L}\operatorname{Succ}_h(\pi_a).
\]

Hence \(\pi_a\) succeeds on every state of \(K(a,L)\) for every retained
candidate. Under \(Q_K\), the target is admitted only when \(|K|\ge2\).

Again, every immediate policy succeeds on one state only. Therefore

\[
\boxed{
|K(a,L)|\ge2
\Longrightarrow
\mathcal C_{Q_K}(u)=\{\pi_a\}.
}
\]

Rows with \(|K|<2\) have no nonvacuous \(Q_K\) target and therefore
\(\mathcal C_{Q_K}(u)=\varnothing\).

Combining Sections 2 and 3 gives, for every searched contract,

\[
\boxed{
Q\in\{Q_J,Q_K,Q_{J+P}\}
\Longrightarrow
\mathcal C_Q(u)\in\{\varnothing,\{\pi_a\}\}.
}
\]

## 4. Same visible state makes a nonempty/disjoint conflict impossible

Take two A2 terminal systems with the same constructor-visible state:

\[
\sigma(i_\Pi(G_1))
=
\sigma(i_\Pi(G_2)).
\]

Because the task tag is constant, equality of the visible state implies equal
active hypothesis:

\[
a_1=a_2=a.
\]

The frozen constructor therefore realizes the same active diagnostic policy
\(\pi_a\) in both systems.

For any searched contract \(Q\), if both compatible sets are nonempty, the
structural lemmas force

\[
\mathcal C_Q(G_1)
=
\{\pi_a\}
=
\mathcal C_Q(G_2).
\]

Therefore

\[
\boxed{
\mathcal C_Q(G_1)\neq\varnothing
\land
\mathcal C_Q(G_2)\neq\varnothing
\Longrightarrow
\mathcal C_Q(G_1)\cap\mathcal C_Q(G_2)
=
\{\pi_a\}\neq\varnothing.
}
\]

So the target condition

\[
\mathcal C_Q(G_1)\neq\varnothing,\quad
\mathcal C_Q(G_2)\neq\varnothing,\quad
\mathcal C_Q(G_1)\cap\mathcal C_Q(G_2)=\varnothing
\]

is structurally impossible under the three declared contracts and the frozen
nine-policy A2 topology.

This is stronger than an empirical zero count, but only within the stated
contract and policy-family scope.

## 5. Exhaustive sealed-record verification

The read-only verification independently reconstructed the final treatment
survivor set \(L\), visible active hypothesis \(a\), and certificate
\((K,J,P)\) for all 9,216 already executed A2-V1 factorial rows. It performed
zero learner reruns and zero prospective executions.

As an extraction cross-check, the already archived ambiguity census was
reproduced:

\[
\boxed{
45/45
\text{ represented prospective visible states are certificate-ambiguous}
}
\]

and

\[
\boxed{
45/48
\text{ active states across the complete factorial are certificate-ambiguous}.
}
\]

Certificate ambiguity therefore remains real even though the selector
conflict below is impossible.

### Prospective V1 stratum

| Contract | Rows with nonempty \(\mathcal C_Q\) | Same-visible nonempty pairs checked | Nonempty/disjoint conflicts |
|---|---:|---:|---:|
| \(Q_J\) | 4,848 | 303,672 | **0** |
| \(Q_K\) | 4,848 | 303,672 | **0** |
| \(Q_{J+P}\) | 4,344 | 258,784 | **0** |

### Complete 9,216-row factorial

| Contract | Rows with nonempty \(\mathcal C_Q\) | Same-visible nonempty pairs checked | Nonempty/disjoint conflicts |
|---|---:|---:|---:|
| \(Q_J\) | 6,688 | 614,096 | **0** |
| \(Q_K\) | 6,880 | 632,432 | **0** |
| \(Q_{J+P}\) | 6,064 | 525,624 | **0** |

The finite search also checked the structural identity on every row:

\[
\boxed{
\mathcal C_Q(u)\neq\varnothing
\Longrightarrow
\mathcal C_Q(u)=\{\pi_{\operatorname{active}(u)}\}
}
\]

for each \(Q\in\{Q_J,Q_K,Q_{J+P}\}\).

The pair counts confirm the theorem on the complete sealed record. They are
not the basis for the impossibility claim.

### Deterministic reproduction procedure

The verification uses only sealed evidence plus the frozen finite algebra:

1. verify the scientific tarball, primary, and raw-evidence SHA-256 identities;
2. read every treatment terminal record and recover `(unit, stratum, active, final_live)`;
3. reconstruct the 48 frozen signed-coordinate-permutation hypothesis maps;
4. for each terminal `(a,L)`, compute \(K(a,L)\), \(J(a,L)\), and \(P(a,L)\);
5. derive \(\mathcal C_{Q_J}\), \(\mathcal C_{Q_K}\), and
   \(\mathcal C_{Q_{J+P}}\) from the frozen nine-policy success sets;
6. group nonempty rows by the exact visible state
   \((\texttt{SWITCHBOARD\_3},a)\);
7. enumerate every within-group pair and test the nonempty/disjoint condition.

No result field is used to choose a new contract during the search.

## 6. Interpretation: certificate ambiguity without policy-choice ambiguity

The earlier A2 record established that the same constructor-visible state can
hide different survivor sets and different certificates. That information
loss remains:

\[
\boxed{
\text{same visible state}
\not\Rightarrow
\text{same certificate}.
}
\]

It also established a hidden feasibility difference: one hidden system can
satisfy a nonvacuous gain contract while another with the same visible state
cannot.

The present negative localizes why this does not become a clean selector
conflict under the searched contracts. The frozen constructor exposes the
active hypothesis \(a\), and \(a\) already determines the only available
multi-state corrective policy relevant to these contracts.

Thus the frozen A2 topology has the form

\[
\text{different hidden certificates}
\longrightarrow
\text{same visible active }a
\longrightarrow
\text{same sole relevant multi-state policy }\pi_a
\longrightarrow
\begin{cases}
\pi_a\text{ satisfies the contract},\\
\text{or no available A2 policy does}.
\end{cases}
\]

Accordingly,

\[
\boxed{
\text{certificate ambiguity exists}
\quad\land\quad
\text{policy-choice ambiguity does not arise under the declared family}.
}
\]

The failure locus is therefore **policy topology for this sought witness**:
the frozen policy family contains no pair of distinct viable multi-state
policies hidden behind the same constructor-visible state.

This does not erase the reconstruction obstruction, and it does not imply
that richer policy families are safer. It says only that this particular A2
architecture cannot instantiate the desired nonempty/disjoint selector
conflict under the declared contracts.

## 7. Terminal standing and claim ceiling

| Claim | Standing |
|---|---|
| A2 same-visible-state certificate ambiguity | **ESTABLISHED** |
| A2 certificate reconstruction obstruction | **ESTABLISHED** |
| A2 hidden gain-contract feasibility difference | **ESTABLISHED** |
| Nonempty/disjoint selector witness under \(Q_J,Q_K,Q_{J+P}\) and frozen A2 nine-policy topology | **NO WITNESS / STRUCTURALLY IMPOSSIBLE** |
| Structural reason: every nonempty compatible set is the visible active diagnostic singleton \(\{\pi_a\}\) | **ESTABLISHED** |
| Broader information-limited selector obstruction | **OPEN** |
| Temporal improvement, human control, general corrigibility | **NOT ESTABLISHED** |
| New assay authorization or MATRIX\(_1\) | **NONE / NOT EARNED** |

The negative result must not be shortened to a global `REFUTED`. Its exact
scope is

\[
\boxed{
\text{NO WITNESS / STRUCTURALLY IMPOSSIBLE}
\quad
\text{UNDER }Q_J,Q_K,Q_{J+P}
\text{ AND THE FROZEN A2 NINE-POLICY FAMILY}.
}
\]

No A2 endpoint, preregistration, historical result, GL record, or MATRIX
kernel object is revised by this analysis.
