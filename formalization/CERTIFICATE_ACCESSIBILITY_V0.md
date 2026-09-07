# Certificate accessibility and certificate-guided realization V0

**Standing:** FORMAL BOUNDARY RECORD / THEOREM-LEVEL / NO EXECUTION.  
**Role:** separates analyst-computed corrective certificates from constructor-visible accessibility and system-realizable policy selection.  
**Source checkpoint:** `73c22e6a36bca262085a9129df7ab8c3a61136b3`.

This record extends the existing EXEC/A2 semantic boundary. It introduces no
implementation, assay, prospective execution, learner modification, or new
scientific endpoint. The definitions below make the next missing link precise:

\[
\text{certificate existence}
\;\longrightarrow\;
\text{certificate accessibility}
\;\longrightarrow\;
\text{certificate-guided realization}
\;\longrightarrow\;
\text{execution}.
\]

None of these arrows is assumed to hold automatically.

## 1. Objects and typing

Fix a declared finite system contract

\[
G=(\mathcal H,\mathcal U,R,c,\beta,\Pi,i_\Pi(G)),
\]

with hypothesis class \(\mathcal H\), primitive affordances \(\mathcal U\),
repair relation \(R\), charged cost \(c\), budget \(\beta\), realization
machinery \(\Pi\), and constructor-visible state \(i_\Pi(G)\).

Let \(a\in\mathcal H\) be the final active hypothesis and let
\(L\subseteq\mathcal H\) be the retained survivor set. The set \(L\) may be
available in an analyst's sealed record without being available to the
constructor or policy selector.

For any candidate \(h\in\mathcal H\), define the success-set families of the
fixed active decoder and the fixed baseline decoder:

\[
F_a(h)=\Phi\!\left(\operatorname{Fix}(T_a^{-1}T_h)\right),
\qquad
F_0(h)=\Phi\!\left(\operatorname{Fix}(T_0^{-1}T_h)\right).
\]

Here \(F_a(h),F_0(h)\subseteq 2^\Omega\), not scalar scores.

The certificate is typed as

\[
\boxed{
\operatorname{Cert}(a,L)=\bigl(K(a,L),J(a,L),P(a,L)\bigr)
}
\]

with

\[
K(a,L)=\bigcap_{h\in L}
\operatorname{Fix}(T_a^{-1}T_h)
\subseteq\Omega,
\]

\[
J(a,L)=\bigcap_{h\in L}
\left(F_a(h)\setminus F_0(h)\right)
\subseteq 2^\Omega,
\]

and

\[
\boxed{
P(a,L):=
\left[\forall h\in L,\;F_0(h)\subseteq F_a(h)\right].
}
\]

\(K\) is a state-level guaranteed diagnostic success set. \(J\) is a
family of uncertainty sets that are gains for every retained candidate.
\(P\) is the Boolean preservation predicate. They answer different
questions and must not be collapsed.

The certificate is an analyst-side mathematical object unless an explicit
information interface makes it accessible to the system.

## 2. Accessibility is reconstructibility

Let

\[
s=\sigma(i_\Pi(G))
\]

be a declared summary of constructor-visible information. The summary may be
smaller than the raw constructor state. It may not read the hidden truth
\(h^\star\), the analyst's tested set \(S\), or any post hoc result.

Certificate accessibility means that there exists a declared reconstruction
map

\[
\boxed{
\kappa:\mathcal S\to
\mathcal K\times\mathcal J\times\{\mathsf{false},\mathsf{true}\}
}
\]

where \(\mathcal K=2^\Omega\) and
\(\mathcal J=2^{2^\Omega}\) are the codomains for \(K\) and \(J\).

such that

\[
\boxed{
\kappa\!\left(\sigma(i_\Pi(G))\right)
=\operatorname{Cert}(a,L)
}
\]

for every system in the declared contract class.

The certificate need not be materialized inside \(i_\Pi(G)\). It is enough
that the exposed information reconstructs it by a fixed, declared map. The
reconstruction map itself is part of the contract; an analyst privately
computing the certificate from a richer record does not establish
accessibility.

### Accessibility theorem

Suppose there is a function
\[
q_\sigma:\mathcal S\to\mathcal H\times 2^{\mathcal H}
\]
such that

\[
q_\sigma(\sigma(i_\Pi(G)))=(a,L)
\]

for every system in the declared class, and suppose the certificate formula
\(\operatorname{Cert}\) is fixed and computable on that class. Then

\[
\kappa(s):=\operatorname{Cert}(q_\sigma(s))
\]

is a valid reconstruction map, with

\[
\kappa(\sigma(i_\Pi(G)))=\operatorname{Cert}(a,L).
\]

This is a sufficiency result for an information interface. It does not say
that the existing A2 constructor exposes \(L\), that a learner computes
\(\kappa\), or that any policy uses the result.

## 3. Certificate-guided policy selection

Accessibility and policy selection are separate. Let \(\Gamma\) be a declared
selector that receives only \(s\) and frozen contract constants:

\[
\Gamma:\mathcal S\longrightarrow
\{(\delta,\pi)\}.
\]

\(\Gamma\) is certificate-guided only if it factors through the reconstructed
certificate:

\[
\Gamma(s)=\Gamma^\prime(\kappa(s)),
\]

with no hidden \(h^\star\), analyst-only \(L\), or analyst-only \(S\) supplied
at selection time.

