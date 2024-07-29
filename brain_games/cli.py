import prompt


def welcome_user():
    """Ask for user's name, print greetings and return entered name"""
    print("Welcome to the Brain Games!")
    name = get_user_input("May I have your name?")
    print(f"Hello, {name}!")
    return name


def get_user_input(message: str, numeric: bool = False) -> str | int:
    message = f"{message} "
    data = prompt.integer(message) if numeric else prompt.string(message)
    return data
