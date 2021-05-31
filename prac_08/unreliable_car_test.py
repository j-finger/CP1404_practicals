""" CP1404 - Practical 08 - Unreliable Car testing - Jacob Finger """
from prac_08.unreliable_car import UnreliableCar


def main():
    """Test the unreliable car class under a variety of conditions"""

    nissan_xtrail = UnreliableCar("Old mate's Nissan", 20, 90)
    n70_hilux = UnreliableCar("gOoD hoRse", 8000, 1)
    daily_commute = 23
    for daily_trip in range(21):
        nissan_xtrail.drive(daily_commute)
        n70_hilux.drive(daily_commute)
        print("{}. {}".format(daily_trip, nissan_xtrail))
        print("{}. {}".format(daily_trip, n70_hilux))


main()
