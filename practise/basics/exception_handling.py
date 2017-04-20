_author_ = "Rifatul Islam"


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
    This exception is raised when we divide something with the number 0
    """

    def __int__(self, divident, message="Devide by zero Error"):
        self.divident = divident
        self.message = message


try:
    raise MathError("This is a test error")

except MathError as msg:
    print("Opps, this is a error", msg)
    # print(msg)


def divide(x, y):
    try:
        result = x / y

    except ZeroDivisionError as zr:
        print(zr)
    else:
        print("Reslt is : ", result)
    finally:
        print("Function is excecuted")


divide(2, 0)