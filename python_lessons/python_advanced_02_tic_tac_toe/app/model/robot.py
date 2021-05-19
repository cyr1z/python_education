"""
Robot model.

"""

from app.controller.utils import get_player_name
from app.model.player import Player
from settings import ROBOT_NAME, X_SYMBOL, O_SYMBOL, PLAYER_ONE_CREATE


class Robot(Player):
    """
    Robot class.
    """

    def __init__(self, symbol):
        super().__init__(ROBOT_NAME, symbol)


def get_user_and_robot():
    """
    get new user and robot
    :return: list
    """
    print(PLAYER_ONE_CREATE)
    name1 = get_player_name()
    player_1 = Player(name1, X_SYMBOL)
    player_2 = Robot(O_SYMBOL)
    return [player_1, player_2]