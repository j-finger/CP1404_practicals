""""CP1404 - Practical 9 - File Sorting V2 - Jacob Finger"""

import os
import shutil


def main():
    """Sort files into user named directories based on file extensions"""
    os.chdir('FilesToSort')
    file_extensions = {}  # Contains the file extension and the directory for those types of files
    for directory_name, subdirectories, filenames in os.walk('.'):  # List all the files within the current folder
        for filename in filenames:
            file_extension = filename[filename.find('.'):]  # Read the file extension
            if file_extension not in file_extensions:  # Check if the file extension has already been allocated a folder
                folder_name = input("What category would you like to sort {} files into? ".format(file_extension))
                file_extensions[file_extension] = folder_name
                try:
                    os.mkdir(folder_name)
                except FileExistsError:
                    pass
            shutil.move(filename, './' + file_extensions[file_extension])  # Move the file to the new folder


main()
