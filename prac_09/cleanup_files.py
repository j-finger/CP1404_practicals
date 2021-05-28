"""
CP1404 - Practical 9 - File Cleanup Utility - Jacob Finger
"""
import shutil
import os


def main():
    """Iterate through all directories and rename files correctly"""""

    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_and_path = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(file_and_path, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    split_names = ""
    split_names.isupper()
    for i, c in enumerate(new_name):
        if c.isupper() and new_name[i-1].isupper():  # Split 2 uppercase characters
            split_names += '_'
        if c.isupper() and new_name[i-1].islower() and i != 0:  # Split an uppercase and lowercase character
            split_names += '_'
        split_names += c
    return split_names.title()


main()
