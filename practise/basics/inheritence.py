_author_ = "Rifatul Islam"


class Pet:
    def __init__(self, kind, color):
        self.kind = kind
        self.color = color
        print("I am a ", kind, "and my color is: ", color)

    def print_pet_details(self):
        pass


class Dog(Pet):
    def __init__(self, name, kind, color):
        self.name = name
        self.kind = kind
        self.color = color
        super().__init__(kind, color)
        print("My name is: ", name)

    def print_pet_details(self):
        print("this is a overriden method")

    def _this_is_a_private_method(self):
        """There is no private method/attribute in Python."""
        print("This acts like a private method")


dog = Dog("Sophie", "DOG", "Black")
dog._this_is_a_private_method()  # this is just a convention, nothing more than that

print(issubclass(Dog, Pet))
print(isinstance(dog, Dog))


class Worker:
    pass


empl = Worker()
empl.name = "Saad"
empl.job = "Testing"

print(empl.name)
print(empl.job)
