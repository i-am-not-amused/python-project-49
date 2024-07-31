import random


INIT_MSG = "What number is missing in the progression?"
NUMERIC_INPUT = True

_PROG_MIN_RANDOM = 1
_PROG_MAX_RANDOM = 50
_COUNT_MIN_RANDOM = 5
_COUNT_MAX_RANDOM = 10


def get_sequence():
    start = random.randint(_PROG_MIN_RANDOM, _PROG_MAX_RANDOM)
    step = random.randint(_PROG_MIN_RANDOM, _PROG_MAX_RANDOM)
    count = random.randint(_COUNT_MIN_RANDOM, _COUNT_MAX_RANDOM)
    stop = count * step + start
    return list(range(start, stop, step))


def generate_question() -> tuple[str, int]:
    sequence = get_sequence()
    random_idx = random.randint(0, len(sequence) - 1)
    answer, sequence[random_idx] = sequence[random_idx], ".."
    progression = " ".join(map(str, sequence))
    return progression, answer
