"""
CP1404/CP5632 - Practical
Program to determine score status based on a user input number between 0 & 100

get score
if score < 0 or > 100
    display invalid score
else if score >= 90
    display excellent
else if score >= 50
    display passable
else
    print bad
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")