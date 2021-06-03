"""
tic-tac-toe settings

"""
ASK_NUMBER = "Enter a number: "
NUMBERS_MAP = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
X_SYMBOL = '\033[91m\033[1mX\033[0m\033[22m'
O_SYMBOL = '\033[92m\033[1m0\033[0m\033[22m'
START_MENU = [
    [0, 'Exit'],
    [1, 'New Game with Player'],
    [2, 'View log'],
    [3, 'New Game with Robot']
]
END_MENU = [
    [0, 'Exit'],
    [1, 'New Game'],
    [2, 'View log'],
    [3, 'Replay'],
]
TIME_FORMAT = "%d-%m-%Y %H:%M"
MESSAGE_FORMAT = "%(asctime)s  %(message)s"
LOGFILE = 'win.log'
SELECT_NUMBER = "{}, select number: "
WIN_MESSAGE = "   {} WIN!!!"
DRAW_MESSAGE = "   DRAW"
MENU_WELCOME = 'Select one: \n'
PLAYER_ONE_CREATE = "== Player 1 =="
PLAYER_TWO_CREATE = "== Player 2 =="
NO_LOG_MESSAGE = 'empty log'
ROBOT_NAME = 'Robot'
SIZE = 80
