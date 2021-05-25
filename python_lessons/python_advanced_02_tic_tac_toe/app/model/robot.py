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


class Minimax:
    def __init__(self, table):
        self.table = deepcopy(table)

    def is_maximize_player(self):
        return len(self.table.x_choices) > len(self.table.o_choices)

    def max_value(self):
        if self.table.is_terminal:
            return self.table.utility

        best_score = float('-inf')
        for item in self.table.variants:
            self.table.move(item)
            score = self.min_value()
            if best_score < score:
                best_score = score
        return best_score

    def min_value(self):
        if self.table.is_terminal:
            return self.table.utility

        best_score = float('inf')
        for item in self.table.variants:
            self.table.move(item)
            score = self.max_value()
            if best_score > score:
                best_score = score
        return best_score

    def best_choice(self):
        best_score = float('-inf')
        for item in self.table.variants:
            self.table.move(item)
            score = self.min_value()
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
        minimax = Minimax(table)
        return minimax.best_choice()
