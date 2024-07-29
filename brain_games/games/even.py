import random

from brain_games.cli import get_user_input


MAX_QUESTION_COUNT = 3


def generate_question() -> tuple[int, str]:
    """
    Generate number and correct answer for it.

    If generated number is even, the answer is "yes", otherwise "no".
    """
    number = random.randint(1, 100)
    answer = "yes" if number % 2 == 0 else "no"
    return number, answer


def check_answer(user: str, correct: str) -> bool:
    """Checks if user answer is correct and shows appropriate message."""
    is_correct = user == correct
    if is_correct:
        print("Correct!")
    else:
        print(f"{user!r} is wrong answer ;(. Correct answer was {correct!r}.")
    return is_correct


def new_question():
    """Ask question, check user answer and return the result."""
    number, correct_answer = generate_question()
    print(f"Question: {number}")
    user_answer = get_user_input("Your answer:")
    return check_answer(user_answer, correct_answer)


def start_game(name: str):
    """
    Start a new game of even-odd.

    If all answers are correct, user will receive personal congratulations.
    Any wrong given answer will finish the game.
    """
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for _ in range(MAX_QUESTION_COUNT):
        result = new_question()
        if not result:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
