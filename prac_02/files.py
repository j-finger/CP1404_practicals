"""
CP1404 - Prac 2

get name
open "name.txt" as file_out for writing
write name to file_out
close file_out

open "name.txt" as file_in for reading
read name from file_in
display name
close file_in

open "numbers.txt" as file_in for reading
number 1 = first line of file_in
number 2 = second line of file_in
close file_in
total = number 1 + number 2
display total

reset total to 0
open "numbers.txt" as file_in for reading
for line in file_in
    add the line's number to the total

"""

name = input("Please enter your name: ")
file_out = open('name.txt', 'w')
print(name, file=file_out)
file_out.close()

file_in = open('name.txt', 'r')
print(file_in.read())
file_in.close()

file_in = open('numbers.txt', 'r')
num1 = int(file_in.readline())
num2 = int(file_in.readline())
file_in.close()
total = num1 + num2
print(total)

total = 0
file_in = open('numbers.txt', 'r')
for line in file_in:
    total += int(line)
file_in.close()
print(total)
