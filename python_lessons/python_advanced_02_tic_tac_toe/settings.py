"""
tic-tac-toe settings

"""
ASK_NUMBER = "Enter a number: "
NUMBERS_MAP = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
X_SYMBOL = '\033[91m\033[1mX\033[0m\033[22m'
O_SYMBOL = '\033[92m\033[1m0\033[0m\033[22m'
START_MENU = [
    [0, 'Exit'],
    [1, 'New Game'],
    [2, 'View log'],
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
