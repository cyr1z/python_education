"""
module for calculate robot choice in game step.
"""

from random import choice


def make_choice(choices: list) -> int:
    """
    Robot select item number.
    :param choices: list
    :return: int
    """
    return choice(choices)
