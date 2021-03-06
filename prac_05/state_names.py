"""
CP1404 -  Practical 5 - Jacob Finger
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state_code = (input("Enter short state: ")).upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print("{:3} is {}".format(state_code, CODE_TO_NAME[state_code]))
    else:
        print("Invalid short state")
    state_code = (input("Enter short state: ")).upper()
