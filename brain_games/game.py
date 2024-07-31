from enum import Enum

from brain_games.cli import get_user_input, welcome_user


class GameType(str, Enum):
    even = "even"
    calc = "calc"
    gcd = "gcd"
    progression = "progression"
    prime = "prime"


MAX_QUESTION_COUNT = 3


def start_game(game_name: str | None = None):
    user_name = welcome_user()

    match game_name:
        case GameType.even:
            from brain_games.games import even as game
        case GameType.calc:
            from brain_games.games import calc as game
        case GameType.gcd:
            from brain_games.games import gcd as game
        case GameType.progression:
            from brain_games.games import progression as game
        case GameType.prime:
            from brain_games.games import prime as game
        case _:
            return

    run(user_name, game)


def run(user_name: str, game):
    print(game.INIT_MSG)
    for _ in range(MAX_QUESTION_COUNT):
        number, correct_answer = game.generate_question()
        print(f"Question: {number}")
        user_answer = get_user_input("Your answer:", numeric=game.NUMERIC_INPUT)
        result = check_answer(user_answer, correct_answer)
        if not result:
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")


def check_answer(user: str | int, correct: str | int) -> bool:
    is_correct = user == correct
    if is_correct:
        print("Correct!")
    else:
        print(f"'{user}' is wrong answer ;(. Correct answer was '{correct}'.")
    return is_correct
