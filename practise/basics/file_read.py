_author_ = "Rifatul Islam"
import json

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

# This is not a safe operation, as the file is not closed after being opened.
# file = open("../../test.txt", 'r+')
# for line in file:
#     print(line)

# This is safe operation
try:
    file = open("../../test.txt", "r+")
    for line in file:
        print(line)
except FileNotFoundError as ferr:
    print(ferr)
finally:
    file.close()

# Alternate and more convenient way is to use the with statement.
# this close the file after being read
with open("../../test.txt", 'r+') as file:
    print(file.read())

#Serializable objects can be written in file as JSON format
json.dump(basket, file)