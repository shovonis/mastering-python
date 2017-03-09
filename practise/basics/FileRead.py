_author_ = "Rifatul Islam"
import json


file = open("../../test.txt", 'r+')
for line in file:
    print(line)

# file.close()

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

# with open("../../test.txt", 'r+') as file:
#     print(file.read())

json.dump(basket, file)