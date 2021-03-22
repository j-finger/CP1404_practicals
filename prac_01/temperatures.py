"""
CP1404 - Practical 1
Celsius to fahrenheit converter and vice versa

get conversion type or quit signal
while not quit
    if conversion type = fahrenheit
        get temperature
        convert to celsius
        display temperature in celsius
    else if conversion type = celsius
        get temperature
        convert to celsius
        display temperature in fahrenheit
    else
        display "invalid option"
display thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
