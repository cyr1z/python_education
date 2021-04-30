"""

Exercise: https://www.learnpython.org/en/Basic_String_Operations

    Try to fix the code to print out the correct information
    by changing the string.

"""

GOOD_STRING = "Strings are awesome!"

if __name__ == "__main__":
    # Length should be 20
    print("Length of s = %d" % len(GOOD_STRING))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % GOOD_STRING.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % GOOD_STRING.count("a"))

    # Slicing the string into bits
    # Start to 5
    print("The first five characters are '%s'" % GOOD_STRING[:5])
    # 5 to 10
    print("The next five characters are '%s'" % GOOD_STRING[5:10])
    # Just number 12
    print("The thirteenth character is '%s'" % GOOD_STRING[12])
    # (0-based indexing)
    print("The characters with odd index are '%s'" % GOOD_STRING[1::2])
    # 5th-from-last to end
    print("The last five characters are '%s'" % GOOD_STRING[-5:])

    # Convert everything to uppercase
    print("String in uppercase: %s" % GOOD_STRING.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % GOOD_STRING.lower())

    # Check how a string starts
    if GOOD_STRING.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if GOOD_STRING.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % GOOD_STRING.split(" "))
