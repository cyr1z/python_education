"""
Robot model.

"""
from copy import deepcopy

from app.model.table import GameTable
from app.model.utils import get_player_name
from app.model.player import Player
from settings import ROBOT_NAME, X_SYMBOL, O_SYMBOL, PLAYER_ONE_CREATE


def get_user_and_robot():
    """
    get new user and robot
    :return: list
    """
    print(PLAYER_ONE_CREATE)
    name1 = get_player_name()
    player_1 = Player(name1, X_SYMBOL)
    player_2 = Robot(O_SYMBOL)
    return [player_2, player_1]


def utility(table):
    status = None
    if any(_ <= table.x_choices for _ in table.wins):
        status = -10
    elif any(_ <= table.o_choices for _ in table.wins):
        status = 10
    elif not table.variants:
        status = 0
    return status, None


def minimax(table):
    if table.is_terminal:
        best = utility(table)

    else:
        best = (-1, None) if table.is_maximize_player else (1, None)
        for item in table.variants:
            inner_table = deepcopy(table)
            inner_table.move(item)
            value = minimax(inner_table)[0]
            if table.is_maximize_player and value > best[0] or value < best[0]:
                best = (value, item)
    return best


class Robot(Player):
    """
    Robot class.
    """

    def __init__(self, symbol):
        super().__init__(ROBOT_NAME, symbol)

    def get_choice(self, table: GameTable) -> int:
        """
        Robot select item number.
        :param table: GameTable
        :return: int

        if len(table.variants) == 9:
            result = 5
        else:
            result = minimax(table)[1]
        """
        result = minimax(table)[1]
        return result
