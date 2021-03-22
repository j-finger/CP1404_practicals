"""
CP1404 - Practical 1

Different loop examples
"""

# Odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Sets of 10 from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Countdown from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Asks the user for a number of stars and then prints them on one line
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# Prints the stars in a slanted stack
for i in range(0, number_of_stars+1, 1):
    print("*" * i)
