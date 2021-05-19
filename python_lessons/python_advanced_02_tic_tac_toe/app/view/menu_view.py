"""
Menu module.

"""
from termtables import to_string

from settings import MENU_WELCOME


class Menu:
    """
    menu

    """

    def __init__(self, menu_list):
        self.menu_list = menu_list

    def __str__(self):
        return MENU_WELCOME + to_string(self.menu_list, padding=(0, 2))

    @property
    def numbers(self) -> list:
        """
        numbers for select menu item/
        :return: list
        """
        return list(list(zip(*self.menu_list))[0])
