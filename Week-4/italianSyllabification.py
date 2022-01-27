# Italian Syllabification
#
# ====== The task: ====== 
# 

import re

# Here's the first Canto of Dante's inferno from Italian,
# imported from the file 'inferno.txt' in this same
# directory, and saved as a string to the variable 'inferno':

with open("inferno.txt") as file:
   testString = file.read()

print(inferno)

# Italian Rules of Syllabification

# Italian syllable onsets

three_cons = ["sfl", "sfr", "spl", "spr", "sbl", "sbr", "str", "sdr", "scl", "scr",  "sgl", "sgr", "sgn", "sch", "sgh"]

two_cons = ["fl", "fr", "vl", "vr", "pl", "pr", "pn", "ps", "bl", "br", "mn", "sf", "sv", "sp", "sb", "sm", "st", "sd", "sn", "sl", "sr", "sc", "sg", "ch", "tr", "tm", "dr", "cl", "cr", "sq", "gl", "gr", "gn", "gh"]

one_cons = ["f", "v", "p", "b", "m", "s", "z", "t", "d", "n", "l", "r", "c", "g", "h", "q"]

onsets = one_cons + two_cons + three_cons

# Italian vowels

vowels = ["a", "e", "i", "o", "u", "à", "è", "ì", "ò", "ù", "ï", "é", "ó" ]


# test sentence:

testString = "noi scusiamo il ragazzo, non sa cosa fa"

# we want our output to look like:
# .no.i. .scu.si.a.mo. .il. .ra.gaz.zo .non. .sa. .co.sa. .fa.

# First: clean up our string, save it to a list:

testList = ""

print(testList)

#I've started this for us, and added directions for what we need to do to finish it:


for word in testList:
  newWord = ""
  i = 0
  while i < len(word):
    onset_seq_length = 1
    # Check if this letter is the start of an 
    # onset sequence
    while word[i:i + onset_seq_length] in onsets:
      # Check if we've reached the end of the word
      
      # Could still be an onset sequence
      
    if word[i + onset_seq_length - 1] in vowels:
      # The whole sequence is an onset plus a nucleus!
      
      # Move the "cursor" past the sequence we just found
      
    else:
      # That letter couldn't be the start of an onset
      # sequence -- it had to be a coda.  Add the coda
      # to the latest syllable and try the next letter.
      
  print(newWord + ".")
