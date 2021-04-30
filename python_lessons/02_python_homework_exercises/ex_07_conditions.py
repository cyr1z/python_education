"""

Exercise: https://www.learnpython.org/en/Conditions

    Change the variables in the first section, so that each
    if statement resolves as True.

"""
# change this code
NUMBER = 16
SECOND_NUMBER = 0
FIRST_ARRAY = [1, 2, 5]
SECOND_ARRAY = [1, 2]

if __name__ == "__main__":

    if NUMBER > 15:
        print("1")

    if FIRST_ARRAY:
        print("2")

    if len(SECOND_ARRAY) == 2:
        print("3")

    if len(FIRST_ARRAY) + len(SECOND_ARRAY) == 5:
        print("4")

    if FIRST_ARRAY and FIRST_ARRAY[0] == 1:
        print("5")

    if not SECOND_NUMBER:
        print("6")
