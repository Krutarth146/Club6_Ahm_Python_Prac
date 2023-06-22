# Decorators --->

# decorator is First Class Object

# Function have Inner Functions

# It takes function as a Argument

def fun1():
    print("Inside fun1")

def fun2(f):
    print("Inside fun2")
    f()


# fun2(fun1)
# Inside fun2
# Inside fun1
print()
f = fun1
print(type(f))   # <class 'function'>

f()   # Inside fun1
print()
fun2(f)

# Inside fun2
# Inside fun1


# --------------------------------------------

def fun5(f):
    def innerfun():
        print("Henish")
        f()

    return innerfun

@fun5   # Decorator
def fun6():
    print("Mahhir")


# fun = fun5(fun6)
fun6()

# Henish
# Mahhir