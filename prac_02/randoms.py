import random
print(random.randint(5, 20))  # Min = 5, Max = 20
print(random.randrange(3, 10, 2))  # Min = 3, Max = 9
print(random.uniform(2.5, 5.5))  # Min = 2.5, Max = 5.5

#  As a floating/integer number was not specified I have provided solutions to both below
print(random.randint(1, 100))  # Displays a random integer number from 1 to 100 (inclusive)
print(random.uniform(1, 100))  # Displays a random floating number from 1 to 100 (inclusive)