To state realization without smuggling in an unstated preservation rule, fix
a deployment contract \(Q\). \(Q\) specifies a target family
\(\mathcal T_Q\subseteq J\), a budget requirement, and any preservation
requirement that the deployment is supposed to satisfy. Define the
certificate-compatible policy set

\[
\mathcal C_Q(G,\operatorname{Cert})
=
\left\{
(\delta,\pi)\in\mathfrak{Real}_{\Pi,\mathcal U}(i_\Pi(G)):
\begin{array}{l}
\text{\((\delta,\pi)\) satisfies \(Q\),}\\
\text{the charged cost is at most \(\beta\),}\\
\text{and, for every \(S\in\mathcal T_Q\),}\\
\text{\(S\subseteq\operatorname{Succ}_G(\pi)\)}
\end{array}
\right\}.
\]

The quantifier over the target uncertainty set remains the EXEC order:
one realized policy must succeed uniformly over the whole tested set. The
analyst may not choose a different policy after observing the hidden state.

Certificate-guided realization is therefore the conjunction

\[
\boxed{
\kappa(\sigma(i_\Pi(G)))=\operatorname{Cert}(a,L)
\quad\land\quad
\Gamma^\prime(\operatorname{Cert}(a,L))
\in\mathcal C_Q(G,\operatorname{Cert}(a,L)).
}
\]

Execution is a further claim: the selected realized policy must actually
produce the certified success within the charged budget under the declared
response and repair semantics.

The existence of \(K\), \(J\), or \(P\) alone proves none of these latter
properties.

## 4. Reconstruction impossibility

Let \(G_1,G_2\) be two systems with the same visible summary:

\[
\sigma(i_\Pi(G_1))=\sigma(i_\Pi(G_2)).
\]

If their certificates differ,

\[
\operatorname{Cert}_1\ne\operatorname{Cert}_2,
\]

then no deterministic reconstruction map \(\kappa\) from that summary can be
correct for both systems:

\[
\boxed{
\sigma(i_\Pi(G_1))=\sigma(i_\Pi(G_2))
\land
\operatorname{Cert}_1\ne\operatorname{Cert}_2
\Rightarrow
\nexists\kappa\text{ that exactly reconstructs both}.
}
\]

This is an information-theoretic result. It concerns certificate
distinguishability and says nothing by itself about whether the same policy
happens to work in both systems.

## 5. Incompatible-policy impossibility

The stronger control question requires policy incompatibility. Suppose again

\[
\sigma(i_\Pi(G_1))=\sigma(i_\Pi(G_2)),
\]

but, for a shared deployment contract \(Q\),

\[
\boxed{
\mathcal C_Q(G_1,\operatorname{Cert}_1)
\cap
\mathcal C_Q(G_2,\operatorname{Cert}_2)
=\varnothing.
}
\]

Every deterministic selector based only on the shared visible summary returns
the same policy pair in both systems. That pair cannot belong to both
certificate-compatible sets. Therefore no such selector can satisfy the
certificate-guided realization contract in both systems.

\[
\boxed{
\text{same visible summary}
\land
\text{incompatible certificate-compatible policies}
\Rightarrow
\text{no deterministic certificate-correct selector}.
}
\]

This separates the two impossibility problems:

\[
\boxed{
\text{certificate distinguishability}
\neq
\text{policy distinguishability}.
}
\]

Different certificates do not suffice for a control impossibility if the
systems share a safe policy. Conversely, a policy that happens to work does
not establish that the system had information sufficient to know why or when
it was safe.

The result is stated for deterministic selectors. A randomized selector can
restore an exact guarantee only when its support is contained in the relevant
policy intersection; otherwise it changes the claim to a probabilistic one.

## 6. Relation to A2 non-exact expansions

The A2 post-execution analysis computes \(L\), \(K\), \(J\), and \(P\) from
sealed trajectory records. That establishes analyst-side reconstruction from
the archived record. It does not establish that those objects were present in
the constructor-visible state or that the learner computed them.

The existing active hypothesis \(a\) can already generate a realizable
diagnostic policy in the frozen A2 machinery. Therefore actual expansion
under that policy is not evidence that the system possessed a certificate or
used one to select the policy. The unresolved question is whether a declared
interface can expose enough information to justify selection or deployment
without revealing \(h^\star\), the analyst's \(L\), or the tested set.

In particular,

\[
\boxed{
\text{certificate exists}
\not\Rightarrow
\text{certificate is reconstructible}
\not\Rightarrow
\text{a certificate-guided policy is realizable}
\not\Rightarrow
\text{the policy executes successfully}.
}
\]

## Terminal standing

| Claim | Standing |
|---|---|
| Typed certificate \((K,J,P)\) | **DEFINED** |
| Accessibility as reconstruction from constructor-visible summary | **DEFINED** |
| Reconstruction sufficiency theorem | **ESTABLISHED FORMALLY** |
| Same-visible-state certificate ambiguity obstruction | **ESTABLISHED FORMALLY** |
| Incompatible-policy selection obstruction | **ESTABLISHED FORMALLY** |
| A2 certificate accessibility | **NOT ESTABLISHED** |
| A2 certificate-guided selection or deployment | **NOT ESTABLISHED** |
| Temporal improvement, human control, general corrigibility | **NOT ESTABLISHED** |
| New assay authorization or MATRIX\(_1\) | **NONE / NOT EARNED** |

This record closes a definitional seam only. It does not promote the
post-execution A2 certificates into system capabilities, revise any
preregistration, or authorize implementation or prospective execution.
