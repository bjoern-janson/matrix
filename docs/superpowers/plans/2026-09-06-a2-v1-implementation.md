# A2-V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Implement the frozen A2-V1 assay and establish software correctness plus the validation-only 2,176-pair gate, with zero prospective scientific executions.

**Architecture:** A standard-library Python package binds immutable preregistration/reference inputs, implements priority-aware selection using the frozen V0 execution semantics, and checks execution against independent mathematical oracles. An explicit phase controller gates scientific execution and records complete hash-bound evidence. The controller will run validation only after software review.

**Tech Stack:** Python 3.12 standard library, unittest, git. No dependency installation or external research is needed.

**Spec:** `experiments/A2_PREREG_V1.md`, companion `experiments/a2_v1/PREREG_CONTRACT.json`, base commit `374c58a4b21118a89173d1412d8b4b9e1f0a1dd6`.

## Global Constraints

- Preserve every existing file at the base commit, including historical status and archive checksums. New implementation status belongs under `experiments/a2_v1/implementation/`.
- No scientific choices: use the frozen 24 priority ranks, eight rotations, equality update, nine policies, budget 5, charge 40 and 384 hypothesis checks per arm.
- Canonical source IDs and immutable P0/P3/theorem inputs must be checked before any paired execution. Expected references cannot use the V1 learner/evaluator to manufacture expectations.
- The future science command reruns 1,536 theorem controls, 320 P0 references, 320 P3 references, and all invariants in-process before any of 7,040 targets. A cached PASS cannot bypass this.
- This task may execute reference cells or synthetic software fixtures only. Neither tests nor development scripts may execute a real prospective target. The final full validation is owned by the controller, not the implementer.
- Default CLI mode is validation only. An explicit future scientific command may be implemented and tested for failure/phase behavior without executing prospective cells. Do not run it successfully on this task.
- Raw trajectories and contract-check evidence must be preserved, with source/protocol/reference hashes, phase counters, exact primary map and seals. No weighted endpoint.
- On any mismatch use `INVALID_NO_SCIENTIFIC_RESULT`, stop, retain diagnostic receipts without scientifically interpreting partial data, and do not overwrite evidence.
- No subagents may be spawned by implementers or reviewers. No remote pushes, merges, PR creation or V1 full validation by implementers. The controller owns delivery and the full gate.

## Task 1: Implement the complete frozen software and focused tests

**Files to create:**

- `experiments/a2_v1/implementation/a2_v1/__init__.py` and `__main__.py`.
- `authorities.py`: pinned source/reference loading, exact unit strata, independent theorem/P0/P3 reference compilation.
- `engine.py`: priority-aware live-set learner, paired eight-episode training, frozen evaluation, trajectory records.
- `checks.py`: independently check all preregistration §8 invariants, including correct action observations, truth retention, update predicate, costs, isolation, policy witnesses, frontier geometry and bidirectional transplant boundary.
- `derived.py`: exact registered sensitivity/effect-modification and common-loss structures, tested on synthetic frontiers only.
- `runner.py`: reference compilation seals, strict phase controller, validation/science entry points, immutable output seals and invalid receipts.
- `tests/test_authorities.py`, `test_engine.py`, `test_checks.py`, `test_derived.py`, `test_runner.py` as needed for meaningful behavior tests.
- `README.md`: exact commands, frozen resource semantics, evidence formats and current validation-only delivery boundary.

**Interfaces:** These module names separate responsibilities, but internal signatures may be chosen coherently by the implementer and documented in its report. Export `load_authorities()`, `validate(output_dir)` and an explicit `run_prospective(output_dir)` or equivalent CLI functions. CLI must support `python3 -m a2_v1 validate --output DIR`, default to validate, and offer no way to substitute a stored receipt for a fresh gate. The engine's actual paired execution function must have a clear name and unit argument so an independent call profiler can audit every `(h,P,k)` entry.

### Step 1 — Read and map the complete frozen spec

- [ ] Read `experiments/A2_PREREG_V1.md` in full plus the machine contract and relevant V0 model/measurement/runner/checks. Do not import a V0 scientific-run command.
- [ ] Map every §8 invariant and every output requirement to a function and test in the implementer report. Record any engineering completion without altering scientific semantics.

### Step 2 — Establish RED tests before new production code

