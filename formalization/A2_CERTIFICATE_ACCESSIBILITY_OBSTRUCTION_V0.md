# A2 certificate accessibility obstruction V0

**Standing:** POST-EXECUTION / DERIVED / FORMAL BOUNDARY RECORD.  
**Scope:** sealed A2-V1 records and the frozen A2 constructor interface.  
**Source checkpoint:** `92abc97f893658da6c4d2ca17580eb95ffaba62e`.  
**Frozen implementation checkpoint:** `2b79c73dd9ac46fd6f693fd35d63c44cbb396a40`.

This record instantiates the certificate-accessibility boundary from
[`CERTIFICATE_ACCESSIBILITY_V0.md`](CERTIFICATE_ACCESSIBILITY_V0.md) on
the already executed A2-V1 records. It adds no learner run, implementation,
assay, prospective execution, endpoint, or preregistration change.

The result has two different strengths. A2 directly contains a
same-visible-state certificate reconstruction obstruction. It also contains
a hidden difference in whether a nonvacuous gain contract is feasible. That
second result does not yet establish a nonempty-versus-nonempty
information-limited policy-selection conflict.

## 1. Frozen constructor boundary

The canonical A2-V1 implementation binds the terminal constructor state in
`experiments/a2_v1/implementation/a2_v1/engine.py`. Its frozen learner
returns exactly

\[
\operatorname{freeze}()=
\{\texttt{task}:\texttt{SWITCHBOARD\_3},
\texttt{active}:a\}.
\]

The evaluation function \(\_measure\) rejects every constructor object whose
key set is not exactly

\[
\{\texttt{task},\texttt{active}\}.
\]

It then passes that two-field object to the frozen policy realization
machinery. Thus, for the A2 terminal evaluation boundary,

\[
\boxed{
\sigma(i_\Pi(G))=
(\texttt{SWITCHBOARD\_3},a).
}
\]

The constructor does not receive \(L\), \(K(a,L)\), \(J(a,L)\), \(P(a,L)\),
the hidden \(h^\star\), or the analyst's tested uncertainty set.

The source binding used here is:

| File | Frozen source identity |
|---|---|
| `engine.py` | blob `1d6136461e5012f105957f9a7c22a6eadbdc5a5f` |
| `frozen_model.py` | blob `bd40559ca43d5f0ccb7c7e225e51494c74a5d292` |
| `authorities.py` | blob `30a069f4a0da77f8071cc20205d99ec1f32dcb71` |
| frozen original model binding | blob `f3aab0759b994aa06e961c62e7dfc27e8573fcf3` |

These are source identities, not new experimental evidence.

## 2. A2 certificate ambiguity census

The sealed analysis record computes

\[
\operatorname{Cert}(a,L)=\bigl(K(a,L),J(a,L),P(a,L)\bigr)
\]

from each terminal survivor set and the frozen algebraic frontier map. The
visible state is grouped only by the actual constructor fields
\((\texttt{SWITCHBOARD\_3},a)\).

On the prospective V1 stratum, 45 active states are represented and all
45 have more than one distinct certificate. Across the complete V1 factorial,
45 of 48 active states are certificate-ambiguous. These are finite
post-execution census counts, not population estimates.

Therefore A2 contains pairs \(G_1,G_2\) such that

\[
\boxed{
\sigma(i_\Pi(G_1))=\sigma(i_\Pi(G_2))
\quad\land\quad
\operatorname{Cert}(G_1)\ne\operatorname{Cert}(G_2).
}
\]

