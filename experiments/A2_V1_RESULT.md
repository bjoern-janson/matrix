# A2-V1 — Active-Survivor Priority × Encounter-Order Factorial — Result

Status: **COMPLETE / SCIENTIFIC INTERPRETATION ADMITTED**

This record reports the frozen A2-V1 assay preregistered in `experiments/A2_PREREG_V1.md`. The execution used canonical MATRIX state `2b79c73dd9ac46fd6f693fd35d63c44cbb396a40`, Python `3.12.13`, and validated source digest `ea204bad2519f6759f6e5ef1dadd405b7043fe8277e6b5ebbfa3cace09c1c31c`.

The fresh in-process science gate passed before any prospective target entered:

- theorem controls: **1,536 / 1,536 matched**;
- historical P0 references: **320 / 320 matched**;
- covariance P3 references: **320 / 320 matched**;
- prospective target entries before gate completion: **0**.

The controller then executed exactly **7,040 / 7,040** prospective target pairs and sealed a complete **9,216-row** primary map. All final invariant and seal stages completed. The final receipt records `status=COMPLETE` and `scientific_interpretation=ADMITTED`.

## Preregistered exact derived structures

Scientific reporting domain: the 40 noncontrol worlds `h = 8..47`, 24 frozen conjugation-generated priorities, and eight cyclic encounter rotations.

| Structure | Exact result | Universe |
| --- | ---: | ---: |
| Encounter-order sensitivity `E_K` | **912** | 960 `(h,P)` pairs |
| Priority sensitivity `E_P` | **270** | 320 `(h,k)` pairs |
| Priority × encounter effect modification `E_PK` | **40** | 40 worlds |
| `L_any_P` | **0** | 320 `(h,k)` pairs |
| `L_common_P` | **0** | 320 `(h,k)` pairs |
| `L_any_K` | **0** | 960 `(h,P)` pairs |
| `L_common_K` | **0** | 960 `(h,P)` pairs |

Thus, within the frozen family:

1. encounter order changes the exact feedback-frontier contrast for **912/960** fixed `(h,P)` slices;
2. active-survivor priority changes the exact feedback-frontier contrast for **270/320** fixed `(h,k)` slices;
3. the consequence of encounter order is priority-dependent in **every one of the 40 noncontrol worlds**;
4. no fixed `(h,k)` loses something under all 24 priorities, and no fixed `(h,P)` loses something under all eight encounter rotations;
5. consequently, there is no correction opportunity whose loss persists across all priorities at fixed `(h,k)`, nor across all rotations at fixed `(h,P)`.

The third statement is effect modification, not a unique additive decomposition or a percentage attribution between the two factors.

## Descriptive finite class counts

These class counts are secondary descriptions of the exact set-valued primary map; they do not replace it.

| Stratum | Expansion | Null | Contraction | Tradeoff | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| THEOREM_CONTROL | 1,344 | 192 | 0 | 0 | 1,536 |
| HISTORICAL_P0 | 254 | 32 | 18 | 16 | 320 |
| COVARIANCE_P3 | 254 | 32 | 18 | 16 | 320 |
| PROSPECTIVE_TARGET | **5,376** | **860** | **516** | **288** | **7,040** |
| Noncontrol total | **5,884** | **924** | **552** | **320** | **7,680** |

P0 and P3 retain their historical/theorem-covariance provenance; they are not 640 new discoveries.

## Answer to the A2-V1 causal target

The remaining A2-V0 seam is now localized more sharply:

```text
fixed frontier semantics
        +
active-survivor priority
        ×
cyclic encounter order
        ↓
exact corrective-frontier contrast
```

Both controlled factors matter, and their interaction matters throughout the noncontrol world family. At the same time, loss is not invariant to either complete tested factor family: for every fixed `(h,k)` there is at least one tested priority with no loss, and for every fixed `(h,P)` there is at least one tested rotation with no loss.

This means A2-V0's loss/tradeoff structure is not correctly localized to encounter order alone or to the frozen lexicographic priority alone. Within this assay it is contingent on the joint priority × encounter trajectory.

## Claim ceiling

This result is exact for:

- the finite signed-permutation world and frozen A2 semantics;
- the 24 conjugation-generated identity-first active-survivor priorities;
- the eight cyclic encounter rotations;
- the frozen version-space elimination learner and constructor/frontier definitions.

