"""
module for calculate robot choice in game step.
"""

from random import choice

from app.model.table import GameTable


def make_choice(table: GameTable) -> int:
    """
    Robot select item number.
    :param table: GameTable
    :return: int
    """
    return choice(table.variants)
