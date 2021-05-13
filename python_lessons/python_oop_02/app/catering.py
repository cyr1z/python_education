"""
Catering class

"""

from .menu import Menu
from .order import Order
from .settings import DEFAULT_TABLES_COUNT, WAITERS
from .users import Waiter


class Catering:
    """
    Catering class
    """

    def __init__(self, **kwargs):
        self._bill: float = kwargs.get('bill') if kwargs.get('bill') else 0
        if kwargs.get('tables_count'):
            tables_count: int = int(kwargs.get('tables_count'))
        else:
            tables_count: int = DEFAULT_TABLES_COUNT
        self.tables = [_ for _ in range(1, tables_count + 1)]
        self.waiters_pool = [Waiter(name=n, catering=self) for n in WAITERS]
        self.menu: Menu = kwargs.get('menu')

    def get_payment(self, money: float, from_person: Waiter):
        """
        get money to bill
        :param from_person: Waiter
        :param money: float
        :return: None
        """
        self._bill += money
        print(f'{self} received ${money} from {from_person}')

    @property
    def bill_status(self) -> float:
        """
        returns bill status
        :return: float
        """
        return float(self._bill)

    def get_order(self, order: Order):
        """
        Getting order to catering
        :param order: Order
        :return:
        """
        if order.status:
            self._make_food(order)
            order.change_status()

    @staticmethod
    def give_order(order):
        """
        give ready dishes to waiter
        :param order: Order
        :return:
        """
        print('Order dishes are ready')
        order.change_status()
        order.waiter.carry_order(order)

    def _make_food(self, order: Order):
        """
        make food for order
        :param order: Order
        :return:
        """
        for item in order.items:
            print(item.dish.name, 'making')
        order.change_status()
        self.give_order(order)
