"""
Game table class

"""
from copy import deepcopy
from itertools import chain


class GameTable:
    """
    game table with element change methods.

    """

    def __init__(self, numbers_map):
        self.grid = deepcopy(numbers_map)
        self.x_choices = set()
        self.o_choices = set()
        self.variants = list(chain(*numbers_map))

    @property
    def choices(self):
        return {'x_choices': self.x_choices, 'o_choices': self.o_choices}
