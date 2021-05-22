"""
Player module
"""
from app.model.table import GameTable
from settings import X_SYMBOL, O_SYMBOL, PLAYER_ONE_CREATE, \
    PLAYER_TWO_CREATE, SELECT_NUMBER
from app.model.utils import get_player_name, get_digit


class Player:
    """
    Player class
    """

    def __init__(self, name, symbol):
        self.name = name.capitalize()
        self.symbol = symbol

    def get_choice(self, table: GameTable) -> int:
        """
        Human select item number.
        :param table: GameTable
        :return: int
        """
        return get_digit(table.variants, SELECT_NUMBER.format(self.name))


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
