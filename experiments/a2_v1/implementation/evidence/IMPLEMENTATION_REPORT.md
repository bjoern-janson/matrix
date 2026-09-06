# Task 1 implementation report

## Status and scope

Implemented the frozen A2-V1 standard-library package and focused tests under `experiments/a2_v1/implementation/`. No real `PROSPECTIVE_TARGET` cell was executed. No 2,176-cell validation run was executed. Reference smoke execution was limited to `(0,0,0)`, `(1,7,2)`, `(8,0,0)`, and `(8,3,4)`.

Local implementation commit: `074be27a` (`Implement frozen A2-V1 validation software`).

The independently profileable pair boundary is:

`a2_v1.engine.execute_paired_cell(unit, authorities)`

`unit` is the explicit `(hypothesis_index, priority_id, rotation)` tuple.

## RED evidence

Initial command:

`PYTHONPATH=. python3 -m unittest discover -s tests -v`

Initial result: 1 test module error, `ModuleNotFoundError: No module named 'a2_v1'`. This was the expected absence-of-feature failure before production code existed. Subsequent green work exposed and fixed independent priority-order checking, exception identity, clone provenance, and measurement witness defects without weakening assertions.

## Specification coverage

| Frozen requirement | Implementation | Behavioral evidence |
|---|---|---|
| Pinned inputs, 48 hypotheses, 24 priorities, exact strata | `authorities.load_authorities` | authority corruption, historical seal, counts/partition |
| Independent historical and covariance references | `reconstruct_historical`, `compile_p3` | sealed hash and engine-call prohibition |
| Priority-aware survivor selection | `engine.Learner.active` | `{8,11}` under P1 selects 11 |
| Equality update; invalid token discards proposal; real full scan | `Learner.update` | state preservation, truth retention, 48 checks |
| Isolated paired eight-episode execution | `execute_paired_cell`, `_arm` | reference-only smoke and pair checks |
| 40 charge and 384 checks per arm | `engine` plus `checks.check_pair` | invariant and charge mutation |
| Exact constructor boundary and nine policies | `_arm`, `_measure`, `check_pair` | constructor mutation, policy/action/cost checks |
| All states/subsets and common-policy witnesses | `_measure`, independent oracle in `checks` | frontier and witness mutations |
| Directed differences and transplant boundary | `check_pair` | exact set comparisons on changed cells |
| Ordered fresh reference gate and zero-target validation | `runner._run_gate`, `validate` | separate phase mismatch tests and call census |
| Immutable output and stored-PASS rejection | exclusive `_seal`, directory creation | duplicate directory and preexisting receipt tests |
| Future science path | `run_prospective` | only failure/phase behavior tested; no target cell run |
| Exact sensitivity/effect modification | `derived.derive` | explicit synthetic frontier map and witnesses |
| Any/common loss distinction and families | `derived.derive` | synthetic unequal-loss intersection fixture |
| Canonical, hash-bound output order | `runner` | fresh validation seal precedes targets; primary precedes derived |

Section 8 mappings: (1) `load_authorities`; (2) pair clone fields and `check_pair`; (3–7) learner traces plus independent update/rank checks; (8) exact constructor-key check; (9–10) execution rows, costs, witnesses, and independent frontier oracle; (11) frozen snapshot and runner baseline census; (12) directed-difference check; (13) independent bidirectional constructor reconstruction; (14) runner phase counters, immutable seals, unit uniqueness/coverage, and source/reference identities.

## Output contracts

Validation writes canonical exclusive-create `evidence.json` and `receipt.json`. Evidence retains complete arm traces, constructors, final live sets, executions, subset witnesses, invariant records, and authority identities. Validation receipts bind the evidence hash, source digest, phase list, exact counters, runtime, and validation-only standing.

The future science command creates and seals `validation/evidence.json` and `validation/receipt.json` before target entry, then writes combined raw evidence, the exact primary row map, derived structures bound to the primary SHA-256, and the final receipt. Failures retain an immutable `INVALID_NO_SCIENTIFIC_RESULT` receipt and counters.

The source digest covers all `a2_v1/*.py`, `tests/test_*.py`, the frozen preregistration and machine contract, priority and theorem audit JSON, historical compact primary, and pinned V0 model. Paths are stable repository-relative names. Generated runtime evidence and README prose are excluded.

## Commands and results

- `PYTHONPATH=. python3 -m unittest discover -s tests -v` from the V1 implementation directory: 13 tests, PASS.
- `PYTHONPATH=. python3 -m unittest discover -s tests -v` from the V0 implementation directory: 17 tests, PASS.
- `python3 -m compileall -q a2_v1 tests && git diff --check`: exit 0.

## Concerns

The full 2,176-reference validation gate remains intentionally unexecuted for independent controller profiling. The future 7,040-target path is implemented but has never been entered successfully. Final confidence in complete-gate runtime and output volume depends on the controller-owned run.

## Independent-review fix wave — 2026-09-06

