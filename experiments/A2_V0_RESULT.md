# A2-V0 — Scientific execution record

**Program:** MATRIX₀  
**Assay:** A2-PREREG-V0  
**Execution date:** 2026-09-05  
**Status:** COMPLETE / SEALED  
**Repository kernel revision:** NONE  
**README revision:** NONE

This record preserves the result of the frozen A2-V0 causal assay. The primary endpoint is the complete unit-indexed corrective-frontier map. Aggregate counts are descriptive compressions of that set-valued record, not replacements for it.

The result must be read under the preregistered distinction:

\[
\boxed{\text{validated implementation}\neq\text{scientific result}.}
\]

The implementation gate was cleared first; only then were the 320 units unresolved by pre-execution analysis run.

---

## 1. Provenance and custody

MATRIX parent state used by the standalone implementation:

```text
b006a581161be65ea34df39ba9558facddac386b
```

Validated scientific source digest:

```text
dd454df0cf646b44a11f91bc965ab5a40de1e62c860dacdf0e988d32205dc02d
```

Original validated implementation ZIP SHA-256:

```text
76b939f8a1724f14e057096cb2bfffa11e8454d59e4addd9a7bf05475837be6e
```

Original complete scientific-run archive SHA-256:

```text
cb9e444d1264b68013ead4c895fc5717b70bd310d6523cd6f091460c748021ff
```

The scientific run sealed these primary output hashes:

| File | SHA-256 |
| --- | --- |
| `primary.json` | `3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117` |
| `trajectories.json` | `aad6a6782c55f74537d274f78e53668daafddc6834a929ca4efde8018c0795b7` |
| `transplants.json` | `5529b9e29e42221db4f20e35685d2569c21af237e4959341106f45f1fb1e711c` |
| `utilities.json` | `5a054c1348080d78d48b7e529bb06dd1a25f5016d16bd17f998ace3189825ea0` |

Run report SHA-256:

```text
25792670a091adf14f980f47d4156c6855d7a4e3d65c33eb9802f4805c2dac4e
```

The run report binds the science execution to validation receipt hash:

```text
17f3bab6faf0957fa3c5f7b5b6fa11fd9667db1d10406dd6a1cd31ee7bce4b5f
```

The repo preserves the exact run receipt, utility and transplant outputs, an exact sufficient compact representation of the primary frontier endpoint, validated source/evidence, and the sealed SHA-256 identities of the original full serialized outputs.

---

## 2. Pre-execution implementation gate

Before unresolved scientific execution, the frozen implementation independently established:

```text
Tests                              17/17 PASS
Theorem-derived control signatures 64/64 MATCH
Invariant checks                    19/19 PASS
Unresolved units executed            0/320
Repository writes                         0
```

The 64 theorem-derived controls were not treated as scientific discoveries. They were exact validation oracles.

### 2.1 Expansion controls

For hypothesis indices `1..7`, all eight rotations:

\[
\Phi^+=2^\Omega,
\qquad
\Phi^-=\{S:|S|\le1\},
\]

\[
\Delta^+=\{S:|S|\ge2\},
\qquad
\Delta^-=\varnothing,
\]

with

\[
|\Phi^+|=256,
\qquad
|\Phi^-|=9,
\qquad
|\Delta^+|=247.
\]

All 56 matched.

### 2.2 Null controls

For hypothesis index `0`, all eight rotations:

\[
\Phi^+=\Phi^-=2^\Omega,
\qquad
\Delta^+=\Delta^-=\varnothing.
\]

All 8 matched.

The science command reran the gate before permitting unresolved training.

---

## 3. Primary endpoint

The 320 units not classified by the pre-execution theorem audit were all executed.

The frozen unit-level classification is:

| Frontier class | Units | Fraction of unresolved set |
| --- | ---: | ---: |
| EXPANSION | **254** | 79.375% |
| NULL | **32** | 10.000% |
| CONTRACTION | **18** | 5.625% |
| TRADEOFF | **16** | 5.000% |
| **Total** | **320** | **100%** |

Thus the exact paired frontier differed in

\[
254+18+16=288
\]

units:

\[
\boxed{288/320=90\%.}
\]

The primary scientific result is therefore

\[
\boxed{
254\ \mathrm{expansion},\quad
32\ \mathrm{null},\quad
18\ \mathrm{contraction},\quad
16\ \mathrm{tradeoff}.
}
\]

The complete primary object is preserved in reconstructible form in `results/primary_compact.json`; the original full `primary.json` is bound by its sealed SHA-256:

\[
\boxed{
u\mapsto
\left(
\Phi_{B,u}(0),
\Phi_{B,u}(1),
\Delta^+_{B,u},
\Delta^-_{B,u}
\right).}
\]

