"""
CP1404 - Practical 3
Program to determine score status based on a user input number between 0 & 100
Now with functions!

get score
convert score to grade
display grade

func score_to_grade (score)
    if score < 0 or > 100
        return invalid score
    else if score >= 90
        return excellent
    else if score >= 50
        return passable
    else
        return bad
"""

import random


def main():
    random_int_score = random.randint(0, 101)
    random_float_score = random.uniform(0, 100)
    score = float(input("Enter score: "))
    print("Your score is {}.".format(score_to_grade(score)))
    print("The random integer score {} is {}".format(random_int_score, score_to_grade(random_int_score)))
    print("The random floating score {:.2f} is {}".format(random_float_score, score_to_grade(random_float_score)))


def score_to_grade(numeric_score):
    if numeric_score < 0 or numeric_score > 100:
        return "invalid"
    elif numeric_score >= 90:
        return "excellent"
    elif numeric_score >= 50:
        return "passable"
    else:
        return "bad"


main()
