_author_ = "Rifatul Islam"

a = 2
b = 3

print("Use of ** operator (exponent): ", b ** a)
print("Use of // operator(divide without reminder): ", b // a)
print("Use of ^ bitwise mask: ", b ^ a)


# In python list can contains different sets of data types.
aList = ["This is a list", 123, 690.9, ["this is list inside list", 90], "this is outer string"]
print(aList)

aList.append("Appending a String to aList")
print(aList)

aList.extend("Extending aList")
print(aList)


#Tupeles are deinded with () and are not mutable

aTuple = ("This is a tuple", 2334, 2344.0, "Another String")
print(aTuple)

theIteratorInpython = "Iterator"

print(theIteratorInpython[1:5])

# # a simple fibonocci
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b


#simple if
# x = int(input("Please enter an integer: "))
# if (x< 0):
#     print("Negative Number")
# else:
#     print("Positive Number")

# words = ['cat', 'window', 'defenestrate']
#
# for w in words:
#     print(w, len(w))
#


# for i in range(5, 10, 3):
#     print(i)

# Enumuration
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))