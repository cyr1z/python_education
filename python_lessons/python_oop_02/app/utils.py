"""
simple utils
"""
from .settings import NUMBER_REQUEST


def get_digit(items_count: int, welcome_string=NUMBER_REQUEST) -> int:
    """get digit from user input"""
    line = ''
    while not line.isdigit() and 0 <= int(line) <= items_count:
        line = input(welcome_string)
    return int(line)
