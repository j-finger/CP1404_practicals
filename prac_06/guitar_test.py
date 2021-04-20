from prac_06.Guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 440)
    print("{} get_age() - Expected 99. Got {}".format(guitar1.name, guitar1.get_age()))
    print("{} get_age() - Expected 8. Got {}".format(guitar2.name, guitar2.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(guitar1.name, guitar1.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(guitar2.name, guitar2.is_vintage()))


main()
