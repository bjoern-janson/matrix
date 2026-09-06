# GL–MATRIX executable translation V0

**Standing:** FINITE EXECUTABLE TRANSLATION EARNED / POLICY-INDEPENDENT IMPLICATION REFUTED.  
**Role:** derived finite semantic witness and counterconstruction. No experiment, learning result, kernel amendment, or MATRIX_1 promotion.  
**Source checkpoint:** `48ed77ec37deed828ef66aa1403e1f0ef7dd5fcc`.

This record discharges the finite executable translation obligation in Section 7 of [GL_FIXED_SPACE_SEPARATION_V0.md](GL_FIXED_SPACE_SEPARATION_V0.md), under the explicit contracts below. That earlier document retains its historical standing. The governing realization, execution, and frontier definitions are those of [EXEC_V1.md](EXEC_V1.md), especially Sections 3–6 and 12.

The two results must be retained together: the declared nine-policy machinery makes the operator distinction frontier-determining; enriching that same machinery with two fixed inverse decoders erases the frontier distinction. Neither result identifies geometry alone with corrective capacity.

## 1. Finite executable construction

Use column vectors with coordinates numbered 1, 2, 3:

\[
\Omega=\mathbb F_2^3,\qquad
A=I+E_{12},\qquad B=I+E_{13}.
\]

Thus

\[
Ax=(x_1+x_2,x_2,x_3),\qquad
Bx=(x_1+x_3,x_2,x_3),
\]

with arithmetic over \(\mathbb F_2\). Both maps are invertible and self-inverse. Write \(G_T\) for the fixed system whose hidden operator parameter is \(T\in\{A,B\}\), and use \(\beta\) for the budget to distinguish it from matrix \(B\).

In each episode, the latent state is \(x\in\Omega\). The operator parameter is fixed throughout the episode. The latent state does not change before termination. Constructor-visible information is the same fixed task tag in both systems; neither \(T\), \(x\), nor the analyst's tested set \(S\) is a constructor input.

The common primitive interface is

\[
\mathcal U=\{q\}\cup\{r_y:y\in\Omega\}.
\]

Its common execution rule reads the actual hidden operator parameter:

| Action | Observation / effect | Charge |
|---|---|---:|
| \(q\) | Return the full vector \(o=Tx\); retain latent \(x\) | 1 |
| \(r_y\) | Terminate; repair succeeds exactly when \(y=x\) | 1 |

The repair relation is \(R(x,y)\iff y=x\) in both systems. Response jurisdiction is deterministic/trivial. This construction declares

\[
\boxed{C_{\rm real}(\delta)=0,\qquad\beta=2}
\]

for every realization branch, including the enrichment in Section 4. This is an explicit abstract accounting convention for this semantic witness, not a measured resource advantage.

The vector-valued query is a new primitive semantic contract. It is not A2's three separately charged coordinate queries. Only the policy-count shape resembles A2. If realization were instead charged 1, the diagnostic policies below would cost 3 and their stated frontiers would require budget 3.

Let the shared machinery \(\Pi_9\) realize exactly:

\[
\pi_y:r_y\quad(y\in\Omega),\qquad
\pi^\star:q\longrightarrow o\longrightarrow r_o.
\]

Formally, for the fixed common constructor input \(i_0\),

\[
\mathfrak{Real}_{\Pi_9,\mathcal U}(i_0)
=\{(\delta_y,\pi_y):y\in\Omega\}
 \cup\{(\delta_\star,\pi^\star)\}.
\]

Each \(\delta\) selects its named fixed program through a declared, deliberately reachable menu branch. No program is generated from hidden truth or analyst-only \(S\). The machinery has no other realization branches and no automatic closure under arbitrary program composition. Primitive executability alone does not imply realization by \(\Pi_9\).

An immediate policy ignores observations and costs 1. The diagnostic first queries, then copies the observed vector into the repair action; it costs 2. The same realized program must work for all states of a tested set:

\[
S\in\Phi_2(G_T)
\iff
\exists(\delta,\pi)\in\mathfrak{Real}_{\Pi_9,\mathcal U}(i_0)
\ \forall x\in S:
\mathrm{Success}(\pi,x;G_T)=1,\quad
C_{\rm charged}(\delta,\pi,x)\le2.
\]

This is system-relative availability, not a policy chosen separately after revealing each latent state.

## 2. Exact frontier and obstruction enumeration

Put \(F_T=\operatorname{Fix}(T)\). The complete success-set census is

\[
\operatorname{Succ}(\pi_y;G_T)=\{y\},\qquad
\operatorname{Succ}(\pi^\star;G_T)
=\{x:Tx=x\}=F_T.
\]

All nine policies satisfy the budget. Since there are no additional available policies,

\[
\boxed{\Phi_2(G_T)=2^{F_T}\cup\{\{x\}:x\in\Omega\}.}
\]

