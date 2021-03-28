"""
CP1404 - Practical 4 - Jacob Finger
Do it from scratch quick pick program

PICKS_PER_LINE = 6
MIN_PICK = 1
MAX_PICK = 45

get number_of_quick_picks
for i in number_of_quick_picks
    picks = []
    for picked_numbers in PICK_PER_LINE
        add random integer between MIN_PICK and MAX_PICK to picks
    sort the picks
    print the picks on one line (must be variable i.e.3 picks, 9 picks, etc...)
"""
import random

PICKS_PER_LINE = 6
MIN_PICK = 1
MAX_PICK = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        picks = []
        for p in range(PICKS_PER_LINE):
            # adds a random integer number within a range to the 'picks' list
            picks.append(random.randint(MIN_PICK, MAX_PICK))
        picks.sort()  # sort picks from lowest to highest
        for x in range(PICKS_PER_LINE):
            print("{:2} ".format(picks[x]), end='')  # prints all the picks from a set on one line
        print('')


main()
