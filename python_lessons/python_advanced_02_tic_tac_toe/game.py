"""
Game module.
"""
import logging
from itertools import chain
from utils import get_digit

from table import GameTable
from settings import NUMBERS_MAP, MESSAGE_FORMAT, TIME_FORMAT, LOGFILE, \
    SELECT_NUMBER, WIN_MESSAGE, DRAW_MESSAGE

# logging wins
logging.basicConfig(
    level=logging.INFO,
    filename=LOGFILE,
    format=MESSAGE_FORMAT,
    datefmt=TIME_FORMAT,
)

score = {}
control_score_sum = 0


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
            SELECT_NUMBER.format(player.name)
        )
        self.table_choices.remove(number)
        self.table.change_item(number, player.symbol)
        player.make_choice(number)
        if player.is_player_win():
            message = WIN_MESSAGE.format(player.name)
            logging.info(message)
            raise GameOver(message)
        if not self.table_choices:
            message = DRAW_MESSAGE
            raise GameOver(message)

    def step(self, player) -> bool:
        """
        running game step for player
        :param player: Player
        :return: bool
        """
        try:
            self.play(player)
        except GameOver as game_over:
            print(game_over)
            print(self.table)
            return player.winner


def game_play(player1, player2, is_new_game=False):
    """
    Gameplay with two players.
    :param is_new_game: bool
    :param player1: Player
    :param player2: Player
    :return:
    """
    global score
    global control_score_sum

    if is_new_game:
        # set default score
        score = {player1.name: 0, player2.name: 0}
    else:
        # clearing players choices and winner mark
        player1.clear()
        player2.clear()

        # logging
        if sum(score.values()) > control_score_sum:
            logging.info(score)
            control_score_sum = sum(score.values())

    table = GameTable(NUMBERS_MAP)
    game = Game(table_grid=table, numbers_map=NUMBERS_MAP)

    while True:
        if game.step(player1):
            score[player1.name] += 1
            break

        if game.step(player2):
            score[player2.name] += 1
            break

    # logging
    if not is_new_game and sum(score.values()) > control_score_sum:
        logging.info(score)
        control_score_sum = sum(score.values())
