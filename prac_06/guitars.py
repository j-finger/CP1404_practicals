"""CP1404 Practical 06 - Jacob Finger 2021
Guitars exercise.
"""
from prac_06.Guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ")
    while name != '':
        """Creates a Guitar instance based on given name,
        year and cost and appends it to the list of guitars.
        Runs until no guitar name is input"""
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${:,.2f} added.\n".format(name, year, cost))
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars):
        """Iterates through the list of guitars and prints them neatly
        If the guitar is vintage, appends (vintage) to the end of the line"""
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {x.name:>20} ({x.year}), worth ${x.cost:10,.2f}{}".format(i + 1, vintage_string, x=guitar))


main()
