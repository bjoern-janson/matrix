"""Exhaustive endpoint and an independent analytic validation oracle."""
from dataclasses import dataclass
from fractions import Fraction
from . import model as m


@dataclass(frozen=True, slots=True)
class Measurement:
    frontier: tuple[int, ...]
    executions: tuple[tuple[m.Execution, ...], ...]
    witnesses: tuple[tuple[int, ...], ...]
    subsets_checked: int


def measure(hidden_index: int, constructor: m.ConstructorInput) -> Measurement:
    policies = m.realize(constructor)
    rows = tuple(tuple(m.execute(p, m.HYPOTHESES[hidden_index], x)
                       for x in m.STATES) for p in policies)
    frontier = []
    witnesses = []
    for subset in range(256):
        available = []
        # Same realized policy must work for every x in this subset.
        for index, row in enumerate(rows):
            if all(row[x].success and row[x].cost <= m.BUDGET
                   for x in m.STATES if subset & (1 << x)):
                available.append(index)
        witnesses.append(tuple(available))
        if available:
            frontier.append(subset)
    return Measurement(tuple(frontier), rows, tuple(witnesses), 256)


def success_states(measurement: Measurement) -> tuple[int, ...]:
    return tuple(x for x, receipt in enumerate(measurement.executions[-1])
                 if receipt.success and receipt.cost <= m.BUDGET)


def weighted_success(states) -> Fraction:
    return sum((Fraction(2 ** x, 255) for x in states), Fraction(0))


def utility(measurement: Measurement) -> Fraction:
    return weighted_success(success_states(measurement))


def oracle_success(hidden_index: int, active_index: int) -> tuple[int, ...]:
    # Invertible channels: decoding is correct iff the two forward images agree.
    # Deliberately uses string coordinates, not model.channel/decode/execute.
    true_h = m.HYPOTHESES[hidden_index]
    learned_h = m.HYPOTHESES[active_index]
    successes = []
    for x in range(8):
        bits = format(x, '03b')
        images = []
        for h in (true_h, learned_h):
            images.append(''.join(str((int(bits[s]) + b) % 2)
                                  for s, b in zip(h.sigma, h.mask)))
        if images[0] == images[1]:
            successes.append(x)
    return tuple(successes)


def oracle_frontier(states) -> tuple[int, ...]:
    # Analytic powerset construction, independent of policy/subset enumeration.
    feasible = {0, 1, 2, 4, 8, 16, 32, 64, 128}
    subsets = {0}
    for x in states:
        subsets |= {s | (1 << x) for s in tuple(subsets)}
    return tuple(sorted(feasible | subsets))


def downward_closed(frontier) -> bool:
    family = set(frontier)
    return all((s ^ (1 << x)) in family for s in family
               for x in range(8) if s & (1 << x))


def primary_record(unit, control: Measurement, treatment: Measurement):
    minus = sorted(set(control.frontier) - set(treatment.frontier))
    plus = sorted(set(treatment.frontier) - set(control.frontier))
    if plus and minus:
        standing = 'TRADEOFF'
    elif plus:
        standing = 'EXPANSION'
    elif minus:
        standing = 'CONTRACTION'
    else:
        standing = 'NULL'
    return {'unit': list(unit), 'phi_control': list(control.frontier),
            'phi_treatment': list(treatment.frontier), 'delta_plus': plus,
            'delta_minus': minus, 'classification': standing}
