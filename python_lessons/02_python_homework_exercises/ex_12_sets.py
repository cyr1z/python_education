"""
Exercise: https://www.learnpython.org/en/Sets

    In the exercise below, use the given lists to print out a set
    containing all the participants from event A which did not attend event B.

"""

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

if __name__ == "__main__":

    a, b = set(a), set(b)

    # print(a.difference(b))
    print(a - b)
