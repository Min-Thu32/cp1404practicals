import random
from car import Car


class UnreliableCar(Car):
    """Represents an UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float, percentage chance that the drive method will actually drive the car
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance with a certain reliability.

        Drive the car only if a randomly generated number is less than the car's reliability.
        """
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
