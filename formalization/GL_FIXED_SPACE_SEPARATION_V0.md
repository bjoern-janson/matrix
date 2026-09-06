# GL fixed-space separation V0

**Standing:** MATHEMATICAL THEOREM EARNED / MATRIX TRANSLATION UNEARNED.  
**Role:** candidate mathematical substrate only. This record does not amend the MATRIX kernel, define a new MATRIX concept, freeze an assay, or earn `MATRIX_1`.

## 1. Algebraic setup

Let

\[
A,B\in GL(d,2)
\]

act linearly on \(\mathbb F_2^d\). Define their agreement set

\[
D(A,B):=\{x\in\mathbb F_2^d:Ax=Bx\}.
\]

Because \(A\) is invertible,

\[
Ax=Bx
\iff
A^{-1}Bx=x,
\]

so

\[
\boxed{D(A,B)=\operatorname{Fix}(A^{-1}B).}
\]

This identity is purely algebraic. It does not by itself identify \(D(A,B)\) with a MATRIX observation domain, current behavioral equivalence class, or corrective frontier.

## 2. Maximal agreement theorem

### Theorem

For every \(d\ge2\) and every distinct \(A,B\in GL(d,2)\),

\[
\boxed{|D(A,B)|\le 2^{d-1}.}
\]

The bound is sharp.

### Proof

If \(A\ne B\), then

\[
C:=A^{-1}B\ne I.
\]

Hence

\[
D(A,B)=\operatorname{Fix}(C)=\ker(C-I).
\]

Because \(C-I\ne0\), its kernel is a proper linear subspace of \(\mathbb F_2^d\). Every proper subspace has dimension at most \(d-1\), therefore

\[
|D(A,B)|=2^{\dim\ker(C-I)}\le2^{d-1}.
\]

To attain the bound, take

\[
A=I,
\qquad
B=I+E_{12},
\]

where \(E_{12}\) has a single \(1\) in row 1, column 2. Since \(E_{12}^2=0\),

\[
(I+E_{12})^{-1}=I+E_{12},
\]

so \(B\in GL(d,2)\). Agreement requires

\[
E_{12}x=0
\iff
x_2=0,
\]

and therefore

\[
|D(A,B)|=2^{d-1}.
\]

Thus

\[
\boxed{|D|_{\max}=2^{d-1}\qquad(d\ge2).}
\]

## 3. Minimal dimension

\(GL(1,2)=\{I\}\), so \(d=1\) contains no distinct pair \(A,B\) and cannot realize the separation problem.

Thus

\[
\boxed{d=2\text{ is the first nontrivial purely linear dimension.}}
\]

## 4. Equal fixed-space size with different geometry

For every \(d\ge2\), distinct invertible linear maps can have fixed spaces of the same cardinality but different geometry.

For example, in \(d\ge2\),

\[
A=I+E_{12},
\qquad
B=I+E_{21}
\]

give

\[
\operatorname{Fix}(A)=\{x:x_2=0\},
\qquad
\operatorname{Fix}(B)=\{x:x_1=0\},
\]

so

\[
\boxed{
|\operatorname{Fix}(A)|
=
|\operatorname{Fix}(B)|
=
2^{d-1},
\qquad
\operatorname{Fix}(A)\ne\operatorname{Fix}(B).
}
\]

Varying \(d\) gives an infinite cross-dimensional family. No claim of an infinite family inside a fixed finite group \(GL(d,2)\) is intended.

## 5. Combined maximal-agreement witness for \(d\ge3\)

For \(d\ge3\), let

\[
A=I+E_{12},
\qquad
B=I+E_{13}.
\]

Then

\[
\operatorname{Fix}(A)=\{x:x_2=0\},
\qquad
\operatorname{Fix}(B)=\{x:x_3=0\},
\]

so

\[
|\operatorname{Fix}(A)|
=
|\operatorname{Fix}(B)|
=
2^{d-1}
\]

while

\[
\operatorname{Fix}(A)\ne\operatorname{Fix}(B).
\]

At the same time,

\[
Ax=Bx
\iff
x_2=x_3,
\]

so

\[
D(A,B)=\{x:x_2+x_3=0\}
\]

and

\[
|D(A,B)|=2^{d-1}.
\]

Therefore a single pair can simultaneously satisfy

\[
\boxed{
\begin{aligned}
A|_{D}&=B|_{D},\\
|D|&=2^{d-1},\\
|\operatorname{Fix}(A)|&=|\operatorname{Fix}(B)|=2^{d-1},\\
\operatorname{Fix}(A)&\ne\operatorname{Fix}(B).
\end{aligned}
}
\]

