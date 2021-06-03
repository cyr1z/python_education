from functools import partial
from tkinter import Button, Frame, Label, Tk

from app.model.robot import Robot
from settings import SIZE

root = Tk()

root.title('Tic Tac Toe')
panel_frame = Frame(root, height=60)
board_frame = Frame(root, height=100)
board_frame.config(width=SIZE * 3, height=SIZE * 3)
status_frame = Frame(root, height=60)
status = Label(status_frame)
panel_frame.pack(side='top', fill='x')
status_frame.pack(side="top", fill='x')
board_frame.pack(side='bottom', fill='both', expand=1)


def change_to_x(number, buttons):
    """change symbol on button and make it disabled"""
    buttons[number - 1]['text'] = 'X'
    buttons[number - 1]["state"] = "disabled"


def change_to_o(number, buttons):
    """change symbol on button and make it disabled"""
    buttons[number - 1]['text'] = '0'
    buttons[number - 1]["state"] = "disabled"


def quit_game(root):
    """ quit game """
    root.destroy()


def set_status(text=''):
    status['text'] = text
    status.pack()


def game_over(message, buttons):
    set_status(message)
    for button in buttons:
        button["state"] = "disabled"


def make_move(number, table, buttons, player1, player2):
    """make user and robot move"""
    if not table.is_maximize_player:
        player = player1
        change_to_x(number, buttons)
    else:
        player = player2
        change_to_o(number, buttons)
    request = table.choice_handler(number, player)
    if request:
        game_over(request['message'], buttons)
    elif table.is_maximize_player and isinstance(player2, Robot):
        # robot move
        number = player2.get_choice(table)
        make_move(number, table, buttons, player1, player2)


def make_board(buttons, table, player1, player2):
    # make play board buttons
    counter = 1

    for i in range(0, 3):
        for j in range(0, 3):
            buttons.append(
                Button(
                    board_frame,
                    text=counter,
                    command=partial(make_move, counter, table, buttons,
                                    player1, player2)
                )
            )
            buttons[counter - 1].place(
                x=SIZE * j, y=SIZE * i, width=SIZE, height=SIZE
            )
            counter += 1

    set_status('play game')


def make_buttons(play):
    # new game and quit buttons
    new_game_button = Button(panel_frame, text='New Game',
                             command=partial(play))
    new_game_button.place(x=5, y=10, width=90, height=30)
    quit_button = Button(panel_frame, text='Quit',
                         command=partial(quit_game, root))
    quit_button.place(x=160, y=10, width=80, height=30)
