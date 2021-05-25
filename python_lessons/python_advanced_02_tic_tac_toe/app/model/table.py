"""
Game table class

"""
from copy import deepcopy
from itertools import chain

from app.model.win import Win
from app.view.table_view import TableView
from settings import WIN_MESSAGE, DRAW_MESSAGE, NUMBERS_MAP

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

    @property
    def is_terminal(self):
        return any(_ <= self.x_choices for _ in self.wins) or \
               any(_ <= self.o_choices for _ in self.wins) or not self.variants

    @property
    def is_maximize_player(self):
        return len(self.x_choices) > len(self.o_choices)

    @property
    def utility(self):
        if any(_ <= self.x_choices for _ in self.wins):
            status = -10
        elif any(_ <= self.o_choices for _ in self.wins):
            status = 10
        elif not self.variants:
            status = 0
        return status

    def x_move(self, number):
        self.variants.remove(number)
        self.x_choices.add(number)

    def o_move(self, number):
        self.variants.remove(number)
        self.o_choices.add(number)

    def move(self, number):
        if self.is_maximize_player:
            self.o_move(number)
        else:
            self.x_move(number)

    def choice_handler(self, number: int, player):
        """
        Remove number from variants and add to choices
        and run winner check
        :param player: Player
        :param number: int
        :return:
        """
        self.move(number)

        result = {}
        if self.is_terminal and self.utility:
            message = WIN_MESSAGE.format(player.name)
            result = {'message': message, 'status': 1, 'winner': player.name}
        if self.is_terminal and not self.utility:
            message = DRAW_MESSAGE
            result = {'message': message, 'status': 0, 'winner': None}
        return result

    def __str__(self):
        return TableView(**self.choices)
