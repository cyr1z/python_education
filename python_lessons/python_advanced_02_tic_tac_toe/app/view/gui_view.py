from functools import partial
from tkinter import Button, Frame, Label, Tk, simpledialog as sd

from app.controller.get_robot_move import get_robot_move
from app.model.robot import Robot
from settings import SIZE

root = Tk()

root.title('Tic Tac Toe')
panel_frame = Frame(root, height=80)
board_frame = Frame(root, height=100)
board_frame.config(width=SIZE * 3, height=SIZE * 3)
status_frame = Frame(root, height=60)
status = Label(status_frame)
panel_frame.pack(side='top', fill='x')
status_frame.pack(side="top", fill='x')
board_frame.pack(side='bottom', fill='both', expand=1)


def change_to_symbol(number, buttons, symbol):
    """change symbol on button and make it disabled"""
    buttons[number - 1]['text'] = symbol
    buttons[number - 1]["state"] = "disabled"


def quit_game(ev):
    """ quit game """
    root.destroy()


def set_status(text=''):
    """put message to statusbar"""
    status['text'] = text
    status.pack()


def game_over(message, buttons):
    """end game - set message and block buttons"""
    set_status(message)
    for button in buttons:
        button["state"] = "disabled"


def make_move(number, table, buttons, player1, player2):
    """make user and robot move"""
    if not table.is_maximize_player:
        player = player1
        change_to_symbol(number, buttons, 'X')
    else:
        player = player2
        change_to_symbol(number, buttons, '0')
    request = table.choice_handler(number, player)
    if request:
        game_over(request['message'], buttons)
    elif table.is_maximize_player and isinstance(player2, Robot):
        # robot move
        number = get_robot_move(player2, table)
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


def get_name():
    """ get player name for player vs robot game. """
    result = sd.askstring("Name", "What is your name?", parent=root)
    if result is None:
        result = 'You'
    return result


def get_two_names():
    """ get two names for player vs player game. """
    name1 = sd.askstring("Input", "What's Player 1 name?", parent=root)
    name2 = sd.askstring("Input", "What's Player 2 name?", parent=root)
    if name1 is None:
        name1 = 'Player 1'
    if name2 is None:
        name2 = 'Player 2'
    return name1, name2


def make_buttons(play):
    """ new game and quit buttons"""
    # new game button
    new_game_button = Button(panel_frame, text='New Game',
                             command=partial(play))
    new_game_button.place(x=5, y=10, width=90, height=30)

    # new game with robot button
    new_robot_game_button = Button(panel_frame, text='New Game with robot',
                                   command=partial(play, True))
    new_robot_game_button.place(x=95, y=10, width=145, height=30)

    # quit button
    quit_button = Button(panel_frame, text='Quit',
                         command=partial(quit_game, False))
    quit_button.place(x=160, y=45, width=80, height=30)
