"""

Factorial function
n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1

"""


def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))
