"""
module for win combinations for tic-tac-toe 3x3 grid

"""


class Win:
    """
    win combination classes
    Win().combinations - all win combinations for numbers_map grid
    """

    def __init__(self, numbers_map: list):
        self.grid = numbers_map

    @staticmethod
    def get_cols(grid):
        """
        get cols of grid
        :param grid: list
        :return: list
        """
        return list(map(list, (zip(*grid))))

    @property
    def cols(self):
        """
        cols of numbers_map
        :return: list
        """
        return self.get_cols(self.grid)

    @property
    def rows(self):
        """
        rows of numbers_map
        :return:
        """
        return list(self.grid)

    @property
    def backward_diagonal(self):
        """
        backward_diagonal of numbers_map
        :return: tuple
        """
        blanc = [None] * 2
        grid = [blanc[i:] + row + blanc[:i] for i, row in enumerate(self.grid)]
        return self.get_cols(grid)[2]

    @property
    def forward_diagonal(self):
        """
        forward_diagonal of numbers_map
        :return: tuple
        """
        blanc = [None] * 2
        grid = [blanc[:i] + row + blanc[i:] for i, row in enumerate(self.grid)]
        return self.get_cols(grid)[2]

    @property
    def combinations(self):
        """
        win combinations for numbers_map grid
        :return: list
        """
        combinations = self.rows + self.cols
        combinations.append(self.forward_diagonal)
        combinations.append(self.backward_diagonal)
        return list(map(set, combinations))
