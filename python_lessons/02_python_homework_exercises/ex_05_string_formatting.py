"""

Exercise: learnpython.org/en/String_Formatting

    You will need to write a format string which prints out the data
    using the following syntax:
        Hello John Doe. Your current balance is $53.44.

"""

FORMAT_STRING = "Hello %s %s. Your current balance is $%.2f."
data = ("John", "Doe", 53.44)

if __name__ == "__main__":
    print(FORMAT_STRING % data)
