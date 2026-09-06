# A2-V1 remote validation custody note

**Standing:** VALIDATION-ONLY / NO SCIENTIFIC RESULT.

This remote branch anchors the exact reviewed source tree from local commit `929d384972f9bffd12a8380c8204600d3a393941` and records the compact validation custody state archived locally by commit `36f75e8f616230d654b69143525be18782f3dab0`.

Validated source digest:

`ea204bad2519f6759f6e5ef1dadd405b7043fe8277e6b5ebbfa3cace09c1c31c`

Validation-only standing:

- software tests: 30/30 PASS;
- reference pairs: 2,176/2,176 matched;
- invariant assertions: 949,632 PASS;
- prospective pairs executed: 0;
- prospective pairs remaining: 7,040;
- scientific interpretation: NOT RUN / NOT ADMITTED.

The adjacent `STATUS.json`, `CUSTODY.json`, and `validation_receipt.json` are byte-identical to their files in local archive commit `36f75e8...`. `CUSTODY.json` binds the remaining review and raw-validation artifacts by SHA-256.

Full locally verified transport artifacts:

- implementation + evidence ZIP SHA-256: `a6db8ff636cbb4d1964833ead83d06b6970ad3db90d56e8a5ee46a5f6a7ac9ad`;
- complete-history Git bundle SHA-256: `ec9a65bfda1250218488ea2d6508eb31c7c002a7080a07050d072b6bde3dc1ad`;
- raw `validation_run.zip` SHA-256: `b397aba50af26e03946d18492c3580cc5acf5554fec347c3b22f72a907afc643`;
- independent reference ZIP SHA-256: `adb32579d31ce3d21146117df1d2e6582e1cabd6ae44ace722404af263e54d40`.

The full raw binary validation archive is **not duplicated in this remote reconstruction** because the available GitHub connector cannot ingest local binary file bytes directly. No replacement, regenerated archive, or altered binary is substituted for it. Its exact identity, contents manifest, and raw constituent hashes remain bound by `CUSTODY.json` and the verified local `36f75e8` bundle/ZIP.

This remote anchoring does not amend `A2-PREREG-V1`, merge to `main`, authorize prospective execution, or admit a scientific result.