Status: all C1/C2/I1–I6 findings addressed in local commit
`929d384972f9bffd12a8380c8204600d3a393941`
(`Close A2-V1 trajectory, policy boundary and custody review defects`). The prior
implementation commit is correctly `074be27bda227a22d3509cdaeb7a432f41506aa9`;
the shortened `074be27a` above was a reporting typo. This appendix supersedes the
prior assurance claims that the independent review found unsupported.

No protocol, contract, V0 source, prior endpoint, or other file present at the
frozen base was modified. No push, merge, full real 2,176-reference gate, or real
PROSPECTIVE_TARGET execution occurred. No subagents were used by this implementer.
Only reference cells were executed by the real paired engine. Across this wave's
tests the distinct real units are `(0,0,0)`, `(1,1,0)`, `(1,7,2)`, `(8,0,0)`,
`(8,3,0)`, and `(8,3,4)`. The earlier report omitted the permitted theorem mutation
cell `(1,1,0)`; it is explicitly included here. Synthetic controller tests traverse
reference manifests with boundary fakes; one fresh-science test reaches a fake
first-target sentinel that raises before any real engine call.

### TDD and verification evidence

Before production changes, `test_review_regressions.py` was added and run with:

`PYTHONPATH=experiments/a2_v1/implementation python3 -m unittest discover -s experiments/a2_v1/implementation/tests -p test_review_regressions.py -v`

The initial seven regression tests reported `FAILED (failures=12, errors=3)`:
unchecked trajectory/rank/evaluation/witness mutations did not raise,
`transplants` and protocol pin were absent, and preparation/partial faults had no
receipt/diagnostic file. After the trajectory and execution corrections, the
same tests reduced to the three missing controller diagnostic errors. The next
controller regression wave reported `FAILED (failures=5, errors=3)` before the
runner changes: exact-coverage, lexicographic-primary and seal-verification helpers
were absent, source changes admitted validation, and the fresh-science fake
boundary flow was unsupported. Additional real-engine fault regressions first
failed with missing `current_episode`, then missing measurement
`current_execution`; both contexts were added and verified. Intermediate command
path mistakes and a synthetic fixture missing its stratum were corrected without
weakening production checks.

Final exact command from `experiments/a2_v1/implementation/`:

`PYTHONPATH=. python3 -m unittest discover -s tests -v`

Result: **30 tests, PASS, 29.532 seconds**, final log `/tmp/a2-v1-final-tests.log`.
`python3 -m compileall -q a2_v1 tests` and `git diff --check` each exited zero.
The full validation gate remains exclusively controller-owned; these focused test
results are not a validation receipt or a scientific result.

### Review-to-implementation/test mapping

| Finding | Correction | Focused evidence |
|---|---|---|
| C1 | Checker starts from all 48 live IDs, follows every before/after state continuously, checks exact pinned priority for unit P, predicts via an independent forward-map inverse, validates actual correctness and feedback, every step's work, final live/active constructor linkage, and freeze snapshots. No evidence rank rewriting remains. | `test_disconnected_or_falsified_trajectory_rejected`, existing reference smoke and update tests |
| C2 | New `frozen_model.py` verifies original model bytes before executing that module. Measurement calls its actual `ConstructorInput`, `realize`, `RealizedPolicy.action` and `execute`; checker independently compares every action, observation, success, cost, provenance and complete witness list. Primary arm fields must equal measurement frontiers. Both donor-to-recipient directions actually realize/execute the recipient constructor after replacing its active field. | `test_execution_and_complete_witness_linkage`, `test_transplants_are_actual_executions`, reference smoke |
| I1 | Canonical source, all-four-strata unit manifest, exact three reference tables, and a preparation manifest binding their hashes are exclusively created and verified before pair entry. Expected tables are recursively frozen in memory. | `test_seals_precede_first_pair_and_failure_retains_record` |
| I2 | Protocol SHA-256 pinned; nested authority dictionaries become read-only mappings and arrays become tuples. Source manifest retained. Source digest, manifest, freshly loaded authority identity, and all accumulated artifact hashes rechecked before validation PASS, after receipt/before target entry, and around final seals. | `test_nested_authorities_immutable_and_protocol_pinned`, `test_source_change_blocks_validation_pass_and_target_entry`, `test_seal_reverification_rejects_changes`, `test_seal_change_after_gate_prevents_target_entry` |
| I3 | Failure scope begins before authority preparation. Returned records are appended before invariants/reference matching. Entry/return counters are separate. Engine failures expose partial records; diagnostics retain prior and failing records/checks plus in-progress context. Invalid receipt is always created and never overwrites an earlier receipt. | preparation/failing-record/partial-execution regressions, real training/evaluation fault tests |
| I4 | `_primary(records)` sorts all combined rows lexicographically; raw execution evidence remains in phase order. | `test_primary_is_lexicographic` with intentionally interleaved synthetic phase rows |
| I5 | Requested/returned identity and exact stratum checked before matching; declared manifests and compiled-reference key sets checked before execution; exact set coverage, uniqueness, universe, stratum, per-world control baseline and counters checked after references and across the full final map. | `test_coverage_exact_and_full_map_baseline`, preparation/failure tests, synthetic controller census |
| I6 | Added 17 regression tests. Three production reference-mismatch tests use actual checked reference pairs at the failure boundary and unmodified `_match_reference`, with earlier expensive pair boundaries synthesized. Fresh science demonstrably repeats phase order before its fake target sentinel. Exact effect-modification and encounter common/any-loss assertions added. | `test_production_reference_matching_each_phase_with_real_checked_failure_cell`, `test_fresh_science_gate_order_and_stops_at_synthetic_target_boundary`, `test_derived_effect_witness_and_both_encounter_loss_structures` |

