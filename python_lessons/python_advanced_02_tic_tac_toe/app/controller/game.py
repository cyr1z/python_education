"""
Game module.
"""
import logging
from itertools import chain

from app.controller.utils import get_digit
from app.model.robot import Robot, make_choice

from app.view.table import GameTable
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


class Game:
    """
    Game play class
    """

    def __init__(self, numbers_map, player1, player2):
        self.table = GameTable(numbers_map)
        self.table_choices = list(chain(*numbers_map))
        self.players = []
        self.players.append(player1)
        self.players.append(player2)

    def get_choice(self, player):
        if isinstance(player, Robot):
            number = make_choice(self.table_choices)
        else:
            number = get_digit(
                self.table_choices,
                SELECT_NUMBER.format(player.name)
            )
        return number

    def play_step(self, player):
        """
        play step for player
        :param player: Player
        :return:
        """
        print(self.table)
        number = self.get_choice(player)
        self.table_choices.remove(number)
        self.table.change_item(number, player.symbol)
        # TODO: move choice tables to Game object from players
        player.make_choice(number)

        result = {}
        if player.is_player_win():
            message = WIN_MESSAGE.format(player.name)
            logging.info(message)
            result = {'message': message, 'status': 1, 'winner': player.name}
        if not self.table_choices:
            message = DRAW_MESSAGE
            result = {'message': message, 'status': 0, 'winner': None}
        return result

    def iteration(self) -> dict:
        """
        running game step for player
        :return: bool
        """
        request = {}
        for player in self.players:
            request = self.play_step(player)
            if request:
                print(self.table)
                break
        return request


def run_game(player1, player2, is_new_game=False):
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

    game = Game(
        numbers_map=NUMBERS_MAP,
        player1=player1,
        player2=player2,
    )

    while True:
        request = game.iteration()
        if request:
            print(request.get('message'))
            if request.get('status'):
                score[request.get('winner')] += 1
            break

    # logging
    if not is_new_game and sum(score.values()) > control_score_sum:
        logging.info(score)
        control_score_sum = sum(score.values())
