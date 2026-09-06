"""Finite group/order audit only. No learner, feedback trajectory, or assay run.

Python standard library only. Reproduce with:
    python3 audit_priority_family.py --output-dir reproduced
Optional --source-path checks the exact pinned A2-V0 model bytes, without import.
"""
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from itertools import permutations, product
from pathlib import Path

REPO_COMMIT = "1a73502759a308f99d09de88aca67f0dfdcfd412"
MODEL_PATH = "experiments/a2_v0/implementation/a2_v0/model.py"
MODEL_SHA256 = "6ab7a3a27d7be6aed5f7743f6b302e1264c958eef8f1c45b367562613f850eef"
MODEL_BLOB = "f3aab0759b994aa06e961c62e7dfc27e8573fcf3"
H = tuple(product(permutations(range(3)), product((0, 1), repeat=3)))
INDEX = {h: i for i, h in enumerate(H)}


def require(condition, description):
    if not condition:
        raise RuntimeError(description)


def compose(a, b):
    """a * b means T_a after T_b; sigma uses the source's row convention."""
    s, v = a
    t, w = b
    return (tuple(t[s[j]] for j in range(3)),
            tuple(w[s[j]] ^ v[j] for j in range(3)))


def inverse(a):
    s, b = a
    r = tuple(s.index(j) for j in range(3))
    return r, tuple(b[r[j]] for j in range(3))


def state_map(a):
    """Independent representation as a permutation of eight integer states."""
    s, b = a
    out = []
    for x in range(8):
        bits = tuple(int(c) for c in format(x, "03b"))
        observed = tuple(bits[s[j]] ^ b[j] for j in range(3))
        out.append(int("".join(map(str, observed)), 2))
    return tuple(out)


