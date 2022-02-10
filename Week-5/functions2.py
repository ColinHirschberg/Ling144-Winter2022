def sumNumbers(num1, num2):
  result = num1 + num2
  return result

def concatenate(element1, element2):
  result = element1 + element2
  return result


var1 = sumNumbers(2, 6)
var2 = concatenate(2, 6)

print("the output of sumNumbers is ", var1)
print("the output of concatenate is ", var2)

var3 = sumNumbers("cran", "berry")
var4 = concatenate("cran", "berry")

print("the output of sumNumbers is ", var3)
print("the output of concatenate is ", var4)