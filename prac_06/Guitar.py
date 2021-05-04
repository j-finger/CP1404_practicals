"""CP1404 Practical 06 - Jacob Finger 2021 - Guitar class"""
VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name, year, cost):
        """Initialise a Guitar instance
        year: int
        cost: float"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "Guitar: {guitar.name} made in {guitar.year} and costs {guitar.cost}".format(guitar=self)

    def get_age(self):
        """Get the age of the guitar in the present year (2021)"""
        return 2021 - self.year

    def is_vintage(self):
        """Returns true if the guitar is vintage and thereby over 50 years old"""
        return self.get_age() >= VINTAGE_AGE
