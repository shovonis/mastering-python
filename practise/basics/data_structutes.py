from collections import deque



_author_ = "Rifatul Islam"


stack = [1, 2 , 3, 4]
stack.append(5)
stack.append(6)

print(stack)
print(stack.pop())
print(stack.pop())

queue = deque([1, 2, 3, 4])
queue.append(5)
queue.append(6)

print("Queue: ", queue)
print(queue.popleft())
print(queue.popleft())

spam = ['cat', 'bat', 'rat', 'elephant']
print("Spam: ",spam[0:-1])

# Lambdas and Maps in python
squres = list(map(lambda x: x ** 2, range(10)))
print(squres)

# Using for clause in python
another_list = [x * 4 + 2 for x in range(20)]
print(another_list)

# For clause is awesome in python saves a lot of time and it is more readable
#Here is a more complex list
a_more_complex_list = [(x, y) for x in range(10) for y in range(20) if (y % 2 != 0 and x != y)]
print(a_more_complex_list)

another_example = [(x, (x + 4) ** 2) for x in range(10) if x % 2 == 0]
print(another_example)

aTuple = ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
print(aTuple)
print(aTuple[0])

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a_set_of_spell = {x for x in 'abrakadabra' if x not in 'abc'}
print(a_set_of_spell)

a_dic = {'guido': 4127, 'irv': 4127, 'jack': 4098}
print(a_dic)
print(a_dic.items())
print(a_dic.keys())
print(a_dic.values())

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print("What is your favorite{0}? Its a {1}.".format(q,a))

from math import pi, sin
sine_table = [sin(x*pi/180) for x in range(0, 91)]
print(sine_table)

file = open("../../test.txt", "r+")
distinct_words = set(word for line in file for word in line.lower().split())
print(distinct_words)


