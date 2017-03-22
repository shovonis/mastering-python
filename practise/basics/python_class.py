_author_ = "Rifatul Islam"


class SimpleClass:
    """"This is a global variable for Simple Class.
    This will be same for all the instances of this same class, unless changed"""
    a_digit = 8

    def __init__(self):
        """This is the constructor like Java.
        Called when instantiaing"""
        print("This is invoked when instantiaing new objects of this class")

    def function(self):
        return "Hello Python Class"


print(SimpleClass.a_digit)  # Invoked like attribute ref
print(SimpleClass.function)

print(SimpleClass().function())


class Dog:
    kind = 'Shephard'

    def __init__(self, name):
        self.name = name


#Taking the default kind value
dog = Dog("Bull")
print(dog.name)
print(dog.kind)

#Taking the default kind value
dog_3 = Dog("German")
print(dog_3.name)
print(dog_3.kind)



class Pet:
    """This is a pet class for testing mutable global objects"""

    pet_kind = [] #This variable is global and mutable for all objects.

    def __init__(self, name):
        self.name = name

    def append_kind(self, kind):
        self.pet_kind.append(kind)

    def __str__(self):
        return "Name: ", self.name, "Kind: ", self.pet_kind



a_cow = Pet("Mooooo I am a cow")
a_cow.append_kind("COW")
print("This is a : ", a_cow.__str__())

a_dog = Pet("I am a Dog")
a_dog.append_kind("DOG")

#This will pring both COW and DOG for kind as the
# kind object was mutable for multiple objects.
print("This is a:", a_dog.__str__())

