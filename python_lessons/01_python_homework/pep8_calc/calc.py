"""

implementation of the arithmetic calculator

"""
from functools import reduce


class Calc:
    """

    contains a method for casting arguments to float type
    and methods of four arithmetic operations

    """

    @staticmethod
    def cleaned_numbers(*args) -> tuple:
        """
        a method for casting arguments to float type

        :param args: all passed parameters must contain a number
                     as a string containing a number, int, float or other
                     numeric types

        :return: tuple of float elements
        """
        return tuple(float(n) for n in args)

    def addition(self, *args) -> float:
        """
        method for adding arguments
        :param args: tuple of float elements, all parameter must be float
        :return: float sum of parameters
        """
        return sum(self.cleaned_numbers(*args))

    def multiplication(self, *args) -> float:
        """
        method for multiply arguments
        :param args: tuple of float elements, all parameter must be float
        :return: float multiplication of parameters
        """
        return reduce(lambda x, y: x * y, self.cleaned_numbers(*args))

    def division(self, dividend, divisor) -> float:
        """
        method for divide dividend on divisor
        :param dividend: a string containing a number, int, float or other
                         numeric types
        :param divisor: a string containing a number, int, float or other
                        numeric types
        :return: float
        """
        dividend, divisor = self.cleaned_numbers(dividend, divisor)
        return dividend / divisor

    def subtraction(self, whole, particular) -> float:
        """
        method for subtract particular from whole
        :param whole: a string containing a number, int, float or other
                      numeric types
        :param particular: a string containing a number, int, float or other
                           numeric types
        :return: float
        """
        whole, particular = self.cleaned_numbers(whole, particular)
        return whole - particular


if __name__ == "__main__":
    calculator = Calc()

    print(calculator.multiplication(42, 3.14, '6.626'))
