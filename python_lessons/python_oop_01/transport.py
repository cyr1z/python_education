"""
Transport classes
"""


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


class Transport:
    """
    Base transport class
    """

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def __str__(self):
        return f"{self.name} / {self.engine} "


class Cargo(Transport):
    """
    Cargo transport class
    """

    def __init__(self, name, carrying, engine):
        super().__init__(name, engine)
        self.carrying = carrying

    def __str__(self):
        return super().__str__() + f"T carrying / {self.carrying}"


class Passenger(Transport):
    """
    Passenger transport class
    """

    def __init__(self, name, engine, passengers):
        super().__init__(name, engine)
        self.passengers = passengers

    def __str__(self):
        return super().__str__() + f" / {self.passengers} passengers "


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

    print(jeep)
    print(man)
    print(yacht)
    print(strange_amphibian)
