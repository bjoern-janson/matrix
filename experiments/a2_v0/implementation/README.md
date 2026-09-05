# A2-V0 implementation and validation

Standalone implementation of the user-frozen A2-PREREG-V0 assay. This package
contains source, tests, the operational contract, and validation evidence.
It is not a repository commit or an unresolved-unit scientific result.

## Run

Python 3.11 or later is required. There are no third-party dependencies.
Extract the ZIP and run commands from this directory.

```bash
python3 -m unittest discover -s tests -v
python3 -m a2_v0 validate --output validation-new
```

The default command is also validation:

```bash
python3 -m a2_v0 --output validation-new-2
```

Each output directory must be new. Validation runs the 64 theorem-derived
controls, then the remaining invariants. It never trains the 320 unresolved
units. Primitive truth-table checks cover all 48 channel transformations;
these are not paired learning trajectories or unresolved frontier results.

The separate scientific command is supplied for a subsequent execution step:

```bash
python3 -m a2_v0 run-unresolved --output results-new
```

That command repeats both validation gates itself before training any unresolved
unit. It does not accept a saved PASS receipt as a substitute. **It was not run
to produce this deliverable.** The tests exercise its failure paths with injected
gate faults; those paths stop before unresolved training.

## Frozen controls

| Units | Expected control frontier | Expected treatment frontier | Standing |
| --- | --- | --- | --- |
| Hypothesis 0, all 8 rotations | All 256 subsets | All 256 subsets | NULL |
| Hypotheses 1–7, all 8 rotations | Empty set and 8 singletons | All 256 subsets | EXPANSION |

These are 64 theorem-derived signatures: 8 null and 56 expansion. Their matched
execution validates the implementation against known predictions. It is not a
new empirical discovery that feedback can affect this constructed frontier.

## Evidence and custody

`evidence/validation/report.json` records the final validation status, source
digest, exact executed control-unit list, invariant checks, and file hashes.
`evidence/execution-audit-summary.json` records the independently verified call census and binds the original full profiler audit by SHA-256.
`evidence/tests.txt` is the final complete test output.

The original validation package contains full primary, utility, transplant, and trajectory serializations. The repository preserves the exact validation `report.json`, validation/test evidence, source, and sealed hashes for those original serialized files; bulky evidence is not silently promoted above the source-bound report.

Every subset is stored as an integer bitmask: bit `x` means state `x` is in the
subset. Thus 0 encodes the empty set, 129 encodes `{000,111}`, and 255 encodes the
full state set. Arrays of these masks preserve sets of uncertainty sets; they
are not frontier-size scores.

Output files use exclusive creation. A theorem mismatch yields
`CONTROL_MISMATCH`; any other required invariant failure yields
`INVALID_NO_SCIENTIFIC_RESULT`. No unresolved scientific interpretation is
admitted by either status. If an explicit future science run fails after writing
some files, its failure report marks all scientific interpretation NOT_ADMITTED.

`MANIFEST.json` hashes all packaged files except itself. The validation source
digest separately binds the protocol, provenance, implementation, and tests.
The provided tests and control checks do not constitute a machine-checked proof
of the general MATRIX formalism.

## Implementation map

- `a2_v0/model.py`: finite world, information-limited learner, constructor, policy
  actions, and grounded evaluation execution costs.
- `a2_v0/measurement.py`: exhaustive policy/state/subset evaluation; separate
  analytic success/frontier oracle; exact deployment utility.
- `a2_v0/checks.py`: invariant checks applied after matching all 64 controls.
- `a2_v0/runner.py`: paired cloning, control gate, output sealing, explicit science
  path, and source identities.
- `PROTOCOL.md`: complete operational specification and accounting convention.
- `PROVENANCE.json`: source attachment hashes and accepted amendments.

Both arms process all 48 candidate hypotheses per training episode. The fixed
processing batch is charged 1 abstract unit, in addition to 4 primitive action
units; eight episodes cost 40 model units and perform 384 hypothesis checks per
arm. This numeric batch convention fills the draft's unspecified processing
unit and is explicit in the protocol. It is not a claim of equal wall-clock cost.

The weighted utility uses `2**x / 255`, so it encodes the default policy's success
set and remains structurally coupled to this assay's frontier. Transplants check
the declared constructor boundary. Neither endpoint claims broader independence,
general corrigibility, unfamiliar-state generalization, or policy invention.
