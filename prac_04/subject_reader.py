"""
CP1404 Practical 4 - Jacob Finger
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for jcu_class in data:
        print("{} is taught by {:<12} and has {:>3} students".format(jcu_class[0], jcu_class[1], jcu_class[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_lists = []
    for line in input_file:
        #  print(line)  # See what a line looks like
        #  print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #  print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #  print(parts)  # See if that worked
        #  print("----------")
        list_of_lists.append(parts)
    input_file.close()
    return list_of_lists


main()
