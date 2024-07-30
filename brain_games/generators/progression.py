import random


def get_sequence():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    count = random.randint(5, 10)
    stop = count * step + start
    return [x for x in range(start, stop, step)]


def generate_progression() -> tuple[str, int]:
    sequence = get_sequence()
    random_idx = random.randint(0, len(sequence) - 1)
    answer, sequence[random_idx] = sequence[random_idx], ".."
    progression = " ".join(map(str, sequence))
    return progression, answer
