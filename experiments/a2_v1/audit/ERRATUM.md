# Audit report transcription correction

Date: 2026-09-06. Scope: documentation only.

The original report's fifth translation-block order was transcribed as:

```text
0 4 1 5 2 3 6 7
```

The correct order, already present in the independently enumerated and sealed `PRIORITY_FAMILY_AUDIT.json`, is:

```text
0 4 1 5 2 6 3 7
```

The corrected report changes exactly that sequence. In the corrected ZIP, only `A2_V1_PRIORITY_MATHEMATICAL_AUDIT.md` and its entry in `SHA256SUMS.txt` change. The mathematical audit script, both canonical JSON files, and the original audit receipt are byte-identical to the original package. All six displayed translation blocks were checked against the canonical JSON.

The original package remains archived byte-for-byte. This correction changes no priority, proof, control signature, covariance relation, unit count, or scientific standing. It does not constitute a new audit execution or a V1 assay execution.

The original receipt describes the preceding mathematical audit run; it is not represented as a new receipt for this documentation correction. The corrected package checksums identify the corrected document. See `../CUSTODY.md` for both package identities.