By the reconstruction impossibility result in
`CERTIFICATE_ACCESSIBILITY_V0.md\), no deterministic map from this
constructor-visible state can exactly reconstruct the certificate for both
systems.

## 3. Concrete reconstruction witness

The following two already executed prospective units share the same
constructor-visible state:

\[
u_1=(19,16,3),\qquad u_2=(19,16,4).
\]

Both have final active hypothesis \(a=8\), task
\(\texttt{SWITCHBOARD\_3}\), baseline success set \(\varnothing\), and actual
recorded class **EXPANSION** with \(a\ne h^\star\).

| Unit | Final survivor set \(L\) | \(K(a,L)\) | \(J(a,L)\) | \(P(a,L)\) |
|---|---|---|---|---|
| \(u_1\) | \(\{8,19,38\}\) | \(\{1,6\}\) | \(\{\{1,6\}\}\) | true |
| \(u_2\) | \(\{8,10,13,15,17,19,20,22,24,26,29,31,33,35,36,38\}\) | \(\varnothing\) | \(\varnothing\) | false |

The recorded treatment frontier in both units is an actual strict expansion.
For \(u_1\), every retained candidate gives expansion. For \(u_2\), the
retained candidates give 5 expansions, 9 nulls, and 2 contractions.

The constructor sees the same two fields in both rows. The different
survivor sets and certificates are absent from that interface. This is an
actual A2 instantiation of certificate reconstruction ambiguity, not merely
an abstract counterexample.

## 4. Hidden gain-contract feasibility difference

To examine policy compatibility without a vacuous empty target, define the
nonvacuous gain contract \(Q_{\mathrm{gain}}\) as follows:

\[
\exists S\in J(a,L)
\quad\text{such that one available policy succeeds uniformly on }S
\text{ for every }h\in L
\]

within the frozen A2 budget and policy family.

The A2 family contains the eight immediate repair policies
\(\pi_y\) and the active diagnostic policy \(\pi_a\). An immediate policy
succeeds on only one latent state. The active diagnostic succeeds on the
candidate fixed set \(\operatorname{Fix}(T_a^{-1}T_h)\).

For \(u_1\), \(J=\{\{1,6\}\}\). The immediate policies cannot realize this
two-state gain. The diagnostic \(\pi_8\) succeeds on \(\{1,6\}\) for all
three retained candidates. Therefore

\[
\boxed{
\mathcal C_{Q_{\mathrm{gain}}}(u_1)=\{\pi_8\}.
}
\]

For \(u_2\), \(J=\varnothing\). The nonvacuous gain contract has no target,
so

\[
\boxed{
\mathcal C_{Q_{\mathrm{gain}}}(u_2)=\varnothing.
}
\]

The two policy-compatible sets are disjoint while the constructor-visible
states are identical:

\[
\sigma(i_\Pi(G_{u_1}))=\sigma(i_\Pi(G_{u_2}))
\quad\land\quad
\mathcal C_{Q_{\mathrm{gain}}}(u_1)
\cap
\mathcal C_{Q_{\mathrm{gain}}}(u_2)=\varnothing.
\]

The correct interpretation is limited. The second system is infeasible under
\(Q_{\mathrm{gain}}\) even for a selector with perfect information. Thus this
pair establishes a hidden gain-contract feasibility difference, but it does
not isolate information insufficiency as the reason selection fails.

## 5. Claim ceiling

The following claims are established for the sealed A2-V1 records and frozen
constructor boundary:

\[
\boxed{
\begin{aligned}
&\text{A2 same-visible-state certificate ambiguity} && \textbf{ESTABLISHED}\\
&\text{A2 certificate reconstruction obstruction} && \textbf{ESTABLISHED}\\
&\text{A2 hidden gain-contract feasibility difference} && \textbf{ESTABLISHED}\\
&\text{A2 nonempty/disjoint policy-selection obstruction}
&& \textbf{NOT YET ESTABLISHED}.
\end{aligned}
}
\]

The last distinction matters: \(\mathcal C_1\cap\mathcal C_2=\varnothing\)
is not sufficient to attribute selection failure to hidden information when
one of the sets is already empty. A stronger A2 witness would require

\[
\mathcal C_Q(G_1)\ne\varnothing,\qquad
\mathcal C_Q(G_2)\ne\varnothing,\qquad
\mathcal C_Q(G_1)\cap\mathcal C_Q(G_2)=\varnothing.
\]

This record does not establish that stronger result.

No temporal improvement, human-control, informed-selection, general
corrigibility, implementation, assay authorization, or MATRIX\(_1\) claim
follows. The analysis is read-only, post-execution, and derived from sealed
records. No A2 endpoint, preregistration, or historical custody record is
rewritten.
