"""
CP1404 Practical 4 - Jacob Finger
List Exercises
"""
#  Exercise 1 - Numbers
AMOUNT_OF_NUMBERS = 5
list_of_numbers = []

for i in range(AMOUNT_OF_NUMBERS) :
    list_of_numbers.append(int(input("Number: ")))

print("The first number is {}".format(list_of_numbers[0]))
print("The last number is {}".format(list_of_numbers[-1]))
print("The smallest number is {}".format(min(list_of_numbers)))
print("The largest number is {}".format(max(list_of_numbers)))
print("The average number is {:.1f}".format(sum(list_of_numbers)/len(list_of_numbers)))


#  Exercise 2 - Security Checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

users_name = input("Please enter your name: ")
if users_name in usernames:
    print("Access Granted")
else:
    print("Access Denied")
