"""
Game module.
"""
import logging

from app.controller.robot_choice import make_choice
from app.controller.utils import get_digit
from app.model.robot import Robot

from app.model.table import GameTable
from app.view.table_view import TableView
from settings import NUMBERS_MAP, MESSAGE_FORMAT, TIME_FORMAT, LOGFILE, \
    SELECT_NUMBER, WIN_MESSAGE, DRAW_MESSAGE, X_SYMBOL, O_SYMBOL

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

    def __init__(self, numbers_map, player1, player2, win_combinations):
        self.table = GameTable(numbers_map)
        self.players = []
        self.players.append(player1)
        self.players.append(player2)
        self.win_combinations = win_combinations

    def get_choice(self, player):
        if isinstance(player, Robot):
            number = make_choice(self.table.variants)
        else:
            number = get_digit(
                self.table.variants,
                SELECT_NUMBER.format(player.name)
            )
        return number

    def is_player_win(self, choices: set) -> bool:
        """
        check is player win
        :return: bool
        """
        result = False
        if len(choices) >= 3:
            for item in self.win_combinations:
                if item <= choices:
                    result = True
        return result

    def play_step(self, player):
        """
        play step for player
        :param player: Player
        :return:
        """
        table_view = TableView(
            numbers_map=NUMBERS_MAP,
            x_symbol=X_SYMBOL,
            o_symbol=O_SYMBOL,
            **self.table.choices)
        print(table_view)
        number = self.get_choice(player)
        self.table.variants.remove(number)

        if player.symbol == X_SYMBOL:
            player_choices = self.table.x_choices
        else:
            player_choices = self.table.o_choices

        player_choices.add(number)

        result = {}
        if self.is_player_win(player_choices):
            message = WIN_MESSAGE.format(player.name)
            logging.info(message)
            result = {'message': message, 'status': 1, 'winner': player.name}
        if not self.table.variants:
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
                table_view = TableView(
                    numbers_map=NUMBERS_MAP,
                    x_symbol=X_SYMBOL,
                    o_symbol=O_SYMBOL,
                    **self.table.choices)
                print(table_view)
                break
        return request


def run_game(player1, player2, win_combinations, is_new_game=False):
    """
    Gameplay with two players.
    :param win_combinations: list
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

        # logging
        if sum(score.values()) > control_score_sum:
            logging.info(score)
            control_score_sum = sum(score.values())

    game = Game(
        numbers_map=NUMBERS_MAP,
        player1=player1,
        player2=player2,
        win_combinations=win_combinations
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
