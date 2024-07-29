import prompt


def welcome_user():
    """Ask for user's name, print greetings and return entered name"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
