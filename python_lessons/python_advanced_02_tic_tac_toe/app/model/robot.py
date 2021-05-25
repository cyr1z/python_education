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
    return [player_1, player_2]


def minimax(table):
    if table.is_terminal:
        return table.utility

    best_score = float('inf')
    if table.is_maximize_player:
        best_score *= -1
    for item in table.variants:
        table.move(item)
        score = minimax(table)
        if table.is_maximize_player and best_score < score:
            best_score = score
        elif not table.is_maximize_player and best_score > score:
            best_score = score
    return best_score


def best_choice(table):
    table = deepcopy(table)
    best_score = float('-inf')
    for item in table.variants:
        table.move(item)
        score = minimax(table)
        if best_score < score:
            best_score = score
            result = item
    return result


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
        """

        return best_choice(table)
