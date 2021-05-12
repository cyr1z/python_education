"""
 persons objects - Waiters and Customers
"""
from abc import ABC, abstractmethod

from .catering import Catering
from .order import Order


class Person(ABC):
    """
    Basic person class with bill
    bill_status: - check bill
    """

    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name')
        self._bill: float = kwargs.get('bill') if kwargs.get('bill') else 0
        self._catering: Catering = kwargs.get('catering')

    @property
    def bill_status(self) -> float:
        """
        returns bill status
        :return: float
        """
        return float(self._bill)

    @abstractmethod
    def to_pay(self, other_object, money):
        """
        send money to another person bill
        :param other_object: Person or Catering Object
        :param money: float
        :return: None
        """
        raise NotImplementedError("pay method not implemented!")

    @abstractmethod
    def get_payment(self, money: float, from_person):
        """
        get money to bill
        :param from_person: Person
        :param money: float
        :return: None
        """
        raise NotImplementedError("get payment method not implemented!")


class Customer(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = self._catering.tables.pop()

    def to_pay(self, other_object, money):
        """
        send money to another person bill
        :param other_object: Person or Catering Object
        :param money: float
        :return: None
        """
        self._bill -= money
        other_object.get_payment(money, self)

    def _release_table(self):
        self._catering.tables.append(self.table)


class Waiter(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.in_progress = None
        self._orders_dict = dict()


    @property
    def is_free(self):
        return not bool(self.in_progress)

    def get_order(self):
        pass

    def carry_order(self):
        pass

    def _approve_payment(self):
        pass

    def _take_tip(self, money, order):
        pass

    def to_pay(self, other_object, money):
        """
        send money to another person bill
        :param other_object: Person or Catering Object
        :param money: float
        :return: None
        """
        other_object.get_payment(money, self)

    def get_payment(self, money: float, from_person: Customer):
        """
        get money to bill
        :param from_person: Customer
        :param money: float
        :return: None
        """
        order = self._orders_dict.get(from_person.table)
        self._bill += self._take_tip(money, order)
        money -= self._take_tip(money, order)
        print(f'{self} received ${money} from {from_person}')
