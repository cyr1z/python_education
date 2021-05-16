"""
Game module.
"""
import logging
from itertools import chain
from utils import get_digit

from table import GameTable
from settings import NUMBERS_MAP, MESSAGE_FORMAT, TIME_FORMAT, LOGFILE

# logging wins
logging.basicConfig(
    level=logging.INFO,
    filename=LOGFILE,
    format=MESSAGE_FORMAT,
    datefmt=TIME_FORMAT,
)

score = {}


class GameOver(Exception):
    """Win or Draw Game Over Exception."""


class Game:
    """
    Game play class
    """

    def __init__(self, table_grid, numbers_map):
        self.table = table_grid
        self.table_choices = list(chain(*numbers_map))

    def play(self, player):
        """
        play step for player
        :param player: Player
        :return:
        """
        print(self.table)
        number = get_digit(
            self.table_choices,
            f"{player.name}, select number: "
        )
        self.table_choices.remove(number)
        self.table.change_item(number, player.symbol)
        player.make_choice(number)
        if player.is_player_win():
            message = f"  {player.name}, WIN!!!"
            logging.info(message)
            raise GameOver(message)
        if not self.table_choices:
            message = " DRAW "
            raise GameOver(message)

    def step(self, player):
        """
        running game step for player
        :param player: Player
        :return: Player
        """
        try:
            self.play(player)
        except GameOver as game_over:
            print(game_over)
            print(self.table)
            if player.winner:
                score[player.name] += 1
            return player


def game_play(player1, player2, is_new_game=False):
    """
    Gameplay with two players.
    :param is_new_game: bool
    :param player1: Player
    :param player2: Player
    :return:
    """
    global score
    if is_new_game:
        score = {player1.name: 0, player2.name: 0}
    else:
        player1.clear()
        player2.clear()

    table = GameTable(NUMBERS_MAP)
    game = Game(table_grid=table, numbers_map=NUMBERS_MAP)

    while True:
        winner = game.step(player1)
        if winner:
            break

        winner = game.step(player2)
        if winner:
            break

    if not is_new_game:
        logging.info(score)
