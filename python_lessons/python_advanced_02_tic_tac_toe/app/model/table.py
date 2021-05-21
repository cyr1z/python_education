"""
Game table class

"""
from copy import deepcopy
from itertools import chain

from app.model.win import Win
from settings import X_SYMBOL, WIN_MESSAGE, DRAW_MESSAGE, NUMBERS_MAP

win = Win(NUMBERS_MAP)


class GameTable:
    """
    game table with element change methods.

    """

    def __init__(self, numbers_map):
        self.grid = deepcopy(numbers_map)
        self.x_choices = set()
        self.o_choices = set()
        self.variants = list(chain(*numbers_map))
        self.wins = win.combinations

    @property
    def choices(self):
        """
        checked X and 0 cells for table view.
        :return:
        """
        return {'x_choices': self.x_choices, 'o_choices': self.o_choices}

    def is_player_win(self, choices: set) -> bool:
        """
        check is player win
        :return: bool
        """
        result = False
        if len(choices) >= 3:
            for item in self.wins:
                if item <= choices:
                    result = True
        return result

    def choice_handler(self, number: int, player):
        """
        Remove number from variants and add to choices
        and run winner check
        :param player: Player
        :param number: int
        :return:
        """
        self.variants.remove(number)
        if player.symbol == X_SYMBOL:
            player_choices = self.x_choices
        else:
            player_choices = self.o_choices
        player_choices.add(number)

        result = {}
        if self.is_player_win(player_choices):
            message = WIN_MESSAGE.format(player.name)
            result = {'message': message, 'status': 1, 'winner': player.name}
        if not self.variants:
            message = DRAW_MESSAGE
            result = {'message': message, 'status': 0, 'winner': None}
        return result
