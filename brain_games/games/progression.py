import random


init_msg = "What number is missing in the progression?"
numeric_input = True


def get_sequence():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    count = random.randint(5, 10)
    stop = count * step + start
    return list(range(start, stop, step))


def generate_question() -> tuple[str, int]:
    sequence = get_sequence()
    random_idx = random.randint(0, len(sequence) - 1)
    answer, sequence[random_idx] = sequence[random_idx], ".."
    progression = " ".join(map(str, sequence))
    return progression, answer
