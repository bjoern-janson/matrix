# Task 1 independent review

Reviewed frozen `experiments/A2_PREREG_V1.md`, its machine contract, task brief/report, supplied whole-branch diff (374c58a to 074be27bda227a22d3509cdaeb7a432f41506aa9), all production modules and focused tests, and the frozen V0 model. No assay execution, existing suite rerun, prospective execution, source edit, index operation, or ref operation was performed. This requested review report is the only file written.

**Spec-compliance verdict: FAIL — changes required before full validation.**

**Code-quality verdict: FAIL — the checker and custody controller do not support their claimed assurance.**

These are implementation defects under the existing frozen protocol, not requests to amend the science. Passing endpoint smoke tests or the complete reference census would not discharge the omitted invariants.

## Critical findings

### C1. PASS does not establish a valid continuous training trajectory

`a2_v1/checks.py:12–23` accepts each episode's supplied `live_before` independently. It never requires the initial live set to be all 48 hypotheses, continuity with the preceding `live_after`, a full control live set, final-live equality with the last trace, or constructor-active equality with the final selected decoder. It never checks `prediction == decode(active_before, observations)` or validates `actual_correctness` against the prediction and state. Per-episode processing/primitive charges and check counts are ignored; only arm totals are compared. The rank order is trusted from the record rather than checked against the frozen priority identified by `p`; missing rank evidence silently defaults to P0. The science loop even overwrites recorded priority orders before checking (`runner.py:61`), concealing what was actually recorded.

Consequently, state can be reset or substituted between episodes, a different priority can be used, a prediction can be inconsistent with the selected decoder, and final constructor state can be detached from learning without a corresponding invariant rejection. The theorem failure count additionally trusts unchecked `actual_correctness`. This fails §8.2–7 and 11. Retain and independently check the complete state chain, frozen priority identity, selected-decoder prediction, actual correctness, per-step work, and final constructor linkage. Do not rewrite evidence to the expected value before checking it.

### C2. Evaluation evidence and transplantation are not executed/checked at the required policy boundary

`engine.py:_measure` synthesizes action arrays, outcomes, and fixed costs inline with access to the hidden world and latent state. Unlike the frozen V0 `realize`/`RealizedPolicy.action`/`execute` boundary, there is no realized policy object whose input is limited to observations, or action-by-action execution that charges actual declared operations. Although the inline formula looks mathematically equivalent for the current implementation, this does not establish the requested constructor/policy execution boundary.

More decisively, `checks.py:24–29` never reads evaluation `actions` or `observations`, never independently checks every execution's success, and does not require the witness list to equal the complete eligible policy set. Arbitrary undeclared actions or corrupted diagnostic observations can pass unchanged. Algebraic frontier agreement cannot validate those traces. The top-level primary arm frontiers are also never unconditionally linked to `measurement.frontier`.

The claimed bidirectional transplant (`checks.py:31–33`) calls only `_oracle_frontier` on each donor's own active ID. It never transplants into a recipient, realizes donor state through the production constructor, or executes the resulting policies in either direction. It repeats an endpoint formula instead of exercising the contract at issue.

This fails §8.8–10 and 13. Introduce or reuse the verified restricted policy construction/execution interface, independently verify its actions, observations, success and costs, require exact frontier/witness linkage, and execute both recipient transplant directions for changed-frontier pairs while retaining their evidence.

## Important findings

### I1. Required preparation seals do not exist before the first pair

`runner.py:39–44` loads and compiles references and computes a digest in memory, then immediately executes pairs. The first `_seal` is after all 2,176 reference pairs (`:55`). Neither the exact unit manifest nor compiled theorem/P0/P3 expectations is serialized or hash-sealed at any point. `a.identities` contains input hashes, not the compiled reference identity. Thus the README claim that references are compiled **and sealed** before execution is false. Sections 6.3, 7 and 12 and the contract's first output stage explicitly require these seals before any execution. Persist canonical preparation artifacts and an immutable manifest binding their hashes before entering the pair boundary.

### I2. Protocol identity and validation source integrity are insufficiently bound

`authorities.py:EXPECTED` omits the authoritative protocol even though `PATHS` lists it: modifying `A2_PREREG_V1.md` does not cause identity rejection. It merely changes the dynamically calculated implementation digest. `Authorities` is a frozen dataclass with mutable nested contract/theorem/historical/identities dictionaries, contrary to the required immutable normalized inputs.

`runner.py:58` returns validation PASS before the sole source recheck at `:63`. The science command also reaches its first prospective pair before this recheck. Changes during validation can therefore produce a validation PASS and allow target entry without detecting the changed source until after all targets. Freeze nested configuration/reference structures, pin the protocol identity, retain the source manifest, and reverify sources/authority/preparation seals before sealing validation and before target entry. Validate the final seals as well as exclusive file creation; current code has no changed-seal rejection path.

### I3. Failure paths lose evidence and omit failures during preparation

Authority loading, reference compilation and initial source hashing occur before the `try` (`runner.py:39–41`). Identity/reconstruction failures therefore leave an empty attempt directory with no invalid receipt. Once inside the loop, the failing pair is appended only after reference and invariant checks pass (`:44–46`); an exception loses that pair and all prior raw records because the exception handler writes only counters and stages. An exception inside paired execution is not counted at entry. Failures after the validation gate likewise discard prospective diagnostic records.

