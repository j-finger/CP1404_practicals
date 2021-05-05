from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance based on the Car class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability < random.randint(0, 100):
            return super().drive(distance)
        else:
            return 0
