"""
CP1404 - Practical 5 - Jacob Finger
Email library program
"""
CONTINUATION_PHRASES = ['', "yes", 'y', "yeah"]


def main():
    email_name_dict = {"name@gmail.com": "Na Me", "123@numbers.com": "Number Man", "student@my.jcu.edu.au": "Stew Dent"}
    email_to_add = input("Email: ")
    while email_to_add != '':  # email input loop
        if email_to_add in email_name_dict.keys():  # checks if the email is already in the dictionary
            print("That email already exists!")
        elif '@' not in email_to_add:  # checks if the email is vaild
            print("That email is not valid!")
        else:
            # This is my one line solution to processing the name from the email, although I feel its not whats asked
            # name_to_add = email_to_add.split('@')[0].replace('.', ' ').title()
            name_to_add = name_from_email(email_to_add)
            user_answer = input("Is your name {}?".format(name_to_add))
            # changes the user's name if the predicted one is wrong
            if user_answer.lower() not in CONTINUATION_PHRASES:
                name_to_add = input("Name: ").title()
            email_name_dict[email_to_add] = name_to_add

        email_to_add = input("Email: ")

    for email, name in email_name_dict.items():  # prints all emails and names in the dictionary
        print("{} ({})".format(name, email))


def name_from_email(email):
    # Function to return predicted name from a given email
    names = email.split('@')[0]
    names = names.split('.')
    full_name = " ".join(names).title()
    return full_name


main()
