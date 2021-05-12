from .users import Waiter


class Catering:
    def __init__(self, **kwargs):
        self._bill: float = kwargs.get('bill') if kwargs.get('bill') else 0
        if kwargs.get('tables_count'):
            tables_count: int = int(kwargs.get('tables_count'))
        else:
            tables_count: int = 10
        self.tables = [_ for _ in range(1, tables_count + 1)]
        self.orders_pool = list()
        self.waiters_pool = list()

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

    def _make_food(self, order):
        for item in order:
            print(item.dish.name, 'making')
        order.change_status()
