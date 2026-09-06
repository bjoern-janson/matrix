# MATRIX Documentation and Custody Consolidation Design

**Date:** 2026-09-06  
**Scope:** documentation/custody only; no scientific rerun, reinterpretation, or kernel revision.

## Goal

Make current `main` self-sufficient enough that future readers do not need chat history, scratch directories, expiring GitHub Actions artifacts, or remembered local filenames to recover the scientifically material A2-V1 state.

## Protected boundaries

The consolidation MUST NOT change:

- the MATRIX conceptual kernel;
- `formalization/EXEC_V1.md`;
- A2-V0 preregistration, result, or scientific interpretation;
- A2-V1 preregistration or its registered endpoints/decision rules;
- the admitted A2-V1 numerical result or claim ceiling;
- any execution record by regeneration or substitution.

Historical-stage documents may keep statements that were true at their commit. Current indexes must clearly label those records as historical rather than letting old `NOT_RUN` text masquerade as current standing.

## Design

### 1. Restore validation/review bytes exactly

Use the verified local archive `matrix-a2-v1-implementation-36f75e8.zip`, SHA-256 `a6db8ff636cbb4d1964833ead83d06b6970ad3db90d56e8a5ee46a5f6a7ac9ad`, as the byte authority for implementation review and validation evidence omitted from the remote reconstruction.

Restore the already hash-bound files under `experiments/a2_v1/implementation/evidence/` without modifying their contents. Verify each file against `CUSTODY.json` before repository insertion.

### 2. Make the admitted execution recoverable from the repository

The exact Actions artifact `a2-v1-prospective-34045071131.zip` has SHA-256 `17fbf854084a023c8d15a55e185bbe8e31d68d2087ebe05da7fa2c2fae68f11e`; its inner `a2-v1-prospective-output.tar.gz` has SHA-256 `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7`.

Archive the exact inner tarball in the repository. Also expose the two most scientifically useful exact outputs directly:

- `result/primary.json.gz`: deterministic `gzip -n -9` of the exact 9,216-row primary map; decompression must hash to `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076`;
- `result/derived.json`: exact registered membership/witness output, SHA-256 `7b298eef81996ab804c09c5a4d8756d7fbd8842843bcef7a30b9de160f64e10b`.

The tarball is the durable complete-output recovery object; the compact exposed files are for direct scientific inspection. No regenerated scientific endpoint is substituted.

### 3. Archive execution machinery as inert provenance

Copy the exact workflow used for the successful run into `experiments/a2_v1/execution/GITHUB_ACTIONS_WORKFLOW.yml` as an inert archive, not a live workflow on `main`.

Add `experiments/a2_v1/EXECUTION_CUSTODY.md` recording the canonical source commit, workflow/run/job/artifact identities, exact archive hashes, result hashes, and recovery instructions.

### 4. Repair stale navigation without rewriting history

Turn `experiments/a2_v1/README.md` into the current lifecycle index:

`audit -> preregistration -> implementation -> validation -> execution -> result -> current standing`.

It must explain that `CUSTODY.md`, `implementation/STATUS.json`, and `implementation/evidence/REMOTE_CUSTODY.md` are historical-stage records whose `NOT_RUN` language remains intentionally preserved.

Add `experiments/a2_v1/CURRENT_STATE.md` with the post-V1 earned/not-earned boundary. It may state that no next assay is currently frozen; it must not invent the next scientific question.

Add a concise current-program-state block near the top of root `README.md` while leaving the conceptual kernel text unchanged.

Append a custody-only note to `A2_V1_RESULT.md` pointing to the new durable repository archive; do not alter its scientific result sections.

### 5. Verification

Before merge:

- verify all restored validation/review files against `CUSTODY.json`;
- verify the exact execution tarball hash;
- verify `derived.json` hash;
- decompress `primary.json.gz` and verify both the compressed hash and the canonical primary hash;
- verify the archived workflow matches the successful execution branch blob;
- rerun the full 30-test A2-V1 software suite from the exact validated source;
- inspect the diff to confirm no kernel, formalization, preregistration, or implementation source files changed;
- verify current indexes no longer make false present-tense claims about V1 being unexecuted.

## Terminal state

The consolidation earns no new scientific claim. Its terminal state is simply:

```text
scientific state unchanged
+ exact missing custody restored
+ admitted execution recoverable from main
+ current lifecycle/status discoverable from main
```
