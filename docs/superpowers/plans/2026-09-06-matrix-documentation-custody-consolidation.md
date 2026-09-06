# MATRIX Documentation and Custody Consolidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore missing A2-V1 custody bytes, make the admitted execution durably recoverable from the repository, and replace stale current navigation without changing any scientific claim.

**Architecture:** Preserve frozen scientific artifacts and add only exact custody objects plus current-stage indexes around them. Use the verified `36f75e8` implementation archive for omitted validation/review bytes and the exact successful GitHub Actions artifact for scientific-output custody. Keep large scientific evidence inside the exact sealed tarball while exposing the primary and registered derived structures directly.

**Tech Stack:** Git/GitHub, Python 3.12 standard library, SHA-256, gzip/tar/zip, Markdown/JSON/YAML.

**Spec:** `docs/superpowers/specs/2026-09-06-matrix-documentation-custody-consolidation-design.md`

## Global Constraints

- Do not rerun A2-V1 science.
- Do not alter MATRIX kernel semantics, `formalization/EXEC_V1.md`, either preregistration, A2-V0 science, or A2-V1 numerical interpretation/claim ceiling.
- Restore historical artifacts byte-for-byte from their recorded authorities; do not regenerate substitutes.
- Keep historical `NOT_RUN` records intact and label them as historical from current indexes.
- Exact scientific output must remain recoverable after the original Actions artifact expires.
- Every inserted binary/text artifact must be verified against an existing or newly recorded SHA-256 before merge.

---

### Task 1: Restore implementation review and validation evidence

**Files:**
- Create: `experiments/a2_v1/implementation/evidence/INITIAL_REVIEW.md`
- Create: `experiments/a2_v1/implementation/evidence/FINAL_REVIEW.md`
- Create: `experiments/a2_v1/implementation/evidence/IMPLEMENTATION_REPORT.md`
- Create: `experiments/a2_v1/implementation/evidence/controller_audit.py`
- Create: `experiments/a2_v1/implementation/evidence/software_test_audit.json`
- Create: `experiments/a2_v1/implementation/evidence/validation_call_audit.json`
- Create: `experiments/a2_v1/implementation/evidence/independent_references.zip`
- Create: `experiments/a2_v1/implementation/evidence/validation_run.zip`

**Interfaces:**
- Consumes: `matrix-a2-v1-implementation-36f75e8.zip` and existing `CUSTODY.json`.
- Produces: complete validation/review evidence set already named and hash-bound by custody.

- [ ] Verify the transport ZIP SHA-256 is `a6db8ff636cbb4d1964833ead83d06b6970ad3db90d56e8a5ee46a5f6a7ac9ad`.
- [ ] Extract the eight omitted artifacts without rewriting bytes.
- [ ] Compute each SHA-256 and compare to the values in `CUSTODY.json`; abort on any mismatch.
- [ ] Add only the verified artifacts to the consolidation branch.
- [ ] Re-fetch the branch paths and compare Git blob contents/hashes where feasible.

### Task 2: Archive the successful scientific execution

**Files:**
- Create: `experiments/a2_v1/execution/artifacts/a2-v1-prospective-output.tar.gz`
- Create: `experiments/a2_v1/execution/artifacts/a2-v1-prospective-output.tar.gz.sha256`
- Create: `experiments/a2_v1/result/primary.json.gz`
- Create: `experiments/a2_v1/result/derived.json`
- Create: `experiments/a2_v1/execution/logs/tests.log`
- Create: `experiments/a2_v1/execution/logs/prospective.log`
- Create: `experiments/a2_v1/execution/logs/environment.txt`
- Create: `experiments/a2_v1/execution/logs/memory-after.txt`
- Create: `experiments/a2_v1/execution/logs/disk-after.txt`
- Create: `experiments/a2_v1/execution/logs/swap-after.txt`

**Interfaces:**
- Consumes: GitHub Actions artifact `9992901892` from run `34045071131`.
- Produces: repository-resident exact complete-output archive plus directly inspectable primary/derived outputs.

