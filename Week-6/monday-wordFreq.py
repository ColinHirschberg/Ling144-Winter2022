# This is the first page or do of Moby Dick, by Herman Melville
# Taken from Project Gutenberg, https://www.gutenberg.org/files/2701/2701-0.txt

# ========================
# Functions
# ========================

def getMobyDickWords():
    mobydick = """Call me Ishmael. Some years ago-- never mind how long precisely-- having
little or no money in my purse, and nothing particular to interest me on
shore, I thought I would sail about a little and see the watery part of
the world. It is a way I have of driving off the spleen and regulating
the circulation. Whenever I find myself growing grim about the mouth;
whenever it is a damp, drizzly November in my soul; whenever I find
myself involuntarily pausing before coffin warehouses, and bringing up
the rear of every funeral I meet; and especially whenever my hypos get
such an upper hand of me, that it requires a strong moral principle to
prevent me from deliberately stepping into the street, and methodically
knocking people's hats off-- then, I account it high time to get to sea
as soon as I can. This is my substitute for pistol and ball. With a
philosophical flourish Cato throws himself upon his sword; I quietly
take to the ship. There is nothing surprising in this. If they but knew
it, almost all men in their degree, some time or other, cherish very
nearly the same feelings towards the ocean with me.
There now is your insular city of the Manhattoes, belted round by
wharves as Indian isles by coral reefs-- commerce surrounds it with
her surf. Right and left, the streets take you waterward. Its extreme
downtown is the battery, where that noble mole is washed by waves, and
cooled by breezes, which a few hours previous were out of sight of land.
Look at the crowds of water-gazers there."""
    normedText = mobydick.replace("\n", " ")
    punctuation = ";:,.?!-"
    for punct in punctuation:
        normedText = normedText.lower().replace(punct, "")
        normedList = normedText.split(" ")
    return normedList

words_list = getMobyDickWords()
print(words_list)

# Count the number of occurrences of each word and save those numbers in a list.
# First: make a list of the count of each word in our list words_list
# loop through all the words in our list:
#  save a variable that counts how many times that word appears in our list
# append that count to word_frequency
#print(word_frequency)

word_frequency = []
for word in words_list:
  freq = words_list.count(word)
  word_frequency.append(freq)

print(word_frequency)



# zip our two lists into a dictionary:

mobyDict = dict(zip(words_list, word_frequency))


# print our dictionary, formatted with each key/value pair on one line

for word, freq in mobyDict.items():
  print(word, " : ", freq)

# print our dictionary sorted in order from most frequent to least frequent:

for word in sorted(mobyDict, key=mobyDict.get, reverse=False):
  print(word, " : ", mobyDict[word])