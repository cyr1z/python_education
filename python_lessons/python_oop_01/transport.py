"""
Transport classes
"""
from abc import ABC, abstractmethod


class Engine:
    """
    Engine class

    """

    def __init__(self, name, displacement, fuel_type, power):
        self.name = name
        self.fuel_type = fuel_type
        self.power = power
        self.displacement = displacement

    def __str__(self):
        return f"{self.name} Engine {self.displacement}L / " \
               f"fuel: {self.fuel_type} / {self.power}hp "


class Goods:
    def __init__(self, name, weight, count):
        self._weight = weight
        self._count = count
        self.name = name

    @property
    def sum_weight(self):
        return self._weight * self._count

    def __str__(self):
        return f"{self.name} / {self.sum_weight}kg "


class Person:
    def __init__(self, name, ticket_id):
        self.ticket_id = ticket_id
        self.name = name

    def __str__(self):
        return f"{self.name} / {self.ticket_id} "


class Transport(ABC):
    """
    Base transport class
    """

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine
        self._load = []

    @abstractmethod
    def loading(self, something):
        raise NotImplementedError("loading method not implemented!")

    @abstractmethod
    def unloading(self, something):
        raise NotImplementedError("unloading method not implemented!")

    @property
    def on_board(self):
        return '\n     '.join(str(p) for p in self._load)

    def __str__(self):
        return f"{self.name} / {self.engine} "


class Cargo(Transport):
    """
    Cargo transport class
    """

    def __init__(self, name, engine, carrying):
        super().__init__(name, engine)
        self._carrying = carrying

    @property
    def free_carry(self):
        return float(self._carrying) - float(sum(w.sum_weight for w in
                                                 self._load))

    def loading(self, thing):
        if isinstance(thing, Goods) and thing.sum_weight < self.free_carry:
            self._load.append(thing)
            print(f'{thing.name} LOADED')
        else:
            print('loading is not possible')

    def unloading(self, thing):
        self._load.pop(thing)

    def __str__(self):
        return super().__str__() + f"/ {self.free_carry}T free "


class Passenger(Transport):
    """
    Passenger transport class
    """

    def __init__(self, name, engine, passengers: int):
        super().__init__(name, engine)
        self._passengers = passengers

    @property
    def free_seats(self):
        """
        free seats for passengers
        :return: int
        """
        return self._passengers - len(self._load)

    def loading(self, unit: Person):
        """
        load passengers
        :param unit: Person
        :return: list of loaded passengers
        """
        if isinstance(unit, Person) and self.free_seats:
            self._load.append(unit)
            print(f"WELCOME {unit.name}")
        else:
            print('loading is not possible')
        return self._load

    def unloading(self, unit):
        self._load.pop(unit)

    def __str__(self):
        return super().__str__() + f" / {self.free_seats} free seats "


class WaterMixin:
    """
    Mixin for water transport
    """

    def __init__(self, draught):
        self.draught = draught

    def __str__(self):
        return f"/ {self.draught} draught "


class RoadMixin:
    """
    Mixin for road transport
    """

    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return f"/ {self.number_of_wheels} wheels "


class Car(Passenger, RoadMixin):
    """
    passengers car
    """

    def __init__(self, name, engine, passengers, number_of_wheels=4):
        super().__init__(name, engine, passengers)
        RoadMixin.__init__(self, number_of_wheels)

    def __str__(self):
        return super().__str__() + RoadMixin.__str__(self)


class Track(Cargo, RoadMixin):
    """
    Cargo track
    """

    def __init__(self, name, engine, carrying, number_of_wheels=4):
        super().__init__(name, engine, carrying)
        RoadMixin.__init__(self, number_of_wheels)

    def __str__(self):
        return super().__str__() + RoadMixin.__str__(self)


class Boat(Passenger, WaterMixin):
    """
    passengers boat
    """

    def __init__(self, name, engine, passengers, draught):
        super().__init__(name, engine, passengers)
        WaterMixin.__init__(self, draught)

    def __str__(self):
        return super().__str__() + WaterMixin.__str__(self)


class Amphibian(Passenger, RoadMixin, WaterMixin):
    """
    Amphibian transport
    """

    def __init__(self, name, engine, passengers, draught, number_of_wheels):
        super().__init__(name, engine, passengers)
        WaterMixin.__init__(self, draught)
        RoadMixin.__init__(self, number_of_wheels)

    def __str__(self):
        return super().__str__() + WaterMixin.__str__(self) + \
               RoadMixin.__str__(self)


if __name__ == "__main__":
    best_diesel_engine = Engine(
        name='Chrysler EcoDiesel',
        displacement=3.0,
        power=240,
        fuel_type='Diesel'
    )

    wonderful_gas_engine = Engine(
        name="Ford DOHC V-8",
        displacement=5.0,
        power=444,
        fuel_type="GAS"
    )

    jeep = Car(
        name='Jeep',
        engine=best_diesel_engine,
        passengers=5,
    )

    man = Track(
        name="Man",
        engine=best_diesel_engine,
        carrying=16,
        number_of_wheels=6
    )

    yacht = Boat(
        name='Beda',
        engine=best_diesel_engine,
        passengers=15,
        draught=600
    )
    strange_amphibian = Amphibian(
        name='Triton Bus',
        engine=wonderful_gas_engine,
        passengers=8,
        draught=200,
        number_of_wheels=4
    )



    print(yacht)
    print(strange_amphibian)

    stanley = Person(name="Stanley", ticket_id="444333")
    willy = Person(name="Willy", ticket_id="555666")
    doors = Goods(name='50 doors', weight=0.05, count=50)
    print(jeep)
    jeep.loading(stanley)
    print(jeep)
    print(jeep.on_board)

    print(man)
    man.loading(willy)

    man.loading(doors)
    print(man)




