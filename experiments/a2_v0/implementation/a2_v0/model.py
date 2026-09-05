"""Finite execution. Learners and policies never receive hidden world labels."""
from dataclasses import dataclass, field
from itertools import permutations, product

TASK = 'SWITCHBOARD_3'
BUDGET = 5
STATES = tuple(range(8))


class InvalidAssay(RuntimeError):
    status = 'INVALID_NO_SCIENTIFIC_RESULT'


def require(condition, message):
    if not condition:
        raise InvalidAssay(message)


@dataclass(frozen=True, slots=True)
class Hypothesis:
    sigma: tuple[int, int, int]
    mask: tuple[int, int, int]

    def __post_init__(self):
        require(sorted(self.sigma) == [0, 1, 2], 'invalid permutation')
        require(len(self.mask) == 3 and all(b in (0, 1) for b in self.mask),
                'invalid channel mask')


HYPOTHESES = tuple(Hypothesis(s, b) for s in permutations(range(3))
                   for b in product((0, 1), repeat=3))
UNITS = tuple((i, k) for i in range(48) for k in range(8))
CONTROLS = tuple(u for u in UNITS if u[0] < 8)
UNRESOLVED = tuple(u for u in UNITS if u[0] >= 8)


def channel(h: Hypothesis, x: int) -> tuple[int, ...]:
    require(type(x) is int and x in STATES, 'invalid latent state')
    return tuple(((x >> (2 - h.sigma[j])) & 1) ^ h.mask[j] for j in range(3))


def decode(h: Hypothesis, observations: tuple[int, ...]) -> int:
    require(len(observations) == 3 and all(o in (0, 1) for o in observations),
            'decoder requires exactly three binary observations')
    x = 0
    for j, observed in enumerate(observations):
        x |= (observed ^ h.mask[j]) << (2 - h.sigma[j])
    return x


@dataclass(frozen=True, slots=True)
class Feedback:
    valid: bool
    correct: bool

    def __post_init__(self):
        require(type(self.valid) is bool and type(self.correct) is bool,
                'feedback must contain two booleans')
        require(self.valid or not self.correct, 'noninformative token must be (False, False)')


@dataclass(frozen=True, slots=True)
class Processing:
    hypothesis_checks: int
    charge: int


@dataclass(frozen=True, slots=True)
class ConstructorInput:
    task: str = TASK
    active: int = 0

    def __post_init__(self):
        require(self.task == TASK, 'undeclared constructor task')
        require(type(self.active) is int and 0 <= self.active < 48,
                'invalid constructor hypothesis')


@dataclass(slots=True)
class Learner:
    live: set[int] = field(default_factory=lambda: set(range(48)))
    frozen: bool = False

    @property
    def active(self):
        require(bool(self.live), 'empty version set')
        return min(self.live)

    def snapshot(self):
        return (tuple(sorted(self.live)), self.frozen)

    def predict(self, observations):
        return decode(HYPOTHESES[self.active], observations)

    def update(self, observations, attempted_repair, feedback):
        require(not self.frozen, 'learning is disabled after the training freeze')
        require(type(attempted_repair) is int and attempted_repair in STATES,
                'invalid attempted repair')
        # Full fixed scan in both arms, even after the version set shrinks.
        consistent = set()
        checks = 0
        for i, h in enumerate(HYPOTHESES):
            agrees = decode(h, observations) == attempted_repair
            if agrees == feedback.correct:
                consistent.add(i)
            checks += 1
        proposed = self.live.intersection(consistent)
        if feedback.valid:
            require(bool(proposed), 'feedback eliminated every hypothesis')
            self.live = proposed
        return Processing(checks, 1)

    def freeze(self):
        self.frozen = True
        return ConstructorInput(active=self.active)


@dataclass(frozen=True, slots=True)
class RealizedPolicy:
    kind: str
    target: int | None
    hypothesis: int | None
    provenance: tuple
    realization_cost: int = 1

    def action(self, observations):
        if self.kind == 'immediate':
            return ('r', self.target)
        require(self.kind == 'diagnostic', 'undeclared policy form')
        if len(observations) < 3:
            return ('q', len(observations))
        return ('r', decode(HYPOTHESES[self.hypothesis], observations))


def realize(i: ConstructorInput) -> tuple[RealizedPolicy, ...]:
    require(type(i) is ConstructorInput, 'constructor accepts only declared input')
    immediate = tuple(RealizedPolicy('immediate', z, None,
                      (i.task, i.active, 'immediate', z)) for z in STATES)
    diagnostic = RealizedPolicy('diagnostic', None, i.active,
                                (i.task, i.active, 'diagnostic', i.active))
    return immediate + (diagnostic,)


@dataclass(frozen=True, slots=True)
class Execution:
    success: bool
    cost: int
    actions: tuple[tuple[str, int], ...]
    observations: tuple[int, ...]


def execute(policy: RealizedPolicy, hidden_h: Hypothesis, x: int) -> Execution:
    # The verifier owns the hidden environment; action() sees observations only.
    observations = ()
    actions = []
    cost = policy.realization_cost
    for _ in range(4):
        kind, index = policy.action(observations)
        actions.append((kind, index))
        cost += 1
        if kind == 'q' and index in (0, 1, 2):
            observations += (channel(hidden_h, x)[index],)
        elif kind == 'r' and index in STATES:
            return Execution(index == x, cost, tuple(actions), observations)
        else:
            return Execution(False, cost, tuple(actions), observations)
    return Execution(False, cost, tuple(actions), observations)
