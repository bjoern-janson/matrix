# A2-V0 Implementation Plan

> For agentic workers: use superpowers:executing-plans inline. The user has
> approved the scientific design and prohibited repository writes this turn.
> Do not reopen the mathematical audit or execute unresolved units for testing.

**Goal:** Deliver a runnable standalone assay and an auditable validation record.

**Architecture:** Pure finite channel/decoder functions feed an information-limited
learner and constructor. A separate verifier executes policies and enumerates
frontiers. The runner validates the theorem controls before remaining invariants;
unresolved execution is an explicit separate command that repeats both gates.

**Tech stack:** Python 3.11+ standard library, unittest, exact Fraction arithmetic.

**Spec:** `PROTOCOL.md`, implementing the approved conversation and attachments.

## Global constraints

384 units; 64 controls; 320 unresolved. Eight training episodes. Evaluation budget
5; costs 1 per query, repair, and realization. Nine policies. 256 subsets per
arm. No stochastic components, network dependencies, repository mutations,
result-selected thresholds, or unresolved-unit training during validation.

## Task 1: finite execution and measurement

Files: `a2_v0/model.py`, `a2_v0/measurement.py`, `tests/test_core.py`.
Interfaces: `channel(h, x)`, `decode(h, y)`, `Learner.predict/update/freeze`,
`realize(ConstructorInput)`, `execute(policy, h, x)`, `measure(h, constructor)`.

- [x] Write failing tests with literal channel/decoder examples, invalid-feedback
  retention, positive and negative update behavior, nonshared clone state,
  exact realization costs, and exact known-control frontiers.
  Example: `measure(1, ConstructorInput(active=0)).frontier` must equal
  `(0, 1, 2, 4, 8, 16, 32, 64, 128)`.
- [x] Run `python3 -m unittest discover -s tests -p test_core.py -v` and observe
  missing-implementation failures, before implementing the behavior.
- [x] Implement the exact frozen semantics, including full 48-item processing,
  constructor-visible fields, policy-visible histories, and exhaustive verifier.
- [x] Repeat that command and require all tests to pass.

## Task 2: controls and execution gate

Files: `a2_v0/runner.py`, `a2_v0/__main__.py`, `tests/test_runner.py`.
Interfaces: `train_pair(unit)`, `validate(output_directory)`,
`run_unresolved(output_directory)`. The runner consumes measurement records.

- [x] Write failing tests that require all 64 literal theorem signatures,
  source-bound validation evidence, validation-only default behavior, and
  stopping before any unresolved training after an injected control mismatch.
- [x] Run `python3 -m unittest discover -s tests -p test_runner.py -v` and
  observe missing-implementation failures.
- [x] Implement the control-first gate and run the 64 controls. If any mismatch
  occurs, stop the gate and localize it; retain the failure record.
- [x] Validate remaining invariants: version-set truth retention, equal charges,
  cloning, exact available policies, no evaluation learning, independent analytic
  frontier cross-checks, downward closure, and learned-state transplant behavior.
- [x] Implement explicit unresolved execution, with fresh gates and ordered
  exclusive-create output sealing. Test output sealing with known-control data.
  Do not invoke the unresolved science command during this task.

## Task 3: verification and delivery

Files: `README.md`, `evidence/*`, `MANIFEST.json`, distribution ZIP.

- [x] Run the full meaningful test suite, including injected boundary failures.
- [x] Run `python3 -m a2_v0 validate --output evidence/validation` and inspect all
  64 signatures and every invariant result. Require unresolved execution count 0.
- [x] Review code against every scientific constant and gate in the spec.
- [x] Package source, tests, protocol, and validation evidence with SHA-256 hashes.
- [x] Save the artifacts and report only verified state. Do not commit or push.
