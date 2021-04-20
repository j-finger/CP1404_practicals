"""CP1404 Practical 06 - Jacob Finger 2021 - ProgrammingLanguage class example """


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance

        reflection: boolean
        year: int"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{x.name}, {x.typing} Typing, Reflection={x.reflection}, First appeared in {x.year}".format(x=self)

    def is_dynamic(self):
        """Checks if the language is dynamically typed
        :return: True/False
        """
        if self.typing == "Dynamic":
            return True
        else:
            return False

