import random

from brain_games.cli import get_user_input
from brain_games.game import check_answer

MAX_QUESTION_COUNT = 3

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def generate_question() -> tuple[str, int]:
    """Generate number and correct answer for it."""
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    op = random.choice(list(operations.keys()))
    expression = f"{num1} {op} {num2}"
    answer = operations[op](num1, num2)
    return expression, answer


def new_question():
    number, correct_answer = generate_question()
    print(f"Question: {number}")
    user_answer = get_user_input("Your answer:", numeric=True)
    return check_answer(user_answer, correct_answer)


def start_game(name: str):
    print("What is the result of the expression?")
    for _ in range(MAX_QUESTION_COUNT):
        result = new_question()
        if not result:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
