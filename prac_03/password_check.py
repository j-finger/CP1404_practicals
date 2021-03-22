"""
CP1404/CP5632 - Practical 3
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""

    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password, MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARS_REQUIRED, SPECIAL_CHARACTERS):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password, min_length, max_length, special_chars_req, special_chars):

    #  Determine if the provided password is valid, given the input parameters
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # count each kind of character
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in special_chars:
            count_special += 1

    # if length is wrong, return False
    if not min_length < len(password) <= max_length:
        return False

    # if any of the 'normal' counts are zero, return False
    elif not count_upper or not count_digit or not count_lower:
        return False

    # if special characters are required, then return False if the count of those is zero
    elif special_chars_req and not count_special:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
