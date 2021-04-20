"""CP1404 Practical 06 - Jacob Finger 2021 - Guitar class"""


class Guitar:
    def __init__(self, name, year, cost):
        """Initialise a Guitar instance
        year: int
        cost: float"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "Guitar: {x.name} made in {x.year} and costs {x.cost}".format(x=self)

    def get_age(self):
        """Get the age of the guitar in the present year (2021)"""
        return 2021 - self.year

    def is_vintage(self):
        """Returns true if the guitar is vintage and thereby over 50 years old"""
        if self.get_age() > 50:
            return True
        else:
            return False