---

## 4. Directional frontier movement

Among the 320 previously unresolved units:

\[
\Delta^+\neq\varnothing
\]

for every expansion or tradeoff unit:

\[
\boxed{254+16=270.}
\]

Meanwhile

\[
\Delta^-\neq\varnothing
\]

for every contraction or tradeoff unit:

\[
\boxed{18+16=34.}
\]

Therefore feedback is not monotone with respect to the measured corrective frontier in this assay:

\[
\boxed{
F\not\Rightarrow
\Phi_B(G^{+F})\supseteq\Phi_B(G^{-F})
\quad\text{in A2-V0}.
}
\]

This is not a statement that feedback is generally harmful. It is a finite-assay falsification of universal monotone corrective expansion within the declared A2-V0 system.

The 34 loss-bearing units are scientifically important because they prevent the result from collapsing into a one-directional “feedback helps” demonstration.

---

## 5. Full 384-unit context

The 64 theorem-derived controls should remain analytically labeled rather than being rebranded as execution discoveries.

For bookkeeping only, combining them with the 320 executed-unresolved units gives:

| Class | Theorem controls | Previously unresolved execution | Full 384 |
| --- | ---: | ---: | ---: |
| EXPANSION | 56 | 254 | **310** |
| NULL | 8 | 32 | **40** |
| CONTRACTION | 0 | 18 | **18** |
| TRADEOFF | 0 | 16 | **16** |
| **Total** | **64** | **320** | **384** |

The scientific novelty of the run is the exact topology of the previously unresolved 320 units, not the existence of the 56 pre-proved positive controls.

---

## 6. Secondary weighted deployment-performance endpoint

Only after sealing the primary frontier result was the weighted deployment endpoint inspected.

Recall:

\[
V(A)=\sum_{x_i\in A}\frac{2^i}{255},
\qquad
255V(A)=\sum_{x_i\in A}2^i.
\]

This endpoint is a lossless encoding of the default policy's success set and is structurally coupled to A2-V0's frontier architecture. It is therefore **not** evidence of empirical independence between general future viability and corrective topology.

Across the 320 units:

| Sign of `C_improve` | Units |
| --- | ---: |
| `> 0` | **264** |
| `= 0` | **32** |
| `< 0` | **24** |

By frontier class:

| Frontier class | Positive | Zero | Negative |
| --- | ---: | ---: | ---: |
| EXPANSION | **254** | 0 | 0 |
| NULL | 0 | **32** | 0 |
| CONTRACTION | 0 | 0 | **18** |
| TRADEOFF | **10** | 0 | **6** |

The finite-unresolved-set mean is exactly

\[
\boxed{
\overline C_{\mathrm{improve}}=\frac{241}{400}=0.6025.
}
\]

The most informative joint cases are the 16 tradeoffs:

\[
\boxed{10\text{ tradeoff units had }C_{\mathrm{improve}}>0,}
\]

\[
\boxed{6\text{ tradeoff units had }C_{\mathrm{improve}}<0.}
\]

Thus even where the assay's deployment metric improves, some jointly correctable uncertainty sets can be lost. The correct narrow lesson is:

\[
\boxed{
\text{better weighted deployment performance}
\neq
\text{monotone preservation of corrective capacity}
\quad\text{in A2-V0}.
}
\]

Because the metric is structurally coupled to the success set, this does not yet establish a general empirical theory separating viability from corrective topology.

---

## 7. Information-boundary transplant check

There were 288 unresolved units with changed frontiers.

The preregistered bidirectional constructor-state transplant check passed for

\[
\boxed{288/288.}
\]

The permitted interpretation is only:

\[
\boxed{
\text{the implementation respected the declared constructor-visible-state boundary.}
}
\]

This is not new discovery that `Π` is the unique mediator. A2-V0 structurally restricted evaluation availability to the declared constructor-visible active hypothesis; the transplant verifies that the implementation honored that restriction.

No general mechanism promotion to `g`, `Q`, or `Π` is earned.

---

## 8. Secondary trajectory observation: frontier expansion without exact environment identification

This analysis was performed after the primary endpoint was sealed.

Treatment finished with the exact true hypothesis active in

\[
\boxed{202/320}
\]

previously unresolved units.

However, among the 254 expansion units, there were

\[
\boxed{52}
\]

cases in which treatment expanded the corrective frontier even though the final active hypothesis was not the exact hidden generating transformation:

\[
\hat h_8\neq h^\star.
\]

The narrow empirical separation is therefore:

