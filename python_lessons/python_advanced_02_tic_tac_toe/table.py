"""
Game table class

"""
from copy import deepcopy
from termtables import to_string


class GameTable:
    """
    game table with element change methods.

    """

    def __init__(self, numbers_map):
        self.grid = deepcopy(numbers_map)

    def change_item(self, number: int, symbol: str):
        """
        change number to symbol in self.grid
        :param number: cell number
        :param symbol: players symbol
        :return:
        """
        for row in self.grid:
            for index, cell in enumerate(row):
                if cell == number:
                    row[index] = symbol

    def __str__(self) -> str:
        return to_string(self.grid, padding=(1, 3))
