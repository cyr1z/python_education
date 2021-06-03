""" Tkinter gui for minimax tic-tac-toe """

from app.model.player import Player
from app.model.robot import Robot
from app.model.table import GameTable
from settings import NUMBERS_MAP, X_SYMBOL, O_SYMBOL

# game window and frames
from app.view.gui_view import make_board, root, make_buttons, get_name, \
    get_two_names


def play(with_robot=False):
    """ main play """

    if with_robot:
        name1 = get_name()
        player2 = Robot(X_SYMBOL)
    else:
        name1, name2 = get_two_names()
        player2 = Player(name2, X_SYMBOL)
    player1 = Player(name1, O_SYMBOL)

    table = GameTable(NUMBERS_MAP)
    buttons = []
    make_board(buttons, table, player1, player2)
    root.mainloop()


if __name__ == "__main__":
    make_buttons(play)
    play()
