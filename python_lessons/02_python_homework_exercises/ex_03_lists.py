"""

Exercise: https://www.learnpython.org/en/Lists

    In this exercise, you will need to add numbers and strings
    to the correct lists using the "append" list method. You must add
    the numbers 1,2, and 3 to the "numbers" list, and the words 'hello'
    and 'world' to the strings variable.

    You will also have to fill in the variable second_name with the
    second name in the names list, using the brackets operator [].
    Note that the index is zero-based, so if you want to access
    the second item in the list, its index will be 1.

"""

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
# the variable second_name with the second name in the names list
SECOND_NAME = names[1]

# add the numbers 1,2, and 3 to the "numbers" list
# using the "append" list method
for i in range(1, 4):
    numbers.append(i)

# add the words 'hello' and 'world' to the strings variable
strings.append("hello")
strings.append("world")

if __name__ == "__main__":
    # this code should write out the filled arrays and the second
    # name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % SECOND_NAME)
