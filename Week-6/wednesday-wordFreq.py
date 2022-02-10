# This is the first page or do of Moby Dick, by Herman Melville
# Taken from Project Gutenberg, https://www.gutenberg.org/files/2701/2701-0.txt

# ========================
# Functions
# ========================

def getMobyDickWords():
# MODIFY ME!
    normedText = mobydick.replace("\n", " ")
    punctuation = """;:,."?!-"""
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

#print(word_frequency)



# zip our two lists into a dictionary:

mobyDict = dict(zip(words_list, word_frequency))


# print our dictionary, formatted with each key/value pair on one line

for word, freq in mobyDict.items():
  print(word, " : ", freq)

# print our dictionary sorted in order from most frequent to least frequent:

for word in sorted(mobyDict, key=mobyDict.get, reverse=False):
  print(word, " : ", mobyDict[word])