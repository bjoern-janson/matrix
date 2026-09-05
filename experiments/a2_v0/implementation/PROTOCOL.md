# A2-PREREG-V0 implementation contract

This standalone package implements the design frozen in the conversation on
2026-09-05. It does not change the MATRIX repository or its conceptual kernel.
Reference repository: bjoern-janson/matrix at
`b006a581161be65ea34df39ba9558facddac386b`.

## Scientific constants

- States are integers 0 through 7 representing `000` through `111`, most
  significant bit first. A query index is a tuple coordinate, not a bit shift.
- Hypotheses are `(sigma, b)` in lexicographic product order: the six
  permutations of `(0,1,2)`, each followed by masks `000` through `111`.
- `q_j` returns `x[sigma[j]] XOR b[j]`; repair `r_z` succeeds iff `x == z`.
- There are 384 units `(hypothesis_index, rotation)`, each with two cloned arms.
- Train for eight episodes on `(rotation + t) mod 8`. Each episode always
  queries 0, 1, 2, predicts with the minimum surviving hypothesis, and repairs.
- Treatment receives `(valid=True, actual_correctness)`; control receives
  `(valid=False, False)`. Both run the same full 48-hypothesis consistency scan.
- On valid feedback retain exactly the previously surviving hypotheses for
  which `(candidate_prediction == attempted_repair) == actual_correctness`.
- Freeze learning after training. Constructor input is exactly the task tag
  `SWITCHBOARD_3` and the active hypothesis index. No full version set, true
  hypothesis, latent state, or tested uncertainty set enters the constructor.
- Exactly nine policies are available: eight immediate repairs and one
  diagnostic policy using the active hypothesis. No other decoder is available.
- Query and repair cost 1 each. Every evaluation policy realization costs 1.
  Evaluation budget is 5: immediate repair total 2; diagnostic total 5.
- The primary endpoint enumerates all nine realized policies, all eight states,
  and all 256 uncertainty sets. It retains the full frontier and difference sets.
- Deployment utility is the exact rational sum of `2**x / 255` over states
  correctly repaired by the default diagnostic policy. It is structurally
  coupled to this frontier and is not an independent viability measurement.
- Transplanting the active hypothesis is a contract check, not discovered
  mediation. There is no residual existence null or post-hoc decision threshold.

## Training accounting convention

The design fixed equal processing charges but did not assign a numeric unit to
one processing batch. This implementation declares one charge per complete
48-hypothesis feedback batch. Each episode therefore costs 4 primitive action
units plus 1 processing-batch unit, or 40 units over training. It additionally
records all 384 hypothesis checks per arm. This is an explicit abstract resource
model, not a wall-clock or processor-instruction equivalence claim. Selection
and feedback work are included in the fixed batch charge. Neither charge nor
loop length depends on outcome or version-set size.

## Frozen gates and scope

Hypothesis indices 0 through 7, all eight rotations, are the 64 theorem-derived
controls. Index 0 has full frontiers in both arms. Indices 1 through 7 have the
empty set and eight singleton sets in control, and the full powerset in
treatment. Their learned active hypothesis equals the true index after training.
These are analytical predictions, not discoveries from execution.

Order: implement -> reproduce all 64 control signatures -> validate remaining
invariants -> only then permit the 320 unresolved units. A control mismatch
raises `CONTROL_MISMATCH`; any other required invariant failure raises
`INVALID_NO_SCIENTIFIC_RESULT`. Neither admits unresolved scientific results.

`validate` executes controls and invariant checks only. `run-unresolved` is a
separate explicit command which repeats both gates in its own process before
executing exactly indices 8 through 47, all rotations. A saved PASS JSON is
never accepted as authorization or substituted for fresh gates.

Unresolved outputs are sealed in order: full frontier records, then deployment
utility, then transplant checks. Completed output files are never overwritten.
Subset integers in JSON are bitmask encodings of sets, not scalarized endpoints:
bit `x` is present iff state `x` belongs to the set.

## Current deliverable boundary

This task creates the implementation and validation evidence only. It does not
execute the 320 unresolved units, create a commit, or write to GitHub.
