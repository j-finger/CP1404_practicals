"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""
import doctest
from prac_06.car import Car


def repeat_string(s='string', n=2):
    """Repeat string s, n times, with spaces in between."""
    return " ".join(s for i in range(n))


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0

    test_car = Car(fuel=10)
    assert test_car.fuel == 10


run_tests()

doctest.testmod()


def punctuate_sentence(string_in="some words"):
    """
    Apply basic punctuation to a limited number of formats.
    :param string_in: any string of words (preferred)
    :return: Capitalised first word and a full stop at the end.
    >>> punctuate_sentence('hello')
    'Hello.'
    >>> punctuate_sentence('It is an ex parrot.' )
    'It is an ex parrot.'
    >>> punctuate_sentence('3rok3n sentence.')
    '3rok3n sentence.'
    """
    list_of_chars = list(string_in)
    list_of_chars[0] = list_of_chars[0].upper()
    if list_of_chars[-1] != '.':
        list_of_chars += '.'
    return "".join(list_of_chars)
