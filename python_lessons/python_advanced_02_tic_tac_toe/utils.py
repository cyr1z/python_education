"""
simple utils
"""


def get_digit(choices: list, welcome_string) -> int:
    """
    get digit from user input
    :param choices: lst
    :param welcome_string: str
    :return: int
    """
    while True:
        line = input(welcome_string)
        try:
            line = int(line)
        except ValueError:
            print("not digit")
            continue
        if line not in choices:
            print("not in choices")
            continue
        break
    return line


def get_player_name(wromg_name='') -> str:
    """
    det name string
    :return: str
    """
    while True:
        name = input("What is your name: ")
        if name == wromg_name:
            print("the name already taken.")
        else:
            break
    return name


def read_log(filename):
    """
    read log file
    :param filename: str
    :return: str
    """
    # TODO: rewrite file reading
    with open(filename, 'r') as file:
        line = file.read()
    return line
