# A2-V0 archive index

This directory preserves the implementation, custody, sealed outputs, and post-execution structural analysis for MATRIX₀ Attack 2 / A2-V0.

Primary records:

- `../A2_PREREG_V0.md` — frozen scientific and causal contract, including theorem-derived controls and claim ceiling.
- `../A2_V0_RESULT.md` — comprehensive scientific execution record and interpretation ceiling.
- `STATUS.json` — machine-readable execution standing.
- `CUSTODY.md` — hashes and artifact identities.
- `results/primary_compact.json` — exact sufficient unit-level representation of the 320-unit frontier endpoint under the frozen nine-policy architecture; it reconstructs every `Phi`, `Delta+`, and `Delta-` from success masks and also preserves the per-unit weighted deployment contrast and transplant-check standing used in the scientific record.
- `results/report.json` — exact sealed scientific-run receipt and source/validation binding.
- `implementation/` — inspectable validated source, tests, protocol, provenance, and validation evidence.
- `analysis/POST_EXECUTION_STRUCTURE_V0.md` — comprehensive post-execution structural decomposition of the frozen 320-unit result; explicitly derived/non-preregistered and claim-ceiling preserving.
- `analysis/STRUCTURE_CENSUS.json` — machine-readable aggregate fixed-set, trajectory, order-sensitivity, scalarization, and claim-ceiling census for the post-execution analysis.
- `analysis/UNIT_STRUCTURE.json.gz` — gzip-compressed exact per-unit relative-transform, fixed-set, frontier, and trajectory-derived structural record.
- `analysis/TRAINING_DYNAMICS.json.gz` — gzip-compressed per-unit treatment dynamics derived from the sealed raw trajectory object.

The repo stores the scientifically material state directly: frozen contracts, validated source, exact compact frontier endpoint, per-unit secondary endpoint/contract-check information, run receipt, validation evidence, post-execution structural analysis, compact derived structural data, and hashes required to identify the original full serialized outputs. The original bulky `primary.json`, `utilities.json`, `transplants.json`, and trajectory serialization remain byte-identified by sealed SHA-256 values in `CUSTODY.md`; the compact record is an exact sufficient representation for the endpoint and secondary facts used here, not an aggregate substitute.

No file in this directory changes the MATRIX₀ conceptual kernel or rewrites `formalization/EXEC_V1.md`.
