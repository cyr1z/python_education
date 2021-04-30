"""

Exercise: https://www.learnpython.org/en/Variables_and_Types

    The target of this exercise is to create a string, an integer, and a
    floating point number. The string should be named mystring and should
    contain the word "hello". The floating point number should be named
    myfloat and should contain the number 10.0, and the integer should be
    named myint and should contain the number 20.

"""

# change this code
MYSTRING = "hello"
MYFLOAT = 10.0
MYINT = 20

if __name__ == "__main__":
    # testing code
    if MYSTRING == "hello":
        print("String: %s" % MYSTRING)
    if isinstance(MYFLOAT, float) and MYFLOAT == 10.0:
        print("Float: %f" % MYFLOAT)
    if isinstance(MYINT, int) and MYINT == 20:
        print("Integer: %d" % MYINT)
