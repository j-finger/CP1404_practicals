"""
CP1404 - Practical 9 - File Cleanup Utility - Jacob Finger
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    split_word = ""
    split_word.isupper()
    for i, c in enumerate(new_name):
        if c.isupper() and new_name[i-1].isupper():
            split_word += '_'
        if c.isupper() and new_name[i-1].islower() and i != 0:
            split_word += '_'
        split_word += c
    return split_word.title()


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics/Christmas')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            file_and_path = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(file_and_path, new_name)


main()
# demo_walk()