def map_compose(a, b):
    return tuple(a[b[x]] for x in range(8))


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def audit():
    checks = []

    def passed(name, count=None):
        row = {"name": name, "status": "PASS"}
        if count is not None:
            row["cases"] = count
        checks.append(row)

    maps = tuple(state_map(h) for h in H)
    require(len(H) == len(set(maps)) == 48, "48 distinct actions")
    require(H[0] == ((0, 1, 2), (0, 0, 0)), "index zero is identity")
    require(all(sorted(m) == list(range(8)) for m in maps), "actions bijective")
    passed("48_distinct_bijections_and_identity_index", 48)
    table = tuple(tuple(INDEX[compose(a, b)] for b in H) for a in H)
    for i, j in product(range(48), repeat=2):
        require(maps[table[i][j]] == map_compose(maps[i], maps[j]),
                "tuple multiplication versus state-map composition")
    passed("closure_and_independent_composition_agreement", 2304)
    for i, j, k in product(range(48), repeat=3):
        require(table[table[i][j]][k] == table[i][table[j][k]], "associativity")
    passed("associativity", 110592)
    inverses = tuple(INDEX[inverse(a)] for a in H)
    for i in range(48):
        require(table[0][i] == table[i][0] == i, "identity law")
        require(table[i][inverses[i]] == table[inverses[i]][i] == 0, "inverse law")
    passed("identity_and_two_sided_inverse_laws", 48)

    conjugations = tuple(tuple(table[table[g][h]][inverses[g]]
                               for h in range(48)) for g in range(48))
    for g, order in enumerate(conjugations):
        require(sorted(order) == list(range(48)) and order[0] == 0,
                "conjugation is identity-fixing permutation")
        for h in range(48):
            independent = map_compose(map_compose(maps[g], maps[h]), maps[inverses[g]])
            require(maps[order[h]] == independent, "conjugation representations agree")
        for h, j in product(range(48), repeat=2):
            require(order[table[h][j]] == table[order[h]][order[j]], "automorphism law")
    passed("48_identity_fixing_conjugations", 48)
    passed("independent_conjugation_agreement", 2304)
    passed("conjugation_automorphism_law", 110592)

    center = [g for g in range(48) if all(table[g][h] == table[h][g] for h in range(48))]
    stabilizer = [g for g, order in enumerate(conjugations) if order == tuple(range(48))]
    require(center == stabilizer == [0, 7], "center and ordered-list stabilizer")
    passed("center_equals_full_order_stabilizer", 48)
    grouped = defaultdict(list)
    for g, order in enumerate(conjugations):
        grouped[order].append(g)
    require(len(grouped) == 24 and all(len(gs) == 2 for gs in grouped.values()),
            "24 orders of multiplicity two")
    for order, gs in grouped.items():
        require(table[gs[0]][7] == gs[1], "duplicate pair differs by central complement")
    passed("deduplication_exactly_central_pairs", 48)

    orders = []
    for p_id, (order, gs) in enumerate(sorted(grouped.items(), key=lambda item: min(item[1]))):
        rank = tuple(order.index(h) for h in range(48))
        representative = min(gs)
        inverse_conjugation = conjugations[inverses[representative]]
        require(rank == inverse_conjugation, "rank equals inverse conjugation")
        require(set(order[:8]) == set(range(8)), "translations remain first block")
        require(order[0] == 0 and order[7] == 7, "central positions preserved")
        orders.append({"priority_id": p_id, "representative_index": representative,
                       "generator_indices": gs, "order": order, "rank_by_hypothesis": rank})
    require(orders[0]["order"] == tuple(range(48)), "original priority present")
    passed("identity_first_inverse_ranks_translation_block_and_lex_member", 24)

    classes = sorted(set(tuple(sorted({order[h] for order in conjugations})) for h in range(48)))
    class_of = {h: i for i, cls in enumerate(classes) for h in cls}
    for p in orders:
        require(all(class_of[p["order"][r]] == class_of[r] for r in range(48)),
                "conjugacy class fixed at every rank")
    first_blocks = sorted(set(p["order"][:8] for p in orders))
    fixed_positions = [r for r in range(48) if all(p["order"][r] == r for p in orders)]
    prefix_lengths = [n for n in range(1, 49)
                      if all(set(p["order"][:n]) == set(range(n)) for p in orders)]
    require(len(classes) == 10 and len(first_blocks) == 6 and fixed_positions == [0, 7],
            "restricted rank structure")
    require(prefix_lengths == [1, 7, 8, 48], "exact invariant prefix sets")
    passed("conjugacy_and_prefix_restrictions", 24)

    schedules = {tuple((k + t) % 8 for t in range(8)) for k in range(8)}
    schedule_symmetries = [g for g in range(48)
                          if {tuple(maps[g][x] for x in s) for s in schedules} == schedules]
    require(schedule_symmetries == [0, 4], "symmetries of exact cyclic schedule family")
    passed("cyclic_schedule_family_symmetry", 48)

    # Covariance premises only: all group actions and priority lists, no trajectories.
    order_to_id = {tuple(p["order"]): p["priority_id"] for p in orders}
    for r, g in product(range(48), repeat=2):
        transported = tuple(conjugations[r][h] for h in conjugations[g])
        require(transported == conjugations[table[r][g]], "priority action covariance")
    for r, h, y in product(range(48), range(48), range(8)):
        relabeled_h = conjugations[r][h]
        lhs = maps[inverses[relabeled_h]][maps[r][y]]
        rhs = maps[r][maps[inverses[h]][y]]
        require(lhs == rhs, "decoder covariance under simultaneous relabeling")
    passed("priority_and_decoder_covariance_no_trajectories", 20736)
    transported_lex_id = order_to_id[conjugations[4]]
    require(transported_lex_id == 3, "deterministic transported lex priority id")
    require(all(maps[4][x] == (x + 4) % 8 for x in range(8)), "half-turn schedules")
    require(set(conjugations[4][8:]) == set(range(8, 48)), "noncontrol world partition preserved")
    transported_grid = {(conjugations[4][h], (k + 4) % 8)
                        for h, k in product(range(8, 48), range(8))}
    require(transported_grid == set(product(range(8, 48), range(8))),
            "reference transport covers each noncontrol world/rotation exactly once")
    passed("v0_reference_transport_slice", 320)

    # Algebraic premise of the controls. This never creates or advances a learner.
    distinct_translation_cases = 0
    for target in range(8):
        for candidate in range(8):
            relative = map_compose(maps[inverses[candidate]], maps[target])
            require(all((relative[x] == x) == (candidate == target) for x in range(8)),
                    "distinct translation decoders disagree everywhere")
            distinct_translation_cases += 8
    passed("translation_control_lemma_all_state_cases", distinct_translation_cases)

    # These are theorem predictions, not measured outputs or executed controls.
    control_signatures = []
    for p in orders:
        for h, k in product(range(8), range(8)):
            r = p["rank_by_hypothesis"][h]
            require(0 <= r <= 7, "control true translation rank bound")
            control_signatures.append([p["priority_id"], h, k, r,
                                       "NULL" if h == 0 else "EXPANSION", 0, h,
                                       "FULL" if h == 0 else "SINGLETON_FLOOR", "FULL",
                                       "EMPTY" if h == 0 else "NON_SINGLETON_SETS", "EMPTY"])
    require(len(control_signatures) == 1536, "control product size")
    counts = Counter(r[4] for r in control_signatures)
    require(counts == {"NULL": 192, "EXPANSION": 1344}, "control signature counts")
    passed("theorem_signature_enumeration_no_controls_executed", 1536)

    manifest = {
        "schema": "a2-v1-priority-family-mathematical-audit/1",
        "standing": "AUDITED_CANDIDATE_NOT_PREREGISTRATION",
        "source": {"repository": "bjoern-janson/matrix", "commit": REPO_COMMIT,
                   "path": MODEL_PATH, "sha256": MODEL_SHA256, "git_blob": MODEL_BLOB},
        "composition": "T_(a*b) = T_a composed with T_b; output coordinate j reads sigma[j]",
        "conjugation": "c_g(h)=g*h*inverse(g)",
        "priority": "order[r]=index(c_g(H[r])); choose smallest rank of live original index",
        "hypotheses": [{"index": i, "sigma": h[0], "mask": h[1], "state_map": maps[i]}
                       for i, h in enumerate(H)],
        "all_48_conjugated_orders": [{"generator_index": g, "order": order}
                                    for g, order in enumerate(conjugations)],
        "distinct_priorities": orders,
        "center_indices": center,
        "ordered_list_stabilizer_indices": stabilizer,
        "conjugacy_classes": classes,
        "first_translation_blocks": first_blocks,
        "universally_fixed_positions": fixed_positions,
        "invariant_original_prefix_lengths": prefix_lengths,
        "exact_cyclic_schedule_symmetry_indices": schedule_symmetries,
        "v0_reference_transport": {
            "standing": "MATHEMATICALLY_DERIVABLE_NOT_MATERIALIZED_OR_EXECUTED",
            "relabeling_element_index": 4, "deduplicated_priority_id": transported_lex_id,
            "deduplicated_priority_representative_index": 3,
            "unit_mapping": "(h,P0,k) -> (c_4(h),P3,(k+4)%8)",
            "endpoint_mapping": "Phi'={g4(S): S in Phi}; same transport for Delta+ and Delta-",
            "additional_noncontrol_endpoints_determined": 320,
            "original_plus_transported_noncontrol_endpoints": 640,
            "note": "Other 7040 cells have no status of unresolved conferred by this audit."},
        "unit_universe_if_v0_world_partition_is_carried_forward": {
            "iteration_order": ["hypothesis_index", "priority_id", "rotation"],
            "all": {"hypothesis_indices_inclusive": [0, 47], "priorities": 24,
                    "rotations_inclusive": [0, 7], "paired_units": 9216},
            "theorem_controls": {"hypothesis_indices_inclusive": [0, 7], "paired_units": 1536},
            "noncontrol_endpoint_grid": {"hypothesis_indices_inclusive": [8, 47], "paired_units": 7680},
            "v0_noncontrol_reference_cells": {"priority_id": 0, "paired_units": 320,
                                               "standing": "ALREADY_OBSERVED_V0"},
            "new_priority_noncontrol_cells": {"priority_ids_inclusive": [1, 23], "paired_units": 7360,
                                              "standing": "NOT_EXECUTED_BY_THIS_AUDIT_INCLUDES_320_TRANSPORT_REFERENCES"},
            "remaining_noncontrol_cells_after_two_reference_slices": {
                "excluded_priority_ids": [0, 3], "paired_units": 7040,
                "standing": "NOT_RUN_NOT_CERTIFIED_ANALYTICALLY_UNRESOLVED"}},
        "check_results": checks,
        "execution": {"assay_units_executed": 0, "learner_updates": 0,
                      "theorem_controls_executed": 0, "repository_mutations": 0},
    }
    predictions = {
        "schema": "a2-v1-theorem-control-predictions/1",
        "standing": "ANALYTIC_PREDICTIONS_NOT_EXECUTION",
        "columns": ["priority_id", "hypothesis_index", "rotation", "predicted_training_failures",
                    "class", "active_control", "active_treatment", "phi_control", "phi_treatment",
                    "delta_plus", "delta_minus"],
        "set_codes": {"FULL": "all 256 subsets of Omega", "SINGLETON_FLOOR": "empty set plus eight singletons",
                      "NON_SINGLETON_SETS": "all 247 subsets of size at least two", "EMPTY": "empty family"},
        "rows": control_signatures,
    }
    return manifest, predictions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-path", type=Path)
    args = parser.parse_args()
    if args.source_path:
        source = args.source_path.read_bytes()
        require(hashlib.sha256(source).hexdigest() == MODEL_SHA256, "pinned model SHA-256")
        blob = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
        require(blob == MODEL_BLOB, "pinned model Git blob")
    manifest, predictions = audit()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    seals = {}
    for name, data in [("PRIORITY_FAMILY_AUDIT.json", manifest),
                       ("THEOREM_CONTROL_PREDICTIONS.json", predictions)]:
        content = canonical(data)
        with (args.output_dir / name).open("xb") as f:
            f.write(content)
        seals[name] = hashlib.sha256(content).hexdigest()
    print(json.dumps({"status": "PASS", "check_groups": len(manifest["check_results"]),
                      "distinct_orders": 24, "center": [0, 7], "assay_units_executed": 0,
                      "source_bytes_checked": bool(args.source_path), "sha256": seals}, sort_keys=True))


if __name__ == "__main__":
    main()
