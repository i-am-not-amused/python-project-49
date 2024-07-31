import random

INIT_MSG = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
NUMERIC_INPUT = False

_PRIME_MIN_RANDOM = 1
_PRIME_MAX_RANDOM = 100


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(_PRIME_MIN_RANDOM, _PRIME_MAX_RANDOM)
    answer = "yes" if is_prime(number) else "no"
    return number, answer
