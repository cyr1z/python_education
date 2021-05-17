"""
Console play main module
"""
from app.controller.game import game_play
from app.view.menu import Menu
from app.model.player import get_new_users
from app.controller.utils import read_log
from app.model.win import Win
from settings import NUMBERS_MAP, START_MENU, END_MENU, ASK_NUMBER, LOGFILE


def play():
    """
    Main function
    :return:
    """

    win = Win(NUMBERS_MAP)
    menu = Menu(START_MENU, ASK_NUMBER)
    end_menu = Menu(END_MENU, ASK_NUMBER)

    while True:
        # start menu
        int_choice = menu.get_choice()

        if not int_choice:
            break

        if int_choice == 1:
            users = get_new_users(win.combinations)
            game_play(users[0], users[1], is_new_game=True)

            while True:
                # end menu
                int_choice = end_menu.get_choice()

                if not int_choice:
                    break

                if int_choice == 1:
                    users = get_new_users(win.combinations)
                    game_play(users[0], users[1], is_new_game=True)

                if int_choice == 2:
                    print(read_log(LOGFILE))

                if int_choice == 3:
                    game_play(users[0], users[1])

        if int_choice == 2:
            print(read_log(LOGFILE))