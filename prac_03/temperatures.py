"""
CP1404 - Practical 3
Celsius to fahrenheit converter and vice versa, now with functions!

get conversion type or quit signal
while not quit
    if conversion type = fahrenheit
        get temperature
        display converted temperature in celsius
    else if conversion type = celsius
        get temperature
        display converted temperature in fahrenheit
    else
        display "invalid option"
display thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            user_temp = float(input("Celsius: "))
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(user_temp)))
        elif choice == "F":
            user_temp = float(input("Fahrenheit: "))
            print("Result: {:.2f} C".format(fahrenheit_to_celsius(user_temp)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(temp_in):
    #  Converts a celsius value and returns it in fahrenheit
    return temp_in * 9.0 / 5 + 32


def fahrenheit_to_celsius(temp_in):
    #  Converts a fahrenheit value and returns it in celsius
    return 5 / 9 * (temp_in - 32)


main()
