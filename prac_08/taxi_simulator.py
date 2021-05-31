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
            valid_index = False
            while not valid_index:
                try:
                    print("Taxis available:")
                    print_taxi_list(taxis)
                    user_input = input("Choose taxi: ").lower()
                    current_taxi = taxis[int(user_input) - 1]
                    valid_index = True
                except IndexError:
                    print("That taxi does not exist!")
                except ValueError:
                    print("That's not a valid integer!")
            print("Bill to date: ${:.2f}".format(bill))

        elif user_input == 'd':
            """Drives the current taxi a given distance"""
            if current_taxi:
                current_taxi.start_fare()
                valid_integer = False
                while not valid_integer:
                    try:
                        distance_to_drive = int(input("Drive how far? "))
                        valid_integer = True
                    except ValueError:
                        print("That's not a valid integer!")
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                bill += trip_cost
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                print("Bill to date: ${:.2f}".format(bill))
            else:
                print("You don't have a taxi selected! Please select a valid taxi")

        else:
            print("That is not a valid menu choice")
        user_input = input(MENU).lower()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    print_taxi_list(taxis)


def print_taxi_list(taxis):
    """Displays the list of taxis"""
    for i, taxi in enumerate(taxis, 1):
        print("{} - {}".format(i, taxi))


main()
