# A2-V0 custody record

## Repository parent before archival write

```text
b006a581161be65ea34df39ba9558facddac386b
```

## Validated scientific source identity

```text
dd454df0cf646b44a11f91bc965ab5a40de1e62c860dacdf0e988d32205dc02d
```

This digest binds the validated protocol/provenance/implementation/test source used for the scientific execution.

## Original validated implementation package

Original external package SHA-256:

```text
76b939f8a1724f14e057096cb2bfffa11e8454d59e4addd9a7bf05475837be6e
```

## Complete scientific-run archive

Original complete run-archive SHA-256:

```text
cb9e444d1264b68013ead4c895fc5717b70bd310d6523cd6f091460c748021ff
```

The complete run archive contained `primary.json`, `report.json`, `trajectories.json`, `transplants.json`, `utilities.json`, and the validation directory rerun by the science command before unresolved execution.

## Sealed science files

```text
primary.json
3ee83c7c50b9085cd990c09f57cb8ab784abe854e020c48a3137706fcf90e117

trajectories.json
aad6a6782c55f74537d274f78e53668daafddc6834a929ca4efde8018c0795b7

transplants.json
5529b9e29e42221db4f20e35685d2569c21af237e4959341106f45f1fb1e711c

utilities.json
5a054c1348080d78d48b7e529bb06dd1a25f5016d16bd17f998ace3189825ea0

report.json
25792670a091adf14f980f47d4156c6855d7a4e3d65c33eb9802f4805c2dac4e
```

The run receipt records validation binding:

```text
17f3bab6faf0957fa3c5f7b5b6fa11fd9667db1d10406dd6a1cd31ee7bce4b5f
```

## Repository preservation rule

The repository preserves the scientifically material state directly rather than relying on a chat attachment:

- validated source, tests, protocol, provenance, and validation evidence under `implementation/`;
- exact sealed `results/report.json`;
- `results/primary_compact.json`, an exact sufficient representation of the full 320-unit frontier endpoint under the frozen A2-V0 architecture, including each arm's active hypothesis and diagnostic success mask, the exact rational deployment contrast, and changed-unit transplant standing;
- sealed SHA-256 identities for the original full `primary.json`, `utilities.json`, `transplants.json`, trajectories, and both original archive packages.

For the frozen nine-policy architecture, the compact endpoint reconstructs every frontier exactly from each arm's diagnostic success mask via `Phi(A) = {S: |S| <= 1} union 2^A`. Therefore the repo does not replace the scientific endpoint with an aggregate count. The full raw serializations remain immutable external custody objects identified by their hashes; all facts used for the program's standing are directly source-controlled.

## Pre-execution call audit

The independent profiler audit of validation recorded 64 paired control calls (128 arm calls), hypothesis indices `0..7`, and zero unresolved calls. The repository keeps `implementation/evidence/execution-audit-summary.json` and binds the original full audit by SHA-256:

```text
11c0a8308199da7e64cea8d8e5318a7354aaf83f84dfd2458cde8852fe2a0934
```
