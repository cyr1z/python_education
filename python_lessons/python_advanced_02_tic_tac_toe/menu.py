"""
Menu module.

"""
from termtables import to_string

from utils import get_digit


class Menu:
    """
    menu

    """

    def __init__(self, menu_list, ask_numbers):
        self.menu_list = menu_list
        self.ask_numbers = ask_numbers

    def __str__(self):
        return 'Select one: \n' + to_string(self.menu_list, padding=(0, 2))

    @property
    def numbers(self) -> list:
        """
        numbers for select menu item/
        :return: list
        """
        return list(list(zip(*self.menu_list))[0])

    def get_choice(self) -> int:
        """
        Print the menu and get choices.
        :return: int
        """
        print(self)
        return get_digit(self.numbers, self.ask_numbers)
