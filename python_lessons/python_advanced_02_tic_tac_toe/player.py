"""
Player module
"""
from settings import X_SYMBOL, O_SYMBOL
from utils import get_player_name


class Player:
    """
    Player class
    """

    def __init__(self, name, win_combinations, symbol):
        self.win_combinations = win_combinations
        self.choices = set()
        self.name = name.capitalize()
        self.symbol = symbol
        self.winner = False

    def is_player_win(self) -> bool:
        """
        check is player win
        :return: bool
        """
        result = False
        if len(self.choices) >= 3:
            for item in self.win_combinations:
                if item <= self.choices:
                    result = True
        self.winner = result
        return result

    def make_choice(self, number: int):
        """
        add number to choices
        :param number: int
        :return:
        """
        self.choices.add(number)

    def clear(self):
        """ clear choices and winner mark"""
        self.choices.clear()
        self.winner = False


def get_new_users(win_combinations):
    """
    get new player
    :param win_combinations: list
    :return: list
    """
    print("== Player 1 ==")
    name1 = get_player_name()
    player_1 = Player(name1, win_combinations, X_SYMBOL)
    print("== Player 2 ==")
    name2 = get_player_name(name1)
    player_2 = Player(name2, win_combinations, O_SYMBOL)
    return [player_1, player_2]
