from brain_games.cli import get_user_input, welcome_user
from brain_games.generators.calc import generate_expression
from brain_games.generators.even import generate_number
from brain_games.generators.gcd import generate_gcd
from brain_games.generators.prime import generate_prime
from brain_games.generators.progression import generate_progression

MAX_QUESTION_COUNT = 3


def start_game(game_name: str | None = None):
    numeric_input = False
    user_name = welcome_user()

    match game_name:
        case "even":
            generator = generate_number
            init_msg = ("Answer \"yes\" if the number is even, "
                        "otherwise answer \"no\".")
        case "calc":
            init_msg = "What is the result of the expression?"
            numeric_input = True
            generator = generate_expression
        case "gcd":
            init_msg = "Find the greatest common divisor of given numbers."
            numeric_input = True
            generator = generate_gcd
        case "progression":
            init_msg = "What number is missing in the progression?"
            numeric_input = True
            generator = generate_progression
        case "prime":
            init_msg = ("Answer \"yes\" if given number is prime. "
                        "Otherwise answer \"no\".")
            generator = generate_prime
        case _:
            return

    run(user_name, init_msg, numeric_input, generator)


def run(user_name: str, init_msg: str, numeric_input, generator):
    print(init_msg)
    for _ in range(MAX_QUESTION_COUNT):
        number, correct_answer = generator()
        print(f"Question: {number}")
        user_answer = get_user_input("Your answer:", numeric=numeric_input)
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
