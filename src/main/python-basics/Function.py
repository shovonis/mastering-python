_author_ = "Rifatul Islam"


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# Invalid function calls
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# def chesse_shop(kind, *types, **categories):
#     """This is a function that takes a var list and var dictionaty as arugumemnt
#     also this *type must be bofore **categories"""
#
#     print(kind)
#     for type in types:
#         print("This is the type of the cake: ",types)
#
#     print("-" * 40)
#
#     for cat in categories:
#         print(cat, " : ", categories[cat])
#
# chesse_shop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))


def make_increment(n):
    return lambda x: x + n

f = make_increment(9)
print(f(1))

