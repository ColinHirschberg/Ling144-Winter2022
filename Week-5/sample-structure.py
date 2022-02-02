# Anatomy of a well-structured program

import re     # import statements come first
import os     # these are the extra libraries you might need

def multiply_by_12(number):   # function definitions next
  result = number * 12
  return result

def divide_by_3(number):
  result = number / 3
  return result

numList = [1, 2, 3, 4, 5, 6]      # declare global variables

for index in range(len(numList)):             # control flow statements
  numList[index] = multiply_by_12(numList[index])
  numList[index] = divide_by_3(numList[index])
print(numList)