The empty set already belongs to \(2^{F_T}\). This establishes the whole frontier, rather than merely the distinguished decoder's success set.

For the chosen operators,

\[
F_A=\{x:x_2=0\},\qquad F_B=\{x:x_3=0\},
\]

so \(|F_A|=|F_B|=4\) and \(|F_A\cap F_B|=2\). Therefore

\[
|\Phi_2(G_A)|=|\Phi_2(G_B)|=2^4+(8-4)=20,
\]

and

\[
|\Phi_2(G_A)\cap\Phi_2(G_B)|
=2^2+(8-2)=10.
\]

Both directed differences have cardinality 10. Explicit witnesses are

\[
S_A=\{(0,0,0),(0,0,1)\}\in\Phi_2(G_A)\setminus\Phi_2(G_B),
\]

\[
S_B=\{(0,0,0),(0,1,0)\}\in\Phi_2(G_B)\setminus\Phi_2(G_A).
\]

Hence the frontiers are incomparable, despite equal cardinality.

Every singleton is feasible. A set of size at least two is infeasible exactly when it contains a point outside \(F_T\). Choosing that point and any other point produces an infeasible pair; every proper subset of that pair is feasible. Conversely, a pair wholly inside \(F_T\) is feasible. Thus the exact minimal-obstruction hypergraph is

\[
\boxed{
H_2(G_T)=
\{\{x,y\}:x\ne y,\ \{x,y\}\not\subseteq F_T\}.
}
\]

Consequently each obstruction family has \(\binom82-\binom42=28-6=22\) pairs. The feasible-pair families have six members each and one common member, so each obstruction family has five members absent from the other.

### Reproducible finite check

The following standard-library enumeration executes only the explicitly declared finite programs. It verifies the algebraic statements; it is not an A2 assay, prospective experiment, or learned-system result. State integer \(4x_1+2x_2+x_3\) encodes a vector; subset-mask bit \(x\) denotes that state.

```python
from itertools import combinations

OMEGA = tuple(range(8))
A = lambda x: x ^ (((x >> 1) & 1) << 2)
B = lambda x: x ^ ((x & 1) << 2)

def policies(enriched=False):
    menu = [("repair", y) for y in OMEGA] + [("copy", None)]
    return menu + ([("inverse_A", None), ("inverse_B", None)]
                   if enriched else [])

def execute(T, policy, x):
    kind, target = policy
    if kind == "repair":
        return (("r", target),), (), target == x, 1
    o = T(x)
    y = {"copy": lambda z: z,
         "inverse_A": A, "inverse_B": B}[kind](o)
    return (("q",), ("r", y)), (o,), y == x, 2

def powerset_masks(states):
    mask = sum(1 << x for x in states)
    return {s for s in range(256) if not (s & ~mask)}

def frontier(T, enriched=False):
    executions = [[execute(T, p, x) for x in OMEGA]
                  for p in policies(enriched)]
    return {s for s in range(256)
            if any(all(row[x][2] and row[x][3] <= 2
                       for x in OMEGA if s & (1 << x))
                   for row in executions)}

def obstructions(front):
    return {s for s in range(256) if s not in front
            and all((s ^ (1 << x)) in front
                    for x in OMEGA if s & (1 << x))}

fa = {x for x in OMEGA if A(x) == x}
fb = {x for x in OMEGA if B(x) == x}
domain = {x for x in OMEGA if A(x) == B(x)}
floor = {1 << x for x in OMEGA}
pa, pb = frontier(A), frontier(B)
ha, hb = obstructions(pa), obstructions(pb)

assert all(A(A(x)) == B(B(x)) == x for x in OMEGA)
assert fa == {0, 1, 4, 5} and fb == {0, 2, 4, 6}
assert domain == {0, 3, 4, 7}
assert pa == powerset_masks(fa) | floor
assert pb == powerset_masks(fb) | floor
assert (len(pa), len(pb), len(pa - pb), len(pb - pa)) == (20, 20, 10, 10)
assert 3 in pa - pb and 5 in pb - pa
for fixed, excluded in ((fa, ha), (fb, hb)):
    assert excluded == {sum(1 << x for x in pair)
                        for pair in combinations(OMEGA, 2)
                        if not set(pair) <= fixed}
assert (len(ha), len(hb), len(ha - hb), len(hb - ha)) == (22, 22, 5, 5)
assert all(execute(A, p, x) == execute(B, p, x)
           for p in policies() for x in domain)
assert pa & powerset_masks(domain) == pb & powerset_masks(domain)
assert frontier(A, True) == frontier(B, True) == set(range(256))
print("PASS: finite semantic enumeration; no A2 assay execution")
```

The direct proofs above are the mathematical authority. The enumeration is a reproducible consistency check of all 256 uncertainty sets.

## 3. Domain-restricted agreement

The algebraic agreement domain is

\[
D=\{x:Ax=Bx\}=\{x:x_2=x_3\},\qquad |D|=4=2^{3-1}.
\]

By the prior GL theorem, this is the maximal possible agreement-domain cardinality for distinct elements of \(GL(3,2)\).

Here \(\operatorname{Trace}\) denotes observable action/observation traces together with charged costs and terminal repair judgments. It excludes the hidden operator parameter itself; the full verifier states \(G_A,G_B\) are different.

Immediate repairs are identical in both systems. For \(x\in D\), the query observation is also identical, so the copy decoder emits the same repair and receives the same repair judgment. Therefore

\[
\boxed{
\forall x\in D\ \forall\pi\in\operatorname{Avail}_9:
\operatorname{Trace}(\pi,x;G_A)
=\operatorname{Trace}(\pi,x;G_B).
}
\]

The shared policy family and equal traces on \(D\) imply

\[
\boxed{\Phi_2(G_A)\cap2^D=\Phi_2(G_B)\cap2^D.}
\]

This also follows from \(F_A\cap D=F_B\cap D=\{(0,0,0),(1,0,0)\}\). Every separating uncertainty set reaches outside \(D\).

Thus agreement on a declared observation domain of maximal possible size does not imply equality of the global corrective frontier. “Maximal” is relative to distinct operators in this linear family, not all conceivable systems. No time, training, distribution shift, or later divergence has been introduced. Calling \(D\) a present testing domain is a domain declaration, not a temporal theorem.

## 4. Inverse enrichment and policy-independent refutation

Hold both systems' latent operators, primitive interface, observations, repair relation, costs, budget, and constructor input fixed. Replace \(\Pi_9\) with common machinery \(\Pi_{11}\) whose menu contains all nine earlier programs plus

\[
\pi_A:q\longrightarrow o\longrightarrow r_{A^{-1}o},\qquad
\pi_B:q\longrightarrow o\longrightarrow r_{B^{-1}o}.
\]

Both inverse programs are fixed, named, deliberately selectable branches available in both systems. Neither receives a hidden \(T\) flag. They merely apply their respective fixed inverse to the query observation. Realization remains explicitly zero-cost; both programs cost 2 to execute.

For each fixed world,

\[
\pi_A\text{ succeeds on every }x\text{ in }G_A,\qquad
\pi_B\text{ succeeds on every }x\text{ in }G_B.
\]

It follows that

\[
\boxed{
\Phi_2(G_A;\Pi_{11})
=\Phi_2(G_B;\Pi_{11})
=2^\Omega,\qquad |2^\Omega|=256.
}
\]

The quantifier is

\[
\forall T\in\{A,B\}\ \exists\pi_T\in\operatorname{Avail}_{11}\
\forall x\in\Omega.
\]

This establishes each fixed system's available capacity. It does not establish

\[
\exists\pi\ \forall T\in\{A,B\}\ \forall x\in\Omega,
\]

or a controller that can identify the correct inverse without operator information. Availability of both programs is not an informed inverse-selection procedure. The original EXEC_V1 reachable-policy interpretation is retained.

Although \(\operatorname{Fix}(A)\ne\operatorname{Fix}(B)\), the enriched frontiers are equal. Thus this is a finite counterexample to the policy-independent implication

\[
\operatorname{Fix}(A)\ne\operatorname{Fix}(B)
\ \Longrightarrow\
\Phi_\beta(G_A)\ne\Phi_\beta(G_B)
\quad\text{independently of }\Pi.
\]

The positive and negative results concern the very same operator pair. Under \(\Pi_9\) its distinction determines different frontiers; under \(\Pi_{11}\) the frontier distinction disappears. This exercises the existing system-relative decomposition of operator/observation semantics, realization machinery, and corrective capacity. It is not empirical validation of MATRIX_0.

## Terminal standing

| Claim | Standing |
|---|---|
| Finite executable GL-to-MATRIX translation under the declared contracts | **EARNED** |
| Incomparable frontiers under the complete nine-policy menu | **ESTABLISHED** |
| Domain-restricted trace agreement with global frontier separation | **ESTABLISHED** |
| Frontier washout under the declared inverse enrichment | **ESTABLISHED** |
| Policy-independent fixed-space-inequality-to-frontier-inequality implication | **REFUTED** |
| Learning, temporal improvement, informed inverse selection, human control, general corrigibility | **NOT ESTABLISHED** |
| New assay authorization or MATRIX_1 | **NONE / NOT EARNED** |

\[
\boxed{
\text{finite translation EARNED}
\ \land\
\text{policy-independent implication REFUTED}
\ \land\
\text{no temporal/learning/general corrigibility claim}
}.
\]

The existential finite translation obligation of the earlier GL record is closed by this construction. A policy-independent strengthening is refuted. No new experiment or follow-up is frozen, and no A2 scientific record is revised.
