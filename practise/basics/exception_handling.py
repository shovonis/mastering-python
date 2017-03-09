# _author_ = "Rifatul Islam"
#
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#
#

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [D, C, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# try:
#     raise NameError("Salut, Je'mapplle Rifatul")
# except NameError:
#     print("My Name is Rifatul")
#     raise



class Error(Exception):
    pass

class CustomValidatorException(Error):
    """Exception raised for errors in the input.

    Attributes: expression -- input expression in which the error occurred message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.message = message
        self.expression = expression

class MathError(Error, ZeroDivisionError):
    """
    This exception is raised when we devide something with the number 0
    """
    def __int__(self, divident, message="Devide by zero Error"):
        self.divident = divident
        self.message=message



try:
    raise MathError

except MathError as msg:
    print("Opps!!, Something went wrong: ".format(msg))