\[
\boxed{
\text{exact representation recovery}
\neq
\text{necessary condition for corrective-frontier expansion}
\quad\text{in A2-V0}.
}
\]

This does **not** establish a general theory of approximate representation, partial identification, semantic equivalence, or representation quality. It only shows that exact recovery of the hidden transformation was unnecessary for frontier expansion in 52 finite assay units.

---

## 9. What the execution established

Under the frozen paired-clone, isolation, fixed-interface, exact-realization, exact-budget, and validation contracts, execution established the following finite-assay facts:

1. The corrective frontier is treatment-sensitive in 288 of the 320 units that had been unresolved by pre-execution analysis.
2. The treatment effect is directionally non-monotone: 34 units lose at least one previously correctable uncertainty set.
3. Tradeoff structure is real in the assay: 16 units simultaneously gain and lose correctable uncertainty sets.
4. The primary result cannot be reduced to a positive average or a single scalar without discarding scientifically relevant losses.
5. The declared constructor-state boundary survived all 288 changed-frontier transplants.
6. Exact hidden-transformation recovery was unnecessary for frontier expansion in 52 expansion units.

---

## 10. What was falsified or constrained

A2-V0 directly rules out the following universal statement **within this assay**:

\[
\boxed{
F\Rightarrow\Phi_B(G^{+F})\supseteq\Phi_B(G^{-F}).
}
\]

The 18 contractions and 16 tradeoffs are counterexamples.

The result also blocks the informal substitution

\[
\text{better deployment score}
\equiv
\text{monotonically greater corrective capacity}
\]

inside A2-V0, because 10 tradeoff units have positive deployment contrast while still losing some correctable uncertainty sets.

The result does **not** falsify the MATRIX₀ kernel. The kernel explicitly permits both `Δ+` and `Δ-` and was designed to preserve such negative structure rather than force monotonicity.

---

## 11. What is not earned

The execution does not establish:

- general self-improvement;
- general corrigibility;
- open-ended policy invention;
- unfamiliar-error discovery;
- population-level claims outside the declared finite unit universe;
- universal benefit of feedback;
- universal harm of feedback;
- independence of future viability from corrective topology;
- a unique causal mechanism through `g`, `Q`, or `Π`;
- a general theory of approximate representations;
- MATRIX₁ or any new kernel object.

No README change is warranted merely by this execution.

---

## 12. Frozen claim ceiling

The strongest supported result statement is:

> **Within the 320 previously unresolved units of A2-V0, feedback produced counterfactually attributable changes in the system-realizable corrective frontier in 288 units: 254 expansions, 18 contractions, and 16 tradeoffs; 32 units were unchanged. The result demonstrates treatment sensitivity of the corrective frontier, including losses, under the frozen finite causal assay.**

A second, separately supported statement is:

> **Monotone corrective expansion is false in A2-V0: 34 previously unresolved units exhibit corrective loss (`Δ-≠∅`).**

Both claims are assay-local.

---

## 13. Updated MATRIX research standing

```text
MATRIX₀
│
├── Attack 1 — semantic/oracle adequacy
│   └── CLOSED / survived under EXEC_V1 contracts
│
├── Attack 2 — causal identification
│   └── CLOSED / causal cage frozen
│
├── A2-PREREG-V0
│   └── FROZEN
│
├── A2-V0 implementation
│   ├── 17/17 tests PASS
│   ├── 64/64 theorem controls MATCH
│   ├── 19/19 invariant checks PASS
│   └── VALIDATED
│
└── A2-V0 scientific execution
    ├── unresolved units 320/320 EXECUTED
    ├── EXPANSION    254
    ├── NULL          32
    ├── CONTRACTION   18
    ├── TRADEOFF      16
    ├── Δ+ nonempty  270
    ├── Δ- nonempty   34
    └── COMPLETE
```

The methodological ladder is now:

\[
\boxed{
\text{semantic adequacy}
\checkmark
\rightarrow
\text{causal identification}
\checkmark
\rightarrow
\text{finite scientific execution}
\checkmark
\rightarrow
\text{no conceptual promotion unless subsequently forced}.
}
\]

MATRIX₀ has survived a formal attack and a finite empirical assay, while the empirical assay simultaneously constrained any monotonic-improvement reading by producing real contractions and tradeoffs.

---

## 14. Record discipline

This result is intentionally source-controlled because it materially changes the empirical standing of the program.

The governing archival rule is:

\[
\boxed{
\text{important scientific / operational / epistemic state}
\rightarrow
\text{repo with provenance and claim ceiling}.
}
\]

The record preserves negative results and losses as first-class scientific output. No later synthesis should erase the 34 loss-bearing units or relabel theorem-derived controls as empirical discoveries.
