import random

INIT_MSG = "What is the result of the expression?"
NUMERIC_INPUT = True

_CALC_MIN_RANDOM = 1
_CALC_MAX_RANDOM = 25

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def generate_question() -> tuple[str, int]:
    """Generate expression and correct answer for it."""
    num1 = random.randint(_CALC_MIN_RANDOM, _CALC_MAX_RANDOM)
    num2 = random.randint(_CALC_MIN_RANDOM, _CALC_MAX_RANDOM)
    op = random.choice(list(operations.keys()))
    expression = f"{num1} {op} {num2}"
    answer = operations[op](num1, num2)
    return expression, answer
