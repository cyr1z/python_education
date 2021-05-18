"""
Robot model.

"""
from random import choice

from app.controller.utils import get_player_name
from app.model.player import Player
from settings import ROBOT_NAME, X_SYMBOL, O_SYMBOL, PLAYER_ONE_CREATE


class Robot(Player):
    """
    Robot class.
    """
    def __init__(self, win_combinations, symbol):
        super().__init__(ROBOT_NAME, win_combinations, symbol)


def make_choice(choices: list) -> int:
    """
    Robot select item number.
    :param choices: list
    :return: int
    """
    return choice(choices)


def get_user_and_robot(win_combinations):
    """
    get new user and robot
    :param win_combinations: list
    :return: list
    """
    print(PLAYER_ONE_CREATE)
    name1 = get_player_name()
    player_1 = Player(name1, win_combinations, X_SYMBOL)
    player_2 = Robot(win_combinations, O_SYMBOL)
    return [player_1, player_2]
