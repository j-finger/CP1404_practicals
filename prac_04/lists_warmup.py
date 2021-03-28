"""
CP1404 Practical 4 - Jacob Finger

Lists warmups
"""

numbers = [3, 1, 4, 1, 5, 8, 2]

print(numbers[0])  # 3
print(numbers[-1])  # 2
print(numbers[3])  # 1
print(numbers[:-1])  # 3 1 4 1 5 8
print(numbers[3:4])   # 1
print(5 in numbers)  # 4
print(7 in numbers)  # null
print("3" in numbers)  # null
print(numbers + [6, 5, 3])  # numbers = [3, 1, 4, 1, 5, 8, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[0], numbers[-1])
print(numbers[2:])
print(9 in numbers)
