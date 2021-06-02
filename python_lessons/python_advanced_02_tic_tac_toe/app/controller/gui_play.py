""" Tkinter gui for minimax tic-tac-toe """

from functools import partial
from tkinter import Tk, Frame, Button, Label
from app.model.player import Player
from app.model.robot import Robot
from app.model.table import GameTable
from settings import NUMBERS_MAP, X_SYMBOL, O_SYMBOL

# game window and frames
root = Tk()
root.title('Tic Tac Toe')
SIZE = 80
panel_frame = Frame(root, height=60)
board_frame = Frame(root, height=100)
board_frame.config(width=SIZE * 3, height=SIZE * 3)
status_frame = Frame(root, height=60)
status = Label(status_frame)
panel_frame.pack(side='top', fill='x')
status_frame.pack(side="top", fill='x')
board_frame.pack(side='bottom', fill='both', expand=1)


def play():
    """ main play """
    table = GameTable(NUMBERS_MAP)
    player2 = Robot(X_SYMBOL)
    player1 = Player('Player', O_SYMBOL)
    buttons = []
    counter = 1
    status['text'] = 'PLAY GAME'
    status.pack()

    def change_to_x(number):
        """change symbol on button and make it disabled"""
        buttons[number - 1]['text'] = 'X'
        buttons[number - 1]["state"] = "disabled"

    def change_to_o(number):
        """change symbol on button and make it disabled"""
        buttons[number - 1]['text'] = '0'
        buttons[number - 1]["state"] = "disabled"

    def make_move(number):
        """make user and robot move"""
        if not table.is_maximize_player:
            change_to_x(number)
            player = player1
        else:
            change_to_o(number)
            player = player2

        request = table.choice_handler(number, player)
        if request:
            status['text'] = request['message']
            status.pack()
            for button in buttons:
                button["state"] = "disabled"
        elif table.is_maximize_player:
            # robot move
            make_move(player2.get_choice(table))

    # make play board buttons
    for i in range(0, 3):
        for j in range(0, 3):
            buttons.append(
                Button(
                    board_frame,
                    text=counter,
                    command=partial(make_move, counter)
                )
            )
            buttons[counter - 1].place(
                x=SIZE * j, y=SIZE * i, width=SIZE, height=SIZE
            )
            counter += 1

    root.mainloop()


def quit_game(ev):
    """ quit game """
    global root
    root.destroy()


# new game and quit buttons
new_game_button = Button(panel_frame, text='New Game', command=partial(play))
new_game_button.place(x=5, y=10, width=90, height=30)
quit_button = Button(panel_frame, text='Quit')
quit_button.place(x=160, y=10, width=80, height=30)
quit_button.bind("<Button-1>", quit_game)

if __name__ == "__main__":
    play()
