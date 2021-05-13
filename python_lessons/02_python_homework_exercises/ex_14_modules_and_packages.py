"""

Exercise: https://www.learnpython.org/en/Modules_and_Packages

    In this exercise, you will need to print an alphabetically
    sorted list of all functions in the re module, which contain the word find.

"""
import re

SUBSTRINGS = 'find'

if __name__ == "__main__":
    print(sorted([member for member in dir(re) if SUBSTRINGS in member]))
