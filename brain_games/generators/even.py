import random


def generate_number() -> tuple[int, str]:
    """
    Generate number and correct answer for it.
    If generated number is even, the answer is "yes", otherwise "no".
    """
    number = random.randint(1, 100)
    answer = "yes" if number % 2 == 0 else "no"
    return number, answer
