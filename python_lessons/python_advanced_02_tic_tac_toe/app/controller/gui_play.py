""" Tkinter gui for minimax tic-tac-toe """

from app.model.player import Player
from app.model.robot import Robot
from app.model.table import GameTable
from settings import NUMBERS_MAP, X_SYMBOL, O_SYMBOL

# game window and frames
from app.view.gui_view import make_board, root, make_buttons


def play():
    """ main play """
    table = GameTable(NUMBERS_MAP)
    player2 = Robot(X_SYMBOL)
    player1 = Player('Player', O_SYMBOL)
    buttons = []
    make_board(buttons, table, player1, player2)
    root.mainloop()


if __name__ == "__main__":
    make_buttons(play)
    play()
