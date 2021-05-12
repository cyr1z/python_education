import yaml
from prettytable import PrettyTable


class Menu:
    def __init__(self):
        self.items = dict()

    def load_items(self, file):
        with open(file) as file:
            menu_dict = yaml.load(file, Loader=yaml.FullLoader).get('menu')
            for key, item in menu_dict.items():
                self.items[key] = Dish(
                    item.get('name'),
                    float(item.get('price'))
                )

    def __str__(self):
        table = PrettyTable()
        table.field_names = ['#', 'Name', 'Price']
        for key, dish in self.items.items():
            table.add_row([key, dish.name, dish.price])
        return str(table)


class Dish:
    def __init__(self, name, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}  -   ${self.price}'