- [ ] Download the exact artifact and verify ZIP digest `17fbf854084a023c8d15a55e185bbe8e31d68d2087ebe05da7fa2c2fae68f11e`.
- [ ] Verify inner tarball SHA-256 `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7`.
- [ ] Extract `primary.json` and verify canonical SHA-256 `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076`.
- [ ] Create deterministic `gzip -n -9` primary compression and verify SHA-256 `a317bf081407694cefe2e84b97bfdbd845eef1077a7b92c6328785b565c6e8b3`.
- [ ] Extract `derived.json` and verify SHA-256 `7b298eef81996ab804c09c5a4d8756d7fbd8842843bcef7a30b9de160f64e10b`.
- [ ] Archive the exact inner tarball, checksum file, exposed primary/derived objects, and execution logs.
- [ ] Decompress the repository primary artifact and verify its canonical hash again.

### Task 3: Archive execution provenance and current custody

**Files:**
- Create: `experiments/a2_v1/execution/GITHUB_ACTIONS_WORKFLOW.yml`
- Create: `experiments/a2_v1/EXECUTION_CUSTODY.md`

**Interfaces:**
- Consumes: successful workflow branch `science/a2-v1-prospective-20260906`, run/job/artifact IDs, Task 2 hashes.
- Produces: durable human-readable execution provenance and recovery instructions.

- [ ] Fetch the exact workflow from commit `1f8052ad592b7ac1fe502574774b9c6e20100ec4`.
- [ ] Store it inertly under `experiments/a2_v1/execution/`.
- [ ] Record canonical execution source `2b79c73dd9ac46fd6f693fd35d63c44cbb396a40`, run `34045071131`, job `101518572282`, artifact `9992901892`, and all exact hashes.
- [ ] Explicitly state that the original Actions artifact may expire but the exact complete-output tarball is now repository-resident.

### Task 4: Repair stale current navigation

**Files:**
- Modify: `README.md`
- Modify: `experiments/a2_v1/README.md`
- Create: `experiments/a2_v1/CURRENT_STATE.md`
- Modify: `experiments/A2_V1_RESULT.md` by appending a custody-only archival addendum.

**Interfaces:**
- Consumes: existing historical records plus Tasks 1-3.
- Produces: accurate present-tense navigation while preserving historical-stage documents.

- [ ] Add a concise current-program-state block to root README: MATRIX0 kernel frozen; Attack 1 closed/assumption-scoped; A2-V0 complete; A2-V1 complete/admitted; MATRIX1 not earned.
- [ ] Replace the A2-V1 archive README with a lifecycle index that clearly distinguishes historical prereg/validation records from current assay standing.
- [ ] Add `CURRENT_STATE.md` recording what V1 earned, what it did not earn, and that no next assay is currently frozen.
- [ ] Append a custody-only addendum to `A2_V1_RESULT.md` pointing to the repository-resident execution archive, primary and derived objects. Do not edit the reported scientific values.
- [ ] Search the current navigation files for false present-tense claims that V1 implementation/execution is absent; retain such text only inside explicitly historical-stage records.

### Task 5: Full verification and merge preparation

**Files:** no scientific source changes.

**Interfaces:**
- Consumes: all previous tasks.
- Produces: verified consolidation branch ready for merge.

- [ ] Run `PYTHONPATH=. python3 -m unittest discover -s tests -v` from `experiments/a2_v1/implementation`; require 30/30 PASS.
- [ ] Verify all restored review/validation hashes against `CUSTODY.json`.
- [ ] Verify execution tarball, primary decompression, and derived hashes.
- [ ] Compare the branch to `52023fe84c5c706c0b8b7c18d61936ec99070b65`; confirm no changes under `formalization/`, either preregistration, A2-V0 scientific records, or `experiments/a2_v1/implementation/a2_v1/`.
- [ ] Re-fetch the final branch files and verify current-status links and hashes.
- [ ] Open a consolidation PR, inspect its full changed-file set, then merge only if every verification passes.
