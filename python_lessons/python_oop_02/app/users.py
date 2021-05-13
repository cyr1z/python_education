"""
 persons objects - Waiters and Customers
"""
from abc import ABC, abstractmethod

from .catering import Catering
from random import choice
from .order import Order
from .settings import COUNT_REQUEST, MAX_ORDER_ITEM_COUNT
from .utils import get_digit


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

    def get_payment(self, money: float, from_person):
        print('Keep the change')

    def _release_table(self):
        """
        return table to free catering table list
        :return:
        """
        self._catering.tables.append(self.table)

    def see_menu(self):
        """
        see the menu
        :return:
        """
        print(self._catering.menu)

    def call_water(self):
        """
        call waiter and start ordering
        :return:
        """
        waiter = choice(self._catering.waiters_pool)
        waiter.get_order(self)


class Waiter(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._orders_dict = dict()

    def get_choices(self, order):
        print('Hello, What would you like to eat?')
        while True:
            print(self._catering.menu)
            print('enter "0" for end ordering')
            dish_number = get_digit(len(self._catering.menu.items))
            if not dish_number:
                break
            dish = self._catering.menu.items[dish_number]
            quantity = get_digit(MAX_ORDER_ITEM_COUNT, COUNT_REQUEST)
            if not quantity:
                quantity = 1
            order.add_dish(dish, quantity)
        return order

    def get_order(self, customer):
        order = Order(waiter=self, customer=customer)
        while True:
            order = self.get_choices(order)
            print('your order:')
            print('/n'.join(str(_) for _ in order.items))

            if get_digit(1, 'Enter 1 to confirm or 0 to cancel'):
                self._orders_dict[customer.table] = order
                self._catering.get_order(order)
                break
            else:
                order.items.clear()

    def carry_order(self, order):
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
