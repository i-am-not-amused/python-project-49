import random

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def generate_expression() -> tuple[str, int]:
    """Generate expression and correct answer for it."""
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    op = random.choice(list(operations.keys()))
    expression = f"{num1} {op} {num2}"
    answer = operations[op](num1, num2)
    return expression, answer
