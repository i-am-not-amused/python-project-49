import random

INIT_MSG = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
NUMERIC_INPUT = False

_EVEN_MIN_RANDOM = 1
_EVEN_MAX_RANDOM = 100


def generate_question() -> tuple[int, str]:
    """
    Generate number and correct answer for it.
    If generated number is even, the answer is "yes", otherwise "no".
    """
    number = random.randint(_EVEN_MIN_RANDOM, _EVEN_MAX_RANDOM)
    answer = "yes" if number % 2 == 0 else "no"
    return number, answer
