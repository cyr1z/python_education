"""
Player module
"""

from settings import X_SYMBOL, O_SYMBOL, PLAYER_ONE_CREATE, PLAYER_TWO_CREATE
from app.controller.utils import get_player_name


class Player:
    """
    Player class
    """

    def __init__(self, name, symbol):
        self.name = name.capitalize()
        self.symbol = symbol


def get_new_users():
    """
    get 2 new players
    :return: list
    """
    print(PLAYER_ONE_CREATE)
    name1 = get_player_name()
    player_1 = Player(name1, X_SYMBOL)
    print(PLAYER_TWO_CREATE)
    name2 = get_player_name(name1)
    player_2 = Player(name2, O_SYMBOL)
    return [player_1, player_2]
