import random

init_msg = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
numeric_input = False


def generate_question() -> tuple[int, str]:
    """
    Generate number and correct answer for it.
    If generated number is even, the answer is "yes", otherwise "no".
    """
    number = random.randint(1, 100)
    answer = "yes" if number % 2 == 0 else "no"
    return number, answer
