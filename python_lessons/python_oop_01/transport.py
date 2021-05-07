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
    """
    Cargo transported Goods
    """

    def __init__(self, name, weight, count):
        self._weight = weight
        self._count = count
        self.name = name

    @property
    def sum_weight(self) -> float:
        """
        summarize weight of goods
        :return: float
        """
        return float(self._weight * self._count)

    def __str__(self):
        return f"{self.name} / {self.sum_weight}kg "


class Person:
    """
    Passenger transport transported Persons
    """

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
        """
        abstract method for loading something on board
        :param something:
        :return:
        """
        raise NotImplementedError("loading method not implemented!")

    @abstractmethod
    def unloading(self, something):
        """
        abstract method for uloading something from board
        :param something:
        :return:
        """
        raise NotImplementedError("unloading method not implemented!")

    @property
    def on_board(self):
        """
        print all items on board
        :return: str
        """
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

    @staticmethod
    def _weight_sum(list_ot_thins) -> float:
        """
        sums up the weight of items on board
        :param list_ot_thins: list of items
        :return: float
        """
        return float(sum(w.sum_weight for w in list_ot_thins))

    @property
    def free_carry(self) -> float:
        """
        calculates the weight available for loading
        :return: float
        """
        return float(self._carrying) - self._weight_sum(self._load)

    @staticmethod
    def _check_thing_type(thing):
        """
        check type of loading thing
        :param thing: Goods
        """
        if not isinstance(thing, Goods):
            raise TypeError(
                f"loading not supported for '{type(thing).__name__}'"
            )

    def _check_available_carry(self, thing):
        """
        check is available carry bigger then things weight
        :param thing:
        :return:
        """
        if thing.sum_weight > self.free_carry:
            raise ValueError("Item weight too much")

    def loading(self, thing):
        """
        load things on board
        :param thing: Goods
        :return:
        """
        self._check_thing_type(thing)
        self._check_available_carry(thing)
        self._load.append(thing)
        print(f'{thing.name} LOADED')

    def unloading(self, thing):
        """
        unload things from board
        :param thing: Goods
        :return:
        """
        self._load.pop(thing)

    def __gt__(self, other):
        if isinstance(other, Goods):
            result = self._carrying > other.sum_weight
        elif isinstance(other, Cargo):
            result = self._carrying > other._carrying
        else:
            raise TypeError(
                f"'>' not supported between instances of "
                f"'{type(other).__name__}' and '{type(self).__name__}'"
            )
        return result

    def __lt__(self, other):
        if isinstance(other, Goods):
            result = self._carrying < other.sum_weight
        elif isinstance(other, Cargo):
            result = self._carrying < other._carrying
        else:
            raise TypeError(
                f"'<' not supported between instances of "
                f"'{type(other).__name__}' and '{type(self).__name__}'"
            )
        return result

    def __ge__(self, other):
        if isinstance(other, Goods):
            result = self._carrying >= other.sum_weight
        elif isinstance(other, Cargo):
            result = self._carrying >= other._carrying
        else:
            raise TypeError(
                f"'>=' not supported between instances of "
                f"'{type(other).__name__}' and '{type(self).__name__}'"
            )
        return result

    def __le__(self, other):
        if isinstance(other, Goods):
            result = self._carrying <= other.sum_weight
        elif isinstance(other, Cargo):
            result = self._carrying <= other._carrying
        else:
            raise TypeError(
                f"'<=' not supported between instances of "
                f"'{type(other).__name__}' and '{type(self).__name__}'"
            )
        return result

    def __str__(self):
        return super().__str__() + f"/ {self.free_carry}T free "


class Passenger(Transport):
    """
    Passenger transport class
    """

    def __init__(self, name, engine, passengers: int):
        super().__init__(name, engine)
        self._passengers = passengers

    def _passenger_names(self):
        return tuple(passenger.name for passenger in self._load)

    def __contains__(self, person):
        if isinstance(person, Person):
            result = person in self._load
        else:
            raise TypeError(
                f"'in' not supported between instances of "
                f"'{type(person).__name__}' and '{type(self).__name__}'"
            )
        return result

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

    cat = Track(
        name="Caterpillar",
        engine=best_diesel_engine,
        carrying=200,
        number_of_wheels=4
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

    try:
        print("Stanley" in jeep)
    except TypeError as error:
        print(error)

    print(stanley in jeep)

    print(man)
    try:
        man.loading(willy)
    except TypeError as error:
        print(error)

    man.loading(doors)
    print(man)

    print(f'Is {cat.name} bigger than {man.name}? - Is', cat > man)
    print(f'Is {doors.name} bigger than {man.name}? - Is', doors > man)

    try:
        print(best_diesel_engine > man)
    except TypeError as error:
        print(error)
