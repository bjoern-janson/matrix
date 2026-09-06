# A2-V1 preregistration custody

Repository parent before the preregistration archival commit:

`1a73502759a308f99d09de88aca67f0dfdcfd412`

The commit introducing this record binds the frozen preregistration, its machine-readable companion, the corrected mathematical report, and all archived inputs. It does not rewrite any V0 artifact, MATRIX0 kernel, or `formalization/EXEC_V1.md`.

## Original and corrected audit packages

| Artifact | SHA-256 |
|---|---|
| `audit/packages/a2-v1-priority-audit-original.zip` | `b7040590e942bebb36b30ae1ba180009bbf91f40c888bd6eebcd172652779f39` |
| `audit/packages/a2-v1-priority-audit-corrected.zip` | `b89ef07fa373d60072f64d622cf4ecfe84f682b4a4aacff2dc29a858610f443d` |
| `audit/PRIORITY_FAMILY_AUDIT.json` | `a11c989c0a72d4d0363077ce353fd5642f708933adedee475ca2c1678497bb2c` |
| `audit/THEOREM_CONTROL_PREDICTIONS.json` | `aa274d3038c9a6633a35a3ef66395773bb27413e8768f0956b878667941deaf5` |

Only the report's fifth displayed translation order and its checksum differ between packages. The original audit's 16 mathematical check groups and machine outputs are unchanged. `audit/SHA256SUMS.txt` binds the expanded corrected package members. `ARCHIVE_SHA256SUMS.txt` binds every file added by this preregistration archive except the checksum file itself.

## Bound V0 authorities

- Source state: `bjoern-janson/matrix@1a73502759a308f99d09de88aca67f0dfdcfd412`.
- Model path: `experiments/a2_v0/implementation/a2_v0/model.py`.
- Model Git blob: `f3aab0759b994aa06e961c62e7dfc27e8573fcf3`.
- Model SHA-256: `6ab7a3a27d7be6aed5f7743f6b302e1264c958eef8f1c45b367562613f850eef`.
- V0 source digest: `dd454df0cf646b44a11f91bc965ab5a40de1e62c860dacdf0e988d32205dc02d`.
- Historical compact primary path: `experiments/a2_v0/results/primary_compact.json`.
- Historical compact Git blob: `e8d98cc19a80a1308410559df8386eddcea96ab7`.
- Reconstructed full primary SHA-256: `3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117`.
- Original full scientific-run ZIP SHA-256: `cb9e444d1264b68013ead4c895fc5717b70bd310d6523cd6f091460c748021ff`.

The compact historical record and pinned reconstruction recipe suffice to construct the P0/P3 endpoint references without an external raw archive. No V1 learner may generate its own expected reference values.

## Standing

The exact candidate priority arrays are adopted by `A2-PREREG-V1`. Historical audit standing remains unchanged inside the archived JSON and report. Prospective reference compilation, V1 software validation, and V1 scientific execution have not occurred in this commit. The 1,536 theorem rows are predictions, not measurements. There is no V1 result receipt.
