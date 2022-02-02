# Functions and practice 

# some familiar practice functions

def sumNumbers(num1, num2):
  result = num1 + num2
  print(result)
  return result

def weather(name, city, fahrenheit):
  celsius = (fahrenheit - 32) / 1.8
  print(f"Hi {name}, it's currently {fahrenheit} Fahrenheit in {city}, which is {celsius} in Celsius")
  return celsius


# # Here's our old palindrome program -- let's make a few functions and re-write it.

# example = input('Give me a palindrome: ')
# print(example)

# # Take user input and use a loop to:
# #   Save the first letter as the last letter, second letter as second to last letter, etc...
 
# compare_word = ''
# new_compare_word = example.lower().replace(" ", "").replace(",", "").replace("'", "")

# for letter in new_compare_word:
#   compare_word = letter + compare_word
# reversed_example = compare_word

# if  reversed_example == new_compare_word:
#   print(f"YES, {example} is a palindrome")
# else:
#   print(f"NO, {example} is NOT a palindrome")
