"""
user input functions
"""
from .settings import INPUT_PHRASE


def get_letter() -> str:
    """ get one letter """
    letter = str()
    while len(letter) != 1 or not letter.isalpha():
        letter = input(INPUT_PHRASE)
    return letter