Section 8 mapping after fixes: (1) authority loader plus preparation manifest;
(2) new per-call learner clones plus continuous pinned state-chain checks;
(3) complete step schedule/work and arm totals; (4) independent selected-decoder
prediction/correctness/token comparison; (5) independent live-set recurrence,
truth retention and unchanged control recurrence; (6) frozen rank identity and
selection/monotonicity; (7) independent mathematical inverse/equality recurrence
and active-preservation/removal conditions; (8) pinned restricted constructor and
policy boundary; (9) exact policy/trace/cost/witness comparison; (10) all states,
policies, subsets, independent algebraic frontier and downward closure;
(11) frozen snapshots plus reference/full-map baseline census; (12) unconditional
measurement-primary linkage and exact directed differences; (13) actual retained
bidirectional transplant executions with independent verification;
(14) immutable preparation, counters, exact identity/coverage, source/seal checks
and diagnostic invalidation.

### Interfaces, records, and fault semantics

The exact profileable paired execution boundary is unchanged:

`a2_v1.engine.execute_paired_cell(unit, authorities)`

Its first argument is the explicit original `(h, priority_id, rotation)` tuple.
This is the sole function that performs paired training. Transplant measurement
calls `_measure` within that same pair and never invokes another paired cell.
`check_pair(pair, authorities=None)` accepts the prepared immutable authority
object to avoid reloading per cell; standalone calls load the pinned authorities.
It does not call the production decoder/update or change recorded rank evidence.

`frozen_model.model` is the original V0 model compiled from the very bytes whose
SHA-256 was checked, under the dedicated `a2_v1._verified_v0_model` module name.
Only `ConstructorInput(task, active)` reaches `realize`; action sees observations
only; hidden world/state belong to `execute`. Every measurement records all nine
policy declarations and 72 completed executions. A changed pair adds
`transplants.control_to_treatment` and `transplants.treatment_to_control`, each
with donor/recipient labels, untouched recipient constructor, transplanted
constructor, and complete measurement. Independent checks compare those traces,
then require the donor frontier exactly.

Raw runner evidence schema is now `/2`. Its `checks` list groups evidence per
unit as `{unit, checks, reference_match}`; a failed check may also retain `error`.
Pair records add before/after frozen snapshots and transplant measurements.
Reference compilation files are canonical ordinary JSON; their in-memory forms
are immutable recursively. The manifest contains all four strata (including
only target identities, no target trajectories/endpoints), while expected
references contain only the 2,176 designated reference rows.

`entered` increments immediately before each engine boundary call. `counters`
increments immediately on return, even if that record subsequently fails.
Engine exceptions are wrapped in `InvalidAssay` with `partial_record`: completed
arm traces, current training episode if updating, constructor/final state if
frozen, and completed policy executions with current policy/state boundary if a
policy execution raises. No result or partial internal action list is invented
for an original executor call that never returned. Checker failures attach
`partial_checks` containing preceding PASS entries and the failing invariant.
The runner writes `diagnostics.json`, binding its hash in
`invalid_receipt.json`; it also writes root `receipt.json` if that name is still
absent. A late failure preserves all earlier files, including a validation PASS,
but the invalid receipt invalidates the whole attempted run. Any hard process
termination/unwritable filesystem lacks a completed valid receipt and cannot be
resumed as an admitted attempt.

The source digest includes all current package `.py` files (including the new
verified-loader module), all `test_*.py` files, and every frozen PATHS input,
including protocol and original model. Generated evidence and documentation
are excluded. `source_manifest.json` preserves the exact relative-path/hash map;
`preparation.json` binds its hash, the unit/reference hashes and authority IDs.
Receipts bind accumulated artifact hashes, and newly created receipts are
reverified against their in-memory seal values before successful return.

### Remaining boundary

No known review defect remains unresolved in this implementer's focused checks.
Independent rereview is still required. Runtime and resource behavior of the
complete real 2,176-reference gate is intentionally unverified here and remains
controller-owned. The prospective scientific command remains unexecuted with
real targets. Nothing in this report grants that execution or interprets partial
or synthetic records scientifically.
