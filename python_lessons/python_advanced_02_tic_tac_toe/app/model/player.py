"""
Player module
"""

from settings import X_SYMBOL, O_SYMBOL, PLAYER_ONE_CREATE, PLAYER_TWO_CREATE
from app.controller.utils import get_player_name


class Player:
    """
    Player class
    """

    def __init__(self, name, win_combinations, symbol):
        # TODO: move this to Game controller
        self.win_combinations = win_combinations
        # TODO: move this to Game controller
        self.choices = set()
        self.name = name.capitalize()
        self.symbol = symbol

    def is_player_win(self) -> bool:
        # TODO: move this to Game controller
        """
        check is player win
        :return: bool
        """
        result = 0
        if len(self.choices) >= 3:
            for item in self.win_combinations:
                if item <= self.choices:
                    result = True
        return result

    # TODO: move this to Game controller
    def make_choice(self, number: int):
        """
        add number to choices
        :param number: int
        :return:
        """
        self.choices.add(number)

    # TODO: move this to Game controller
    def clear(self):
        """ clear choices and winner mark"""
        self.choices.clear()


def get_new_users(win_combinations):
    """
    get 2 new players
    :param win_combinations: list
    :return: list
    """
    print(PLAYER_ONE_CREATE)
    name1 = get_player_name()
    player_1 = Player(name1, win_combinations, X_SYMBOL)
    print(PLAYER_TWO_CREATE)
    name2 = get_player_name(name1)
    player_2 = Player(name2, win_combinations, O_SYMBOL)
    return [player_1, player_2]
