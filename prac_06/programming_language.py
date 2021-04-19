class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{x.name}, {x.typing} Typing, Reflection={x.reflection}, First appeared in {x.year}".format(x=self)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

