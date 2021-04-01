"""
CP1404 - Practical 5 - Jacob Finger
"""
email_name_dict = {"name@gmail.com": "Na Me", "123@numbers.com": "Number Man", "student@my.jcu.edu.au": "Stew Dent"}
NO_OPERANDS = ["no", "n", "nah"]
YES_OPERANDS = ["yes", "y", "", "yeah"]


def main():

    email = input("Please enter your email: ")
    while email != '':  # email input loop
        email_name_dict += [email_to_add]
        email_to_add = input("Please enter your email: ")

    for email, name in email_name_dict.items():
        print("{} ({})".format(name, email))


def retrieve_name_from_email():
    #  Function to lookup the name of an email, and change it if it's wrong
    email_to_retrieve = input("Email: ")
    while email_to_retrieve != '':
        if email_to_retrieve in email_name_dict:  # checks if the email exists in data base
            #  Asks the user if the name is correct
            correct_name = input("Is your name {}? (Y/n) ".format(email_name_dict[email_to_retrieve])).lower()
            if correct_name in YES_OPERANDS:
                pass
            elif correct_name in NO_OPERANDS:
                email_name_dict[email_to_retrieve] = input("Name: ").title()
            else:
                print("That is not an appropriate response.")
                correct_name = input("Is your name {}? (Y/n) ".format(email_name_dict[email_to_retrieve])).lower()
            email_to_retrieve = input("Email: ")
        else:
            print("That email does not exist!")
            email_to_retrieve = input("Email: ")


main()
