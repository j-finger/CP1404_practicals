"""Practical 08 - Jacob Finger - SilverServiceTaxi Class"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Version of Taxi with flagfall and fare cost that is multiplied by a given fanciness factor"""
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like Taxi but with flagfall cost"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Return the price for the taxi trip including the flagfall"""
        return super().get_fare() + self.flag_fall
