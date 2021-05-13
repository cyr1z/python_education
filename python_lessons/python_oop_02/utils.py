"""
simple utils
"""
from settings import NUMBER_REQUEST, MONEY_REQUEST


def get_digit(items_count: int, welcome_string=NUMBER_REQUEST) -> int:
    """get digit from user input"""
    while True:
        line = input(welcome_string)
        if not line.isdigit():
            print("not digit")
            continue
        line = int(line)
        if not 0 <= line <= items_count:
            print("not in range")
            continue
        break
    return line


def get_money(total_price, welcome_string=MONEY_REQUEST) -> float:
    """get digit from user input"""
    while True:
        line = input(welcome_string)
        try:
            line = float(line)
        except ValueError:
            print("not digit")
            continue
        if line < total_price:
            print("This is not enough")
            continue
        break
    return line


def get_customer_name() -> str:
    return input("What is your name: ")
