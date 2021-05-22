from copy import deepcopy

from termtables import to_string

from settings import NUMBERS_MAP, X_SYMBOL, O_SYMBOL


class TableView:
    def __init__(self, **kwargs):
        self.grid = deepcopy(NUMBERS_MAP)
        self.x_choices = kwargs.get('x_choices')
        self.o_choices = kwargs.get('o_choices')
        self.x_symbol = X_SYMBOL
        self.o_symbol = O_SYMBOL

    @staticmethod
    def replace_to_symbol(grid: list, choices: set, symbol: str):
        """
        change numbers to symbol in grid
        :param grid: list
        :param choices: set
        :param symbol: str players symbol
        :return:
        """
        for row in grid:
            for index, cell in enumerate(row):
                if cell in choices:
                    row[index] = symbol
        return grid

    def build_table_view(self):
        self.grid = self.replace_to_symbol(
            self.grid,
            self.x_choices,
            self.x_symbol
        )
        self.grid = self.replace_to_symbol(
            self.grid,
            self.o_choices,
            self.o_symbol
        )

    def __str__(self) -> str:
        self.build_table_view()
        return to_string(self.grid, padding=(1, 3))
