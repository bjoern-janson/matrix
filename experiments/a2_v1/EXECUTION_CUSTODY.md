# A2-V1 execution and result custody

**Standing:** COMPLETE / SCIENTIFIC INTERPRETATION ADMITTED.  
**Purpose:** current execution/result custody. The earlier [`CUSTODY.md`](CUSTODY.md) is intentionally retained as the preregistration-stage custody record and is not rewritten retroactively.

## Canonical scientific source

The admitted A2-V1 science command executed the validated repository state:

`2b79c73dd9ac46fd6f693fd35d63c44cbb396a40`

with validated source digest:

`ea204bad2519f6759f6e5ef1dadd405b7043fe8277e6b5ebbfa3cace09c1c31c`.

The science process reran the mandatory fresh 2,176-reference gate before any prospective target entry, then executed exactly 7,040 prospective pairs. The authoritative scientific interpretation is [`../A2_V1_RESULT.md`](../A2_V1_RESULT.md); the final machine receipt is [`result/receipt.json`](result/receipt.json).

## Successful GitHub Actions execution

| Object | Identity |
|---|---|
| Execution branch | `science/a2-v1-prospective-20260906` |
| Workflow commit | `1f8052ad592b7ac1fe502574774b9c6e20100ec4` |
| Workflow run | `34045071131` |
| Workflow job | `101518572282` |
| GitHub Actions artifact | `9992901892` |
| Artifact name | `a2-v1-prospective-34045071131` |
| GitHub artifact ZIP SHA-256 | `17fbf854084a023c8d15a55e185bbe8e31d68d2087ebe05da7fa2c2fae68f11e` |
| Original artifact expiry | `2026-12-05T16:19:33Z` |
| Inner sealed output tarball SHA-256 | `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7` |

The exact workflow used by the successful run is archived inertly at [`execution/GITHUB_ACTIONS_WORKFLOW.yml`](execution/GITHUB_ACTIONS_WORKFLOW.yml). It is not installed as a live workflow on `main`.

## Repository-resident scientific output

The original Actions artifact may expire. MATRIX therefore retains the exact complete-output tarball directly in the repository:

- [`execution/artifacts/a2-v1-prospective-output.tar.gz`](execution/artifacts/a2-v1-prospective-output.tar.gz) — SHA-256 `d1f7605ac4246cd872984a1a3efaead468a9cea242d5fd88642969af1344bfa7`;
- [`execution/artifacts/a2-v1-prospective-output.tar.gz.sha256`](execution/artifacts/a2-v1-prospective-output.tar.gz.sha256) — original checksum sidecar;
- [`execution/logs/`](execution/logs/) — exact test, prospective-execution, environment, memory, disk and swap logs from that archive.

The complete-output tarball contains the scientific output directory, including raw evidence, fresh validation evidence, primary map, derived structures, manifests and final receipt. Its repository copy is the durability object; the original Actions artifact remains provenance rather than a required availability dependency.

For direct inspection, two registered scientific objects are additionally exposed without changing their identities:

- [`result/primary.json.gz`](result/primary.json.gz) — deterministic `gzip -n -9` compression, SHA-256 `a317bf081407694cefe2e84b97bfdbd845eef1077a7b92c6328785b565c6e8b3`; decompression yields canonical `primary.json` SHA-256 `f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076`;
- [`result/derived.json`](result/derived.json) — exact preregistered membership/witness structures, SHA-256 `7b298eef81996ab804c09c5a4d8756d7fbd8842843bcef7a30b9de160f64e10b`.

Other receipt-bound scientific identities remain:

| Artifact | SHA-256 |
|---|---|
| Final receipt | `4b41b91ea06af7d5f9b77ee33b523bdb178f7c321c17af8aa33dcdd546aa44f2` |
| Raw evidence JSON | `6e3188b33a2640133cbdd4b9d91b48513cbd2dfc80c96c21efb561932961c1d1` |
| Fresh science-gate validation receipt | `cfb9e62c8c69477d5ac4717cdb7e2dfa6013078d14a544e8e63262ce4b110be7` |
| Expected references | `31e187d876fa1aa2952fb78e6e6e93399b784bdfbc460b09d3d0b3f7a9a37194` |
| Preparation manifest | `0b047d5e8fac7299e6b04a4497ccfb394cd7137f52dd9d2ec5fd67944dc50873` |
| Source manifest | `ea204bad2519f6759f6e5ef1dadd405b7043fe8277e6b5ebbfa3cace09c1c31c` |
| Unit manifest | `33372d26cce332daa4b997b1106955ee000605025cf412503dcfa29a362537a3` |

## Validation/review custody restored

The validation-only stage remains separately preserved under [`implementation/evidence/`](implementation/evidence/). Its historical standing is **VALIDATION_ONLY / NO SCIENTIFIC RESULT**; that standing is not the current assay standing.

The directory now retains the previously hash-bound review and validation objects, including initial review, correction report, final rereview, independent call observer, software/call audits, independent reference archive and exact validation archive. The principal validation-only identities are:

- reviewed source commit `929d384972f9bffd12a8380c8204600d3a393941`;
- archive commit `36f75e8f616230d654b69143525be18782f3dab0`;
- validation archive SHA-256 `b397aba50af26e03946d18492c3580cc5acf5554fec347c3b22f72a907afc643`;
- independent reference ZIP SHA-256 `adb32579d31ce3d21146117df1d2e6582e1cabd6ae44ace722404af263e54d40`;
- validation call audit SHA-256 `4aeb621b0375225dded426ce2fab58242ef9e29dc6b1b362fe3d8932eefec351`.

[`implementation/evidence/CUSTODY.json`](implementation/evidence/CUSTODY.json) remains the machine-readable authority for the validation-only review/evidence hashes.

## Recovery

Recover the complete admitted execution into a new directory with:

```sh
mkdir recovered-a2-v1
tar -xzf experiments/a2_v1/execution/artifacts/a2-v1-prospective-output.tar.gz -C recovered-a2-v1
```

Recover the canonical primary JSON directly with:

```sh
gzip -dc experiments/a2_v1/result/primary.json.gz > primary.json
sha256sum primary.json
```

The expected primary hash is:

`f1b0f55c0860e9847f69ef4a741f477a66dd5cc7f8d9ed4af35484066e223076`.

## Claim boundary

This custody consolidation changes **availability and discoverability only**. It does not alter the preregistration, rerun the assay, regenerate a scientific endpoint, amend the final receipt, change any reported A2-V1 value, revise the MATRIX kernel, or earn `MATRIX_1`.
