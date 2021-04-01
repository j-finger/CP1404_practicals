"""
CP1404 - Practical 5 - Jacob Finger
Word occurrence calculator
"""
word_count = {}
user_string = input("Please enter a nice long string with plenty of words in it:\n").split()

for word in user_string:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1

user_string.sort()

words_to_sort = list(word_count.keys())
words_to_sort.sort()
max_word_length = len(max(user_string, key=len))

for sorted_word in words_to_sort:
    print("{:{}} : {}".format(sorted_word, max_word_length, word_count[sorted_word]))
