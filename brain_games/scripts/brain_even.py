from brain_games.cli import welcome_user
from brain_games.games.even import start_game


def main():
    name = welcome_user()
    start_game(name)


if __name__ == '__main__':
    main()
