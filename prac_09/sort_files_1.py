""""CP1404 - Practical 9 - File Sorting V1 - Jacob Finger"""

import os
import shutil


def main():
    """Sort files into directories based on their extensions"""
    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):  # List all the files within the current folder
        for filename in filenames:
            file_extension = filename[filename.find('.'):]
            try:
                os.mkdir(file_extension)  # Make a new directory based on the file extension
            except FileExistsError:
                pass
            shutil.move(filename, './' + file_extension)  # Move the file to the new folder


main()
