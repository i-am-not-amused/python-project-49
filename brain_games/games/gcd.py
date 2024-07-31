import random

INIT_MSG = "Find the greatest common divisor of given numbers."
NUMERIC_INPUT = True

_GCD_MIN_RANDOM = 1
_GCD_MAX_RANDOM = 100


def get_gcd(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return max(a, b)


def generate_question():
    num1, num2, gcd = 0, 0, 0
    while gcd < 2:
        num1 = random.randint(_GCD_MIN_RANDOM, _GCD_MAX_RANDOM)
        num2 = random.randint(_GCD_MIN_RANDOM, _GCD_MAX_RANDOM)
        gcd = get_gcd(num1, num2)
    return f"{num1} {num2}", gcd
