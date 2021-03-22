"""
CP1404 - Practical 1

Shopping list calculator

get number of items purchased
while number of items > 0
if total price > 100
    display total price * 0.9
else
    display total price
"""

number_of_items = int(input("Number of items: "))

while number_of_items < 1:
    print("Value cannot be equal to or less than 0!")
    number_of_items = int(input("Number of items: "))
else:
    price_of_items = [float(input("Price of item: ")) for x in range(number_of_items)]
    if sum(price_of_items) > 100:
        print("Total price for {} items is ${:.2f}".format(number_of_items, sum(price_of_items)*0.9))
    else:
        print("Total price for {} items is ${:.2f}".format(number_of_items, sum(price_of_items)))