- [ ] Authority corruption must stop before training; historical reconstruction must hash to `3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117`. P3 compilation must implement the independent state bijection, not call the engine.
- [ ] Test nonlex selection with a synthetic live set `{8,11}` under P1: it selects original hypothesis 11, not 8. This catches accidentally retaining numeric `min(live)`.
- [ ] Test invalid feedback preserves live state while doing the same charged work; informative updates preserve truth using manually derived observations and predictions.
- [ ] Reference-only paired smoke cells cover identity controls, nonidentity translations, and P0/P3 cells. No `(h>=8,P not in {0,3},k)` may be trained by tests.
- [ ] Mutation tests corrupt an observation, frontier witness, update result, charge, or constructor boundary and require a real invariant failure. Expectations must not call the production function under test.
- [ ] Test theorem/P0/P3 gate mismatches separately, including the resulting invalid receipt, stopped later phases, and zero prospective calls. Fakes are permitted at the expensive paired-execution boundary for controller order tests; they must never replace the phase logic being tested.
- [ ] Test that a preexisting PASS cannot authorize targets, that validation-only stops after reference phases, and that duplicate output directories/changed seals are rejected.
- [ ] Test effect modification and both any/common loss definitions with explicit synthetic frontier maps that separate equal cardinality from equal sets and any loss from common loss.

Run the real test commands and retain the initial failing assertions/errors caused by absent functionality in the report. Avoid tests that merely grep source text or mirror constants.

### Step 3 — Implement to make those behaviors pass

- [ ] Implement the loader/compiler with pinned hashes and immutable normalized rank/reference structures. Reconstruct the historical full primary using its original schema and canonical JSON, then derive P3 expectations by state-set transport and original hypothesis mapping.
- [ ] Implement active-rank selection while preserving original decoder IDs. It is permissible to reuse the unchanged V0 model/evaluation module through a verified local import, or to implement equivalent code with independent checks. Do not modify V0 files.
- [ ] Implement all §8 checks with explicit falsifiable comparisons. Independent checking must not merely rerun the same update or evaluation function.
- [ ] Implement ordered reference phases, before/after counters, evidence and failure seals, the validation-only terminal state, and the fresh-gate science path without running targets.
- [ ] Implement exact primary and derived records, canonical serialization, immutable outputs, and compressed raw evidence as appropriate. Evidence must be inspectable and hash-bound, not just aggregate PASS counters.
- [ ] The source digest must cover every scientific/execution input and Python source/test file while excluding generated runtime evidence. Final validation must run unchanged code corresponding to the recorded digest.

### Step 4 — Verify software and commit locally

- [ ] Run focused tests through `python3 -m unittest discover -s tests -v` in the new implementation directory; ensure every actual paired call is a reference cell.
- [ ] Self-review against every spec section, not only the tests. Fix code defects without weakening expected results.
- [ ] Commit only new implementation files and tests locally. Do not change the preregistration or prior status files, run the full 2,176 gate, or push.
- [ ] Write a report containing commit IDs, exact test commands/results, RED evidence, module interfaces, pair execution function location, source-digest scope, raw evidence format and any unresolved concerns.

## Controller completion (after Task 1 review)

1. Review the implementation against the frozen spec with an independent reviewer; route concrete defects back to the implementer.
2. Check base-file preservation and the full software suite once on the reviewed source.
3. Execute `python3 -m a2_v1 validate --output <new-directory>` under an independent call profiler. Required terminal counts: 1,536/320/320 successful reference pairs, 2,176 unique units, zero prospective unit calls.
4. Verify all receipt/file seals, source digest, reference signatures and raw evidence. No scientific interpretation or prospective continuation.
5. Archive implementation-level status and evidence on the isolated branch, preserving every frozen base file. Publish a reviewable branch/PR as appropriate; do not merge the shared main branch in this step.

## Preflight consistency review

| Surface | Producer → consumer | Check |
|---|---|---|
| Authorities → engine | Original hypothesis IDs plus frozen rank arrays | Conjugation changes priority only, never decoder/world labels |
| Authorities → runner | Theorem/P0/P3 expected endpoints | Compiler cannot consume learner outputs |
| Engine → checks | Complete paired records and active-rank state | All §8 invariants have independent comparisons |
| Runner → derived | Sealed complete primary map | Derived work follows primary seal; no utility endpoint |
| Software tests → controller gate | Reference/synthetic tests then full validation | No target execution before or during this delivery |
| Task 1 internal | Tests, files and freeze constraints | Implementation changes only new files; full validation belongs to controller |

No scientific design amendment is part of this plan.