It does **not** establish results for arbitrary identity-first rankings, all `8!` encounter orders, arbitrary search policies, other learners, general corrigibility, or a general law of adaptation. It does **not** by itself earn `MATRIX_1`.

## Primary custody

- final receipt SHA-256: `4b41b91ea06af7d5f9b77ee33b523bdb178f7c321c17af8aa33dcdd546aa44f2`
- primary JSON SHA-256: `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076`
- derived JSON SHA-256: `7b298eef81996ab804c09c5a4d8756d7fbd8842843bcef7a30b9de160f64e10b`
- raw evidence JSON SHA-256: `6e3188b33a2640133cbdd4b9d91b48513cbd2dfc80c96c21efb561932961c1d1`
- fresh validation receipt SHA-256: `cfb9e62c8c69477d5ac4717cdb7e2dfa6013078d14a544e8e63262ce4b110be7`

## GitHub Actions execution custody

- execution branch: `science/a2-v1-prospective-20260906`
- workflow commit: `1f8052ad592b7ac1fe502574774b9c6e20100ec4`
- workflow run ID: `34045071131`
- workflow job ID: `101518572282`
- run conclusion: `success`
- GitHub Actions artifact ID: `9992901892`
- artifact name: `a2-v1-prospective-34045071131`
- GitHub artifact digest: `sha256:17fbf854084a023c8d15a55e185bbe8e31d68d2087ebe05da7fa2c2fae68f11e`
- artifact expires: `2026-12-05T16:19:33Z`

The workflow checked out canonical commit `2b79c73dd9ac46fd6f693fd35d63c44cbb396a40` rather than executing the workflow branch's source tree. Before science, it reran the 30-test suite and the fresh 2,176-cell reference gate.

Inside the Actions artifact, `a2-v1-prospective-output.tar.gz` has SHA-256 `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7` and contains the complete scientific output directory plus execution logs.

Deterministic repository compression of the complete primary map with `gzip -n -9` has SHA-256 `a317bf081407694cefe2e84b97bfdbd845eef1077a7b92c6328785b565c6e8b3`; decompression yields `primary.json` with the receipt-bound SHA-256 above.

## Execution resource record

- software suite: `30/30` passed before execution
- prospective command exit status: `0`
- prospective command wall time: `3:32.69`
- maximum resident set: `7,818,540 KiB`
- configured swap: 6 GiB
- recorded swaps during command: `0`

The earlier local 4-GiB OOM attempt is not a scientific result and is not combined with this run.

## Raw evidence storage note

The exact full raw evidence is 583,344,614 bytes uncompressed and is hash-bound above. The complete scientific output remains in the sealed GitHub Actions artifact identified above; this repository record preserves the admitted result, exact artifact identities, source binding, decision boundary, and claim ceiling. No regenerated or substituted scientific output is used here.

## Repository-resident archival addendum

This addendum records a **custody-only consolidation performed after the admitted result**. It does not alter the preregistration, execution, reported values, interpretation, or claim ceiling above.

The successful Actions artifact was originally retention-limited. Exact admitted execution bytes are now durably repository-resident under [`a2_v1/execution/`](a2_v1/execution/):

- [`a2_v1/execution/artifacts/a2-v1-prospective-output.tar.gz`](a2_v1/execution/artifacts/a2-v1-prospective-output.tar.gz) is the exact sealed output tarball, SHA-256 `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7`;
- [`a2_v1/result/primary.json.gz`](a2_v1/result/primary.json.gz) is deterministic compression of the exact 9,216-row primary map; decompression yields canonical SHA-256 `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076`;
- [`a2_v1/result/derived.json`](a2_v1/result/derived.json) preserves the exact preregistered membership/witness structures, SHA-256 `7b298eef81996ab804c09c5a4d8756d7fbd8842843bcef7a30b9de160f64e10b`;
- [`a2_v1/execution/GITHUB_ACTIONS_WORKFLOW.yml`](a2_v1/execution/GITHUB_ACTIONS_WORKFLOW.yml) is an inert copy of the exact successful science workflow;
- [`a2_v1/EXECUTION_CUSTODY.md`](a2_v1/EXECUTION_CUSTODY.md) records complete recovery/provenance details.

The original Actions artifact remains provenance, but it is no longer required for scientific-output availability. Historical validation-only records remain historical and are not rewritten into post-execution standing.
