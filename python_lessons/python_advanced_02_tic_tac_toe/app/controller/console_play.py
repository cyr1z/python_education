"""
Console play main module
"""
from app.controller.game import run_game
from app.model.robot import get_user_and_robot
from app.view.menu_view import Menu
from app.model.player import get_new_users
from app.controller.utils import read_log, get_digit
from app.model.win import Win
from settings import NUMBERS_MAP, START_MENU, END_MENU, ASK_NUMBER, LOGFILE


def main():
    """
    Main function
    :return:
    """

    win = Win(NUMBERS_MAP)
    menu = Menu(START_MENU)
    end_menu = Menu(END_MENU)

    while True:
        # start menu
        print(menu)
        int_choice = get_digit(menu.numbers, ASK_NUMBER)

        if not int_choice:
            break

        if int_choice == 2:
            print(read_log(LOGFILE))

        if int_choice == 1:
            users = get_new_users()

        if int_choice == 3:
            users = get_user_and_robot()

        run_game(
            users[0],
            users[1],
            win.combinations,
            is_new_game=True
        )

        while True:
            # end menu
            print(end_menu)
            int_choice = get_digit(end_menu.numbers, ASK_NUMBER)

            if not int_choice:
                break

            if int_choice == 1:
                users = get_new_users()
                run_game(
                    users[0],
                    users[1],
                    win.combinations,
                    is_new_game=True
                )

            if int_choice == 2:
                print(read_log(LOGFILE))

            if int_choice == 3:
                run_game(users[0], users[1], win.combinations)
