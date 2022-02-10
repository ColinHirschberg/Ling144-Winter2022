# Practice with try/except blocks!

# Open a file, and print it line by line.

with open('inferno.txt', 'r') as file:
    for line in file:
        print(line)

print('--Done with importing the file--')
print('out of the with block')


