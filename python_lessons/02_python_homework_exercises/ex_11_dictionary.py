"""

Exercise: https://www.learnpython.org/en/Dictionaries

    Add "Jake" to the phonebook with the phone number 938273443,
    and remove Jill from the phonebook.

"""

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

if __name__ == "__main__":
    # add Jake
    phonebook["Jake"] = 938273443
    # remove Jill
    del phonebook["Jill"]

    # testing code
    if "Jake" in phonebook:
        print("Jake is listed in the phonebook.")

    if "Jill" not in phonebook:
        print("Jill is not listed in the phonebook.")
