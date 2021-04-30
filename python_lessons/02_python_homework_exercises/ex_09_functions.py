"""

Exercise: https://www.learnpython.org/en/Functions

    In this exercise you'll use an existing function, and while adding
    your own to create a fully functional program.

    Add a function named list_benefits() that returns the following
    list of strings:

        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"

    Add a function named build_sentence(info) which receives a single
    argument containing a string and returns a sentence starting with
    the given string and ending with the string " is a benefit of functions!"

    Run and see all the functions work together!

"""

LIST_OF_STRINGS = [
    "More organized code",
    "More readable code",
    "Easier code reuse",
    "Allowing programmers to share and connect code together"
]
END_OF_STRING = " is a benefit of functions!"


def list_benefits() -> list:
    """
    return a list of strings
    :return: list of strings
    """
    return LIST_OF_STRINGS


def build_sentence(benefit: str) -> str:
    """
    this function concatenate to each benefit - " is a benefit of functions!"
    :benefit: string
    :return: string
    """
    return benefit + END_OF_STRING


def name_the_benefits_of_functions():
    """
    print all benefits from LIST_OF_STRINGS
    """
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


if __name__ == "__main__":
    name_the_benefits_of_functions()
