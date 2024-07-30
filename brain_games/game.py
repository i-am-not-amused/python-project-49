def check_answer(user: str | int, correct: str | int) -> bool:
    is_correct = user == correct
    if is_correct:
        print("Correct!")
    else:
        print(f"{user!r} is wrong answer ;(. Correct answer was {correct!r}.")
    return is_correct