This contradicts the required invalid receipt and retained trajectories/contract evidence on mismatches (§7, §12 and task brief). Initialize failure bookkeeping before preparation, preserve preparation errors, capture pair entry/completion independently, retain failing/partial records and checks as immutable diagnostics, and bind those diagnostic artifacts in the invalid receipt. Existing files must remain protected against overwrite.

### I4. Complete primary rows are serialized in phase order, not lexicographic unit order

`runner.py:65` directly serializes `records`, which consists of all theorem controls, then all P0 cells, then all P3 cells, then all targets. For example `(47,0,7)` precedes `(8,3,0)`, and `(8,1,0)` comes after every reference cell. This deterministically violates §9's global lexicographic row encoding. Keep execution/evidence in required phase order, but sort the complete primary rows by unit before canonical serialization and sealing.

### I5. Final coverage and baseline checks are weaker than the frozen output contract

`checks.py:10` accepts any recognized stratum label rather than matching the unit. The runner never requires the returned unit to equal the requested unit. Reference coverage checks only length/uniqueness, and final coverage checks only unique-count 9,216 (`runner.py:49–50,62`), not exact equality with the declared mode's manifest, exact per-stratum membership, or exact prospective count. The control-baseline census occurs only over reference records (`:51–53`), never the complete target-inclusive map. These omissions allow incorrectly labeled/swapped/out-of-universe records or target-specific baseline deviations to evade the intended final checks. Explicitly check requested/returned identity, exact manifests and stratum counts, and the full-map per-world baseline before admitting primary output (§8.11,14; §9; §12).

### I6. Focused tests do not support several claimed verification results

The submitted `tests/test_v1.py` does exercise useful smoke cases and five simple mutations. However, runner tests replace both reference matching and invariant checks, so they do not demonstrate production mismatch detection. `test_science_repeats_fresh_gate_and_stored_pass_cannot_bypass` only attempts an already-existing directory; it never verifies fresh-gate science phase order. The derived fixture does not assert `E_PK`, its lexicographically first witness, `L_any_K`, `L_common_K`, or `C_K`. No changed-seal, source-change-during-validation, preparation invalid-receipt, failed-record retention, or disconnected-trajectory test is present. The report's exact smoke list also omits `(1,1,0)`, executed by the mutation test (still a permitted theorem reference).

Add narrow behavioral mutation/controller tests for the concrete gaps above, using synthetic pair-boundary fakes where necessary and no real targets. Do not treat the reported 13 green tests as evidence that all §8 checks or output/failure contracts are implemented.

## What is supported by static inspection

- The supplied whole-branch diff adds files only; no frozen base file is modified in that diff.
- The learner's present update comprehension actually decodes all 48 candidates, intersects with live state, and discards the proposal for invalid feedback. Current active selection uses priority rank rather than numeric minimum.
- Pair construction creates fresh base/control/treatment learners and distinct live sets. The implementation has no apparent cross-cell cache. The checker nevertheless does not independently establish the full clone/continuity contract.
- Priority arrays are tuples loaded from a pinned audit. Model/audit/contract/historical/theorem input hashes are checked, and the loader mathematically compares independently generated state maps to the audit and checks the declared unit partition.
- Historical reconstruction and P3 state transport do not call the V1 learner/evaluator. The P3 compiler explicitly uses the XOR-4 state bijection and conjugated original-hypothesis mapping. The reconstructed historical hash is checked before pair entry.
- The normal runner control flow executes the three reference phases in their required order and validation mode returns before target iteration. There is no stored-PASS bypass API. Output directories and files use exclusive creation.
- The registered derived formulas appear correctly implemented with exact sets, noncontrol domain, lexicographic combination enumeration and retained empty common-loss families. They follow primary serialization and bind its hash. No weighted endpoint is introduced.
- Full validation remains unrun by this reviewer. Nothing in this report authorizes prospective execution.

## Section 8 coverage verdict

| Invariant | Review result |
|---|---|
| 1 | Partial: input hashes/partition checked; protocol pin and immutable nested authorities missing. |
| 2 | Partial: fresh clones in code; unchecked continuous state/priority provenance. |
| 3 | Partial: actual full scan present; per-episode action/work evidence not independently checked. |
| 4 | Partial: token relation checked; selected-decoder prediction and actual correctness not linked. |
| 5 | Incomplete: per-record truth/update checks, no full initial/control state or inter-step chain. |
| 6 | Incomplete: ranks trusted from record, not bound to frozen unit priority. |
| 7 | Partial: separate predicate comparison exists; uses engine decode and lacks chain/prediction checks. |
| 8 | Incomplete: dict key check without restricted realized-policy boundary. |
| 9 | Incomplete: traces/observations/success and complete witness eligibility not checked. |
| 10 | Partial: all states/subsets enumerated and independent frontier formula; execution equivalence unchecked. |
| 11 | Partial: snapshot flag and reference baselines only; full-map baseline absent. |
| 12 | Partial: directed differences checked against top-level frontiers, not always linked to measurement. |
| 13 | Missing actual bidirectional transplant execution. |
| 14 | Incomplete: preparation seals, identity/coverage verification and failure evidence missing. |

Recommendation: route these concrete defects back to the implementer, review corrections, then let the controller perform the authorized validation-only gate on unchanged reviewed code. No stylistic refactoring is requested.
