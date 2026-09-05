"""Invariant checks run after all theorem-derived control signatures match."""
from . import model as m, measurement as e


def check_invariants(pairs):
    checks = []

    def checked(name, condition):
        m.require(condition, 'invariant failed: ' + name)
        checks.append({'name': name, 'status': 'PASS'})

    checked('unit_partition', len(m.HYPOTHESES) == 48 and len(m.UNITS) == 384
            and len(m.CONTROLS) == 64 and len(m.UNRESOLVED) == 320
            and set(m.CONTROLS).isdisjoint(m.UNRESOLVED)
            and set(m.CONTROLS) | set(m.UNRESOLVED) == set(m.UNITS))

    # Primitive truth-table checks are not paired training/evaluation trajectories.
    # No unresolved unit is trained to perform this finite algebraic check.
    tables = []
    coordinate_correct = True
    for h in m.HYPOTHESES:
        table = []
        for x in range(8):
            text_bits = format(x, '03b')
            expected = tuple((int(text_bits[s]) + b) % 2 for s, b in zip(h.sigma, h.mask))
            observed = m.channel(h, x)
            coordinate_correct &= observed == expected and m.decode(h, observed) == x
            table.append(observed)
        tables.append(tuple(table))
    checked('48_distinct_invertible_channels', coordinate_correct and len(set(tables)) == 48)
    checked('hypothesis_order',
            [(h.sigma, h.mask) for h in m.HYPOTHESES] ==
            sorted((h.sigma, h.mask) for h in m.HYPOTHESES)
            and all(h.sigma == (0, 1, 2) for h in m.HYPOTHESES[:8]))
    checked('paired_clone_equality_and_isolation',
            all(p.clone_equal and p.mutable_disjoint for p in pairs))
    checked('constructor_information_boundary', set(m.ConstructorInput.__slots__) == {'task', 'active'}
            and all(type(a.constructor) is m.ConstructorInput for p in pairs
                    for a in (p.control, p.treatment)))

    histories_matched = charges_matched = truth_retained = control_fixed = True
    feedback_isolated = update_correct = True
    exact_availability = exact_accounting = exact_frontier = frozen = True
    formula_matches = histories_respected = True
    for pair in pairs:
        hi, rotation = pair.unit
        for episode, (c, t) in enumerate(zip(pair.control.trace, pair.treatment.trace)):
            histories_matched &= c['x'] == t['x'] == (rotation + episode) % 8
            histories_matched &= c['observations'] == t['observations']
            histories_matched &= c['query_slots'] == t['query_slots'] == [0, 1, 2]
            feedback_isolated &= c['feedback'] == [False, False]
            feedback_isolated &= t['feedback'] == [True, t['prediction'] == t['x']]
        for arm_index, arm in enumerate((pair.control, pair.treatment)):
            histories_matched &= len(arm.trace) == 8
            charges_matched &= arm.training_charge == 40 and arm.hypothesis_checks == 384
            frozen &= arm.evaluation_unchanged
            for trace in arm.trace:
                truth_retained &= hi in trace['live_after']
                charges_matched &= (trace['hypothesis_checks'] == 48 and
                                    trace['processing_charge'] == 1 and trace['primitive_charge'] == 4)
                if arm_index == 0:
                    control_fixed &= trace['live_after'] == list(range(48))
                else:
                    expected_live = []
                    # Independent forward-image characterization of the update:
                    # candidate decodes y to prediction iff T_candidate(prediction)=y.
                    prediction_bits = format(trace['prediction'], '03b')
                    for index in trace['live_before']:
                        h = m.HYPOTHESES[index]
                        image = [(int(prediction_bits[s]) + b) % 2
                                 for s, b in zip(h.sigma, h.mask)]
                        if (image == trace['observations']) == trace['feedback'][1]:
                            expected_live.append(index)
                    update_correct &= trace['live_after'] == expected_live
            policies = m.realize(arm.constructor)
            exact_availability &= len(policies) == 9
            exact_availability &= tuple(p.target for p in policies[:8]) == tuple(range(8))
            exact_availability &= all(p.kind == 'immediate' for p in policies[:8])
            exact_availability &= policies[-1].kind == 'diagnostic'
            exact_availability &= policies[-1].hypothesis == arm.constructor.active
            histories_respected &= policies == m.realize(m.ConstructorInput(active=arm.constructor.active))
            for index, rows in enumerate(arm.measurement.executions):
                for x, receipt in enumerate(rows):
                    exact_accounting &= receipt.cost == (2 if index < 8 else 5)
                    exact_accounting &= receipt.cost == 1 + len(receipt.actions)
                    exact_accounting &= receipt.success == (receipt.actions[-1] == ('r', x))
                    if index < 8:
                        histories_respected &= receipt.actions == (('r', index),)
                    else:
                        histories_respected &= receipt.actions[:3] == (('q', 0), ('q', 1), ('q', 2))
                        histories_respected &= policies[-1].action(receipt.observations) == receipt.actions[-1]
            measurement = arm.measurement
            exact_frontier &= (measurement.subsets_checked == 256 and
                               len(measurement.witnesses) == 256 and
                               e.downward_closed(measurement.frontier))
            expected_success = e.oracle_success(hi, arm.constructor.active)
            formula_matches &= e.success_states(measurement) == expected_success
            formula_matches &= measurement.frontier == e.oracle_frontier(expected_success)

    checked('same_exogenous_training_schedule_and_query_slots', histories_matched)
    checked('matched_fixed_training_work_and_charges', charges_matched)
    checked('feedback_interface_only', feedback_isolated)
    checked('true_hypothesis_retained_after_each_update', truth_retained)
    checked('control_version_set_never_changes', control_fixed)
    checked('learning_update_matches_independent_forward_predicate', update_correct)
    checked('exact_nine_policy_realization', exact_availability)
    checked('policy_actions_depend_only_on_declared_history', histories_respected)
    checked('charged_realization_query_and_repair_costs', exact_accounting)
    checked('all_256_subsets_and_downward_closure', exact_frontier)
    checked('independent_success_and_frontier_oracles', formula_matches)
    checked('no_learning_during_evaluation', frozen)
    return checks