This is the strongest algebraic separation earned here:

\[
\boxed{
\text{maximal possible agreement between distinct operators}
\not\Rightarrow
\text{equal fixed-space geometry}.
}
\]

## 6. What this does and does not say about behavior

The theorem concerns linear operators and their algebraic agreement set. To call \(A|_D=B|_D\) "current behavioral equivalence" inside MATRIX, a later translation must independently establish that the declared executable observation/interaction semantics actually expose exactly the relevant domain \(D\).

Accordingly, the safe current statement is

\[
\boxed{
\text{operator structure}
\ne
\text{agreement on a declared present domain}
\ne
\text{corrective frontier}.
}
\]

The algebraic theorem alone does not establish a behavioral result for MATRIX.

## 7. MATRIX translation obligation

A valid bridge requires explicit executable systems \(G_A,G_B\), not a relabeling of linear algebra.

The construction must specify the actual MATRIX-side objects that determine realizability and frontier membership, including the relevant observation/intervention affordances, policy-generation machinery, valid-repair semantics, grounded cost and corrective budget.

If translation-local notation \(A_{\rm succ}(G)\) is introduced for the success set of the distinguished executable mechanism, then one necessary target could be

\[
A_{\rm succ}(G_A)=\operatorname{Fix}(A),
\qquad
A_{\rm succ}(G_B)=\operatorname{Fix}(B).
\]

But this equality is **not sufficient by itself** to earn frontier separation.

MATRIX frontiers quantify over the system-relative realizable policy family. A different available policy could repair states omitted by the distinguished mechanism and erase the fixed-space distinction at the level of \(\Phi_\beta\).

Therefore the missing bridge includes an additional obligation:

\[
\boxed{
\text{prove that alternate realizable policies do not erase the fixed-space distinction.}
}
\]

One especially clean sufficient construction would establish

\[
\Phi_\beta(G_A)=2^{\operatorname{Fix}(A)},
\qquad
\Phi_\beta(G_B)=2^{\operatorname{Fix}(B)},
\]

for a declared budget \(\beta\). Then

\[
\operatorname{Fix}(A)\ne\operatorname{Fix}(B)
\Rightarrow
\Phi_\beta(G_A)\ne\Phi_\beta(G_B).
\]

This powerset form is sufficient, not required. Any explicit executable construction that makes the fixed-space difference frontier-determining would satisfy the translation burden.

The current causal ladder is therefore

\[
\boxed{
\text{GL theorem}
\rightarrow
\text{explicit executable }G_A,G_B
\rightarrow
\text{fixed-space success correspondence}
\rightarrow
\text{control of alternate realizable policies}
\rightarrow
\Phi_\beta(G_A)\ne\Phi_\beta(G_B).
}
\]

Only the first step is earned by this record.

## 8. Order variables remain distinct

No result here licenses conflation of different notions of order:

\[
\boxed{
\operatorname{ord}(A)
\ne
\text{encounter order}
\ne
\text{learner update order}.
}
\]

Here \(\operatorname{ord}(A)\) means group-theoretic operator order. It is not the ordering of operator composition, corpus encounter, or learning updates.

## 9. Claim ceiling

Earned:

- the maximal-agreement theorem for distinct \(A,B\in GL(d,2)\), \(d\ge2\);
- sharpness of the \(2^{d-1}\) bound;
- existence for every \(d\ge2\) of equal-cardinality but geometrically distinct hyperplane fixed spaces;
- for every \(d\ge3\), a pair exhibiting both maximal agreement and different equal-sized fixed spaces.

Not earned:

- identification of the algebraic agreement set with a MATRIX current-behavior domain;
- an executable MATRIX realization of the fixed spaces;
- any implication from \(\operatorname{Fix}(A)\ne\operatorname{Fix}(B)\) to \(\Phi_\beta(G_A)\ne\Phi_\beta(G_B)\) without the missing construction;
- a new assay or assay authorization;
- an affine generalization;
- a new MATRIX concept;
- any revision of `MATRIX_0`;
- `MATRIX_1`.

## 10. Current ledger

\[
\boxed{
\text{GL theorem EARNED}
\quad\land\quad
\text{MATRIX translation UNEARNED}.
}
\]

This record is a derived mathematical substrate and a translation obligation. It is not empirical evidence and does not modify the standing of A2-V0 or A2-V1.
