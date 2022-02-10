# a dictionary of number words
number_words = {"uno": "eins", "dos": "zwei", "tres": "drei"}

# some helpful things you can do with dictionaries

# 1. use the list() function to turn parts of your dictionaries into lists:

list(number_words.keys())
list(number_words.values())
list(number_words.items())

# 2. Use the keys of the dictionary to substitute for values in a string:

string = "{uno} plus {dos} equals {tres}"
string.format(**number_words)