#!/usb/bin/env python3
from brain_games.game import start_game, GameType


def main():
    start_game(game_name=GameType.gcd)


if __name__ == '__main__':
    main()
