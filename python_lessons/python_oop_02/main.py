"""
Main restrain module
"""
from abc import ABC
from random import choice
from datetime import datetime as dt

from prettytable import PrettyTable
from settings import MAX_ORDER_ITEM_COUNT, COUNT_REQUEST, \
    DEFAULT_TABLES_COUNT, WAITERS, MENU_FILE, ORDER_STATUSES
from utils import get_customer_name, get_digit, get_money
from menu import Menu, Dish


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

    def __str__(self):
        return self.name


class Customer(Person):
    """
    Class customer with pay, eat, and waiter speaking options.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = self._catering.tables.pop()
        self._check_list = list()

    def to_pay(self, order):
        """
        send money to another person bill
        :param order: Order
        :return: None
        """
        money = get_money(order.total)
        print(f'{self.name} give ${money}')
        self._bill -= money
        print(f'{self.name} bill status ${self._bill}')
        order.waiter.get_payment(money, self)

    def release_table(self):
        """
        return table to free catering table list
        :return:
        """
        self._catering.tables.append(self.table)
        print(f'{self}: "Goodbye {self._catering}"')

    def see_menu(self):
        """
        see the menu
        :return:
        """
        print(self._catering.menu)

    def call_waiter(self):
        """
        call waiter and start ordering
        :return:
        """
        print(f'{self.name} call waiter')
        waiter = choice(self._catering.waiters_pool)
        waiter.get_order(self)

    def set_check_list(self, check_list: list):
        """ add order items to check list """
        self._check_list = check_list

    def _check_order(self, order):
        """ compare order items with check list """
        return order.items == self._check_list

    def _eat(self, order):
        """ eating dishes """
        for item in order.items:
            print(f"{self.name} eat {item}")
        order.change_status()

    def get_bill(self, order):
        """ ask waiter for a bill """
        print(f'{self.name}: "Give me a bill, please."')
        print(order.waiter.give_bill(order))

    def get_dishes(self, order):
        """
        get dishes, check order with check list, eat and pay
        :param order: Order
        :return:
        """
        if self._check_order(order):
            order.change_status()
            self._eat(order)
            self.get_bill(order)
            self.to_pay(order)

    def __str__(self):
        return self.name


class Waiter(Person):
    """
    Waiter class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._orders_dict = dict()

    def _get_choices(self, order):
        """
        getting choices of dishes
        :param order: Order
        :return: Order
        """
        print(f"Hello, I'm {self.name}. What would you like to eat?")
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

    def get_order(self, this_customer):
        """
        Getting order
        :param this_customer: Customer
        :return:
        """
        order = Order(waiter=self, customer=this_customer)
        while True:
            order = self._get_choices(order)
            print('your order:')
            table = PrettyTable()
            table.field_names = ['Order']
            for item in order.items:
                table.add_row([str(item)])
            print(str(table))

            if get_digit(1, 'Enter 1 to confirm or 0 to cancel: '):
                self._orders_dict[this_customer.table] = order
                this_customer.set_check_list(order.items)
                order.change_status()
                break
            order.items.clear()
        order.change_status()
        self._catering.get_order(order)

    def carry_order(self, order):
        """ carry order to customer """
        print(f"{self.name}: 'Bon Appetit!'")
        order.customer.get_dishes(order)

    @staticmethod
    def _take_tip(money, order):
        """ taking a tip """
        return money - order.total

    @staticmethod
    def give_bill(order) -> str:
        """
        Give bill from order
        :param order: Order
        :return: str
        """
        result = f'Waiter: {order.waiter}  Date: {order.date}\n'
        table = PrettyTable()
        table.field_names = ['Name', 'Count', "Price"]
        for item in order.items:
            table.add_row([item.dish.name, item.quantity, item.item_total])
        result += str(table) + f'\n Total: {order.total}'
        return result

    def to_pay(self, money):
        """
        send money to another person bill
        :param money: float
        :return: None
        """
        self._catering.get_payment(money, self)

    def get_payment(self, money: float, from_person: Customer):
        """
        get money to catering bill and get tips
        :param from_person: Customer
        :param money: float
        :return: None
        """
        order = self._orders_dict.get(from_person.table)
        print(f'{self} received ${money} from {from_person}')

        # taking a tip if it possible
        tip = self._take_tip(money, order)
        if tip:
            self._bill += tip
            money -= tip

        order.change_status()
        self.to_pay(money)

    def __str__(self):
        return self.name


class Order:
    """
    order class
    """

    def __init__(self, **kwargs):
        self.customer: Customer = kwargs.get('customer')
        self.waiter: Waiter = kwargs.get('waiter')
        self.date = dt.now().date()
        self.items = list()
        self.status = 0

    def add_dish(self, dish, quantity=1):
        """ add dish to order """
        self.items.append(OrderItem(dish, quantity))

    @property
    def total(self) -> float:
        """
        total order price
        :return: float
        """
        return sum(item.item_total for item in self.items)

    def change_status(self):
        """
        change order status
        :return:
        """
        print(ORDER_STATUSES[self.status])
        self.status += 1

    def __str__(self):
        result = f'Waiter: {self.waiter}  Date: {self.date}\n'
        table = PrettyTable()
        table.field_names = ['Name', 'Count']
        for dish in self.items:
            table.add_row([dish.name, dish.count])
        result += str(table) + f' {self.status}'
        return result


class OrderItem:
    """
    Order item class
    """

    def __init__(self, dish, quantity=1):
        self.dish: Dish = dish
        self.quantity: int = quantity

    @property
    def item_total(self) -> float:
        """
        total item prise
        :return: float
        """
        return self.dish.price * self.quantity

    def __str__(self):
        return f'{self.dish.name} - {self.quantity}pcs'


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

    def __str__(self):
        return f"Best Catering with {len(self.tables)} free tables"


if __name__ == "__main__":
    menu = Menu()
    menu.load_items(MENU_FILE)
    catering = Catering(menu=menu)
    customer = Customer(name=get_customer_name(), catering=catering, bill=1000)
    customer.call_waiter()
    customer.release_table()
