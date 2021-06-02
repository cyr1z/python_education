"""
Console play main module
"""
import logging

from app.model.game import Game
from app.model.robot import get_user_and_robot
from app.view.menu_view import Menu
from app.model.player import get_new_users
from app.model.utils import read_log, get_digit
from app.view.table_view import TableView
from settings import NUMBERS_MAP, START_MENU, END_MENU, ASK_NUMBER, LOGFILE, \
    MESSAGE_FORMAT, TIME_FORMAT

# logging wins
logging.basicConfig(
    level=logging.INFO,
    filename=LOGFILE,
    format=MESSAGE_FORMAT,
    datefmt=TIME_FORMAT,
)

score = {}
control_score_sum = 0


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
            print(TableView(**game.table.choices))
            message = request.get('message')
            logging.info(message)
            print(message)
            if request.get('status'):
                score[request.get('winner')] += 1
            break

    # logging
    if not is_new_game and sum(score.values()) > control_score_sum:
        logging.info(score)
        control_score_sum = sum(score.values())


def main():
    """
    Main function
    :return:
    """

    menu = Menu(START_MENU)
    end_menu = Menu(END_MENU)

    while True:
        # start menu
        print(menu)
        int_choice = get_digit(menu.numbers, ASK_NUMBER)
        users = []
        if not int_choice:
            break

        if int_choice == 2:
            print(read_log(LOGFILE))

        if int_choice == 1:
            users = get_new_users()
            run_game(users[0], users[1], is_new_game=True)

        if int_choice == 3:
            users = get_user_and_robot()
            run_game(users[0], users[1], is_new_game=True)



        while True:
            # end menu
            print(end_menu)
            int_choice = get_digit(end_menu.numbers, ASK_NUMBER)

            if not int_choice:
                break

            if int_choice == 1:
                users = get_new_users()
                run_game(users[0], users[1], is_new_game=True)

            if int_choice == 2:
                print(read_log(LOGFILE))

            if int_choice == 3:
                run_game(users[0], users[1])
