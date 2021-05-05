"""Practical 08 - Jacob Finger - SilverServiceTaxi Testing"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi1 = SilverServiceTaxi("Hummer", 300, 4)
    print(taxi1)
    taxi1.drive(50)
    print(taxi1.get_fare())
    taxi2 = SilverServiceTaxi("Porsche", 30, 2)
    taxi2.drive(18)
    print("Expected $48.80 got ${:.2f}".format(taxi2.get_fare()))


main()
