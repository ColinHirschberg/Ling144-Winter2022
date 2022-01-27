# Some regular expression practice problems
# For debugging, head to:
#   https://regex101.com/
# Other references:
#   https://www.w3schools.com/python/python_regex.asp

import re

# abc's of regex
abc = ["abc",
  "abb",
  "adc",
  "abcc",
  "abccb",
  "abccc",
  "adcabcc",
  "abcccc",
  "abccccc",
  "cdababcd",
  "abcccccc",
  "abcbcbcbc",
  "abcb"
]

# First things first,  use a for loop to print out each word in the variable 'wordList' above to the console.



# 1. Find a regular expression that finds all the words with 'ab' in them. 

print('The pattern XXXX finds all words in wordList:')
for word in abc:
	abc_all = re.findall("ab.*", word)
	print(abc_all)

# 2. How would we re-write this regex to match the whole element in the list?

# 3. Find a regular expression that picks out only those words that match ab or abc at the beginning of the word


# 4. Find a regular expression that finds all the words with 'ab' at the beginning. 


# 5. Let's look at this using regex's .search():

searchString = "I do not like green eggs and ham"
match = re.search("ee", searchString)
print(match) #this will print an object

# .string, .span(), .group()



# 6. Find a regular expression that captures all the words with at least 2 c's in them.



emails = [
  "timtroyr@att.net",
  "jcholewa@aol.com",
  "leakin@live.com",
  "stellaau@outlook.com",
  "sbmrjbr@outlook.com",
  "pontipak@yahoo.com",
  "draper@icloud.com",
  "fudrucker@sbcglobal.net",
  "yumpy@gmail.com",
  "nichoj@hotmail.com",
  "meder@outlook.com",
  "hahiss@hotmail.com"
]

# 7. Extract only the part of the email that comes before the @ sign with a regex pattern



# 8. Extract only the names of the service provider (gmail, hotmail, etc...)