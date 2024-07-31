import random

init_msg = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
numeric_input = False


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    answer = "yes" if is_prime(number) else "no"
    return number, answer
