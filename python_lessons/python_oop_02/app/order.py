"""
Order and Order Item
"""
from .menu import Dish
from .users import Customer, Waiter
from datetime import datetime as dt


class Order:
    """

    """

    def __init__(self, **kwargs):
        self.customer: Customer = kwargs.get('customer')
        self.waiter: Waiter = kwargs.get('waiter')
        self.date = dt.now().date()
        self.items = list()
        self.status = 0

    def add_dish(self, dish, quantity=1):
        self.items.append(OrderItem(dish, quantity))

    @property
    def total(self) -> float:
        return sum(item.item_total for item in self.items)

    def change_status(self):
        self.status += 1


class OrderItem:
    def __init__(self, dish, quantity=1):
        self.dish: Dish = dish
        self.quantity: int = quantity

    @property
    def item_total(self) -> float:
        return self.dish.price * self.quantity
