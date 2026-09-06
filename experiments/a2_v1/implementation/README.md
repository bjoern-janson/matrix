# A2-V1 frozen assay software

**Current standing: implementation reviewed; validation-only gate PASS; prospective science NOT RUN.**

The controller reproduced all 1,536 theorem signatures, 320 historical P0 endpoints, and 320 covariance P3 endpoints. An external paired-call observer independently matched all 2,176 endpoints and blocked nonreference execution. All 30 software tests passed. Exactly zero prospective pairs were executed. See [STATUS.json](STATUS.json), [validation receipt](evidence/validation_receipt.json), and [custody manifest](evidence/CUSTODY.json).

The complete raw validation attempt is retained in [validation_run.zip](evidence/validation_run.zip), including pre-execution seals, all trajectories, policy executions, subset witnesses, transplant measurements, and invariant checks. [Initial review](evidence/INITIAL_REVIEW.md), [correction report](evidence/IMPLEMENTATION_REPORT.md), and [final static review](evidence/FINAL_REVIEW.md) preserve the review history. The older parent status files describe the immutable preregistration snapshot. This implementation record adds the later validation state.

To reproduce the independently guarded validation, extract [independent_references.zip](evidence/independent_references.zip) into a temporary directory and run from this implementation directory:

```sh
python3 evidence/controller_audit.py validate --implementation . --reference /ABSOLUTE/TEMP/independent_reference_endpoints.json --audit /ABSOLUTE/NEW/call_audit.json --output /ABSOLUTE/NEW/validation
```

The output directory must not already exist. This command executes only the reference gate. These reference reproductions are software validation, not prospective discoveries. The authorized terminal state is validation-only completion.

This standard-library package implements `A2-PREREG-V1`. It pins and hashes the frozen model, contract, priority audit, theorem predictions, and historical compact primary before paired execution. Priority selection uses original hypothesis IDs ranked by the frozen 24 conjugated orders. Each paired cell is executed by `a2_v1.engine.execute_paired_cell(unit, authorities)`; its explicit `(h, P, k)` unit argument permits independent call profiling.

From this directory, run focused software tests with:

```sh
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

The validation CLI defaults to validation and requires a new output directory:

```sh
PYTHONPATH=. python3 -m a2_v1 --output OUTPUT_DIRECTORY
PYTHONPATH=. python3 -m a2_v1 validate --output OUTPUT_DIRECTORY
```

Validation freshly executes only the 1,536 theorem controls, 320 historical P0 references, and 320 covariance P3 references, in that order. It writes canonical, exclusive-create `evidence.json` and `receipt.json` files. Evidence retains per-unit trajectories, constructor states, nine-policy/eight-state executions, subset witnesses, invariant records, hashes, phases, and counters. Runtime evidence is excluded from the source digest.

The separately named future science command is:

```sh
PYTHONPATH=. python3 -m a2_v1 run-prospective --output NEW_OUTPUT_DIRECTORY
```

It cannot consume a stored PASS. In its own process it compiles and seals references, reruns and seals the full fresh validation gate under `validation/`, and only then reaches prospective cells. A complete run seals raw evidence, the exact 9,216-row primary map, registered derived structures bound to the primary hash, and a final receipt. Any mismatch writes `INVALID_NO_SCIENTIFIC_RESULT`, retains diagnostic counters, and stops. This delivery does not authorize or perform prospective execution.

Review corrections seal `source_manifest.json`, `unit_manifest.json`,
`expected_references.json`, and `preparation.json` before the first paired call.
The manifest covers all package Python modules, focused test modules, protocol,
contract, audits, historical input, and original model. Authorities are recursively
immutable. Sources, authority identities, and all accumulated artifact hashes are
reverified before validation PASS, after writing that receipt (before target
entry), and before/after final seals. The primary rows are globally lexicographic;
raw evidence remains in execution phase order.

Evaluation imports the original V0 model from its SHA-256-verified source bytes.
Only its `ConstructorInput(task, active)` reaches `realize`; each policy's
`action(observations)` is driven by its original `execute` environment. Every
changed pair actually replaces the recipient constructor's active field with the
donor's active field and realizes/executes all nine policies in each direction.
`transplants` retains both complete measurements. Independent checks derive
observations and decoder predictions through a separate forward-map enumeration,
validate the continuous live-state chain, and compare all execution fields and
complete witness sets. They never rewrite recorded ranks or call learner updates.

On a caught fault, `diagnostics.json` retains completed records, the failing
record, completed/failing invariant evidence, and current pair context.
`InvalidAssay.partial_record` from the engine includes completed arm trajectories,
current training episode, frozen constructor when reached, and completed policy
executions plus the in-progress policy/state boundary. If the original executor
raises before returning, no execution result for that in-progress policy/state is
invented. `entered` counts boundary entries; `counters` counts returned pairs,
including a returned pair whose checks fail. `invalid_receipt.json` binds these
diagnostics. It always invalidates the attempt, including any earlier receipt;
an existing file is never overwritten. When no root receipt exists, the invalid
receipt is also written as `receipt.json`. Restart requires a new directory and a
fresh gate. Hard process termination or an unwritable filesystem cannot produce
a completed receipt and must never be resumed as a valid attempt.
