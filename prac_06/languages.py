"""CP1404 Practical 06 - Jacob Finger 2021 - ProgrammingLanguages class test"""
from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language_list = [ruby, python, visual_basic]  # Input instances into an iterable list

    print("The dynamically typed languages are:")
    for language in language_list:
        if language.is_dynamic():  # Demonstrates functionality of the is_dynamic() method
            print(language.name)


main()
