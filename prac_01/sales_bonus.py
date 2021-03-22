"""
CP1404 - Practical 1

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales > 0
    if sales >= 1000
        bonus = 15% of sales
    else
        bonus = 10% of sales
    display your bonus is $xxx.xx
"""

sales = float(input("Please enter sales: $"))
while sales > 0:
    if sales >= 1000:
        bonus = sales * 0.15
    else:
        bonus = sales * 0.1
    print("Your bonus is: ${:.2f}".format(bonus))
    sales = float(input("Please enter sales: $"))
