from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0
    print("Let's drive!")
    user_input = input(MENU).lower()
    while user_input != 'q':
        if user_input == 'c':
            """Display available taxis for hire and prompt the user to select one"""
            print("Taxis available:")
            print_taxi_list(taxis)
            user_input = input("Choose taxi: ").lower()
            current_taxi = taxis[int(user_input)]
            print("Bill to date: ${:.2f}".format(bill))
        elif user_input == 'd':
            if not current_taxi:
                current_taxi.start_fare()
                distance_to_drive = int(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                bill += trip_cost
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
        else:
            print("You don't have a taxi selected! Please select a valid taxi")
        user_input = input(MENU).lower()


def print_taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
