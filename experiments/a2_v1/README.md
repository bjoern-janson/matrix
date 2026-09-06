# A2-V1 archive index

**Active-Survivor Priority × Encounter-Order Factorial.**  
**Current standing:** **COMPLETE / SCIENTIFIC INTERPRETATION ADMITTED**.

This directory preserves the full A2-V1 lifecycle without rewriting earlier stages to sound as if they knew the later result.

## Current authorities

- [`../A2_V1_RESULT.md`](../A2_V1_RESULT.md) — authoritative scientific result and claim ceiling.
- [`STATUS.json`](STATUS.json) — current machine-readable standing: 2,176 reference pairs matched, 7,040 / 7,040 prospective pairs executed, scientific interpretation `ADMITTED`.
- [`CURRENT_STATE.md`](CURRENT_STATE.md) — current earned/not-earned program state and explicit statement that no next assay is frozen here.
- [`EXECUTION_CUSTODY.md`](EXECUTION_CUSTODY.md) — current execution/result custody, recovery instructions and exact repository-resident output identities.
- [`result/receipt.json`](result/receipt.json) — final machine receipt.
- [`result/primary.json.gz`](result/primary.json.gz) — deterministic lossless compression of the exact 9,216-row primary map.
- [`result/derived.json`](result/derived.json) — exact preregistered sensitivity/effect-modification/loss-persistence memberships and witnesses.
- [`execution/artifacts/a2-v1-prospective-output.tar.gz`](execution/artifacts/a2-v1-prospective-output.tar.gz) — exact complete scientific output and execution-log archive from the admitted run.

## Lifecycle

### 1. Mathematical audit — historical pre-preregistration stage

- [`audit/A2_V1_PRIORITY_MATHEMATICAL_AUDIT.md`](audit/A2_V1_PRIORITY_MATHEMATICAL_AUDIT.md) — corrected mathematical audit.
- [`audit/ERRATUM.md`](audit/ERRATUM.md) — one transcription correction; mathematical outputs unchanged.
- [`audit/PRIORITY_FAMILY_AUDIT.json`](audit/PRIORITY_FAMILY_AUDIT.json) — 48 conjugations, 24 distinct priorities, inverse ranks and group checks.
- [`audit/THEOREM_CONTROL_PREDICTIONS.json`](audit/THEOREM_CONTROL_PREDICTIONS.json) — 1,536 analytic control predictions.
- [`audit/audit_priority_family.py`](audit/audit_priority_family.py) — standalone mathematical enumeration only.
- [`audit/packages/`](audit/packages/) — byte-preserved original and corrected audit packages.

The historical audit's candidate/pre-registration labels remain unchanged. The later preregistration adopted its exact priority arrays; the audit itself is not rewritten as a scientific result.

### 2. Frozen preregistration

- [`../A2_PREREG_V1.md`](../A2_PREREG_V1.md) — authoritative prospective protocol.
- [`PREREG_CONTRACT.json`](PREREG_CONTRACT.json) — machine-readable constants, strata, gates and endpoint definitions.
- [`CUSTODY.md`](CUSTODY.md) — **historical preregistration-stage custody**. Its statements that implementation/validation/science had not yet occurred were correct at that commit and are intentionally preserved.
- [`ARCHIVE_SHA256SUMS.txt`](ARCHIVE_SHA256SUMS.txt) — preregistration archive identities.

The frozen 9,216-cell design partitions into 1,536 theorem controls, 320 historical P0 references, 320 covariance-derived P3 references and 7,040 prospective targets. The mandatory fresh 2,176-reference gate remained binding for the science command.

### 3. Implementation and validation — historical validation-only stage

- [`implementation/README.md`](implementation/README.md) — validated implementation-stage index.
- [`implementation/STATUS.json`](implementation/STATUS.json) — **historical validation-only terminal status**: 30 tests PASS, 2,176 / 2,176 references matched, zero prospective pairs, science `NOT_RUN` at that stage.
- [`implementation/evidence/CUSTODY.json`](implementation/evidence/CUSTODY.json) — validation review/evidence hash authority.
- [`implementation/evidence/INITIAL_REVIEW.md`](implementation/evidence/INITIAL_REVIEW.md) — initial independent review and concrete defects.
- [`implementation/evidence/IMPLEMENTATION_REPORT.md`](implementation/evidence/IMPLEMENTATION_REPORT.md) — correction/implementation record.
- [`implementation/evidence/FINAL_REVIEW.md`](implementation/evidence/FINAL_REVIEW.md) — independent rereview PASS.
- [`implementation/evidence/controller_audit.py`](implementation/evidence/controller_audit.py) — independent paired-call observer.
- [`implementation/evidence/software_test_audit.json`](implementation/evidence/software_test_audit.json) and [`validation_call_audit.json`](implementation/evidence/validation_call_audit.json) — exact software/reference audit records.
- [`implementation/evidence/independent_references.zip`](implementation/evidence/independent_references.zip) — exact independent reference endpoints.
- [`implementation/evidence/validation_run.zip`](implementation/evidence/validation_run.zip) — exact complete validation-only archive.
- [`implementation/evidence/REMOTE_CUSTODY.md`](implementation/evidence/REMOTE_CUSTODY.md) — **historical remote validation-only anchoring record**. Its `NOT_RUN` language is not the current assay standing.

### 4. Scientific execution

- [`execution/GITHUB_ACTIONS_WORKFLOW.yml`](execution/GITHUB_ACTIONS_WORKFLOW.yml) — inert exact copy of the successful science workflow.
- [`execution/artifacts/`](execution/artifacts/) — exact sealed complete-output tarball and checksum sidecar.
- [`execution/logs/`](execution/logs/) — test, prospective-run, environment, memory, disk and swap logs from the successful run.
- [`EXECUTION_CUSTODY.md`](EXECUTION_CUSTODY.md) — source/run/job/artifact identities, exact hashes and recovery procedure.

The workflow checked out canonical source commit `2b79c73dd9ac46fd6f693fd35d63c44cbb396a40`, reran the 30-test software suite and fresh 2,176-reference gate, then executed exactly 7,040 prospective pairs.

### 5. Scientific result

The final result is [`../A2_V1_RESULT.md`](../A2_V1_RESULT.md). The complete primary map and registered derived structures are now directly recoverable from the repository rather than depending on the original expiring GitHub Actions artifact.

The exact preregistered counts are:

```text
E_K      912 / 960
E_P      270 / 320
E_PK      40 / 40
L_any_P    0
L_common_P 0
L_any_K    0
L_common_K 0
```

These are finite-assay results under the frozen claim ceiling, not a general adaptation or corrigibility law. `MATRIX_1` remains **NOT EARNED**.

## Historical-state rule

Files are not rewritten merely because the program advanced. In particular, preregistration-stage and validation-only files can correctly say `NOT_RUN` or zero prospective executions. **Current** A2-V1 standing is defined by this index, [`STATUS.json`](STATUS.json), [`CURRENT_STATE.md`](CURRENT_STATE.md), [`../A2_V1_RESULT.md`](../A2_V1_RESULT.md), and [`EXECUTION_CUSTODY.md`](EXECUTION_CUSTODY.md).

No file in this archive consolidation changes the MATRIX conceptual kernel, `formalization/EXEC_V1.md`, either preregistration, or any A2-V1 scientific value/claim ceiling.
