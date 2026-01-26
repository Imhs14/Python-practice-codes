# It let's you add the extra behaviour to the function W/O changing the Function's code
""" it is a function that takes another function as input and returns a new function """
def casechanger(func):
    def myinner():
        return func().upper()
    return myinner 
@casechanger
def myfunc():
    return "hello heera"

print(myfunc())

# when @decorator_name i.e case changer is detected by the python
# it does this job i.e myfunc = casachanger(myfunc) myfunc is passed to the casechanger function first then
# now myfunc returns the "hello heera" to the case changer as input
# next as the casechanger gets the input from the myfunc it gives the inner function i.e my inner
# next as myfunc passes the "hello heera" it returns the "hello heera" by apply uppercase to it
# return myinner will return it self 

def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def func1():
    return "hello shanker"
print(func1())

@changecase
def func2():
    return "hi what is your name"
print(func2())

# Arguments in the decorator Function
def case(func):
    def innerr(x):
        return func(x).upper()
    return innerr
@case
def funcc1(nam):
    return "hello" + nam
print(funcc1(" heera"))

# using the *args and **kwargs
"""Sometimes the decorator function has no control over the arguments passed from decorated function,
 to solve this problem, add (*args, **kwargs) to the wrapper function, 
this way the wrapper function can accept any number, and any type of arguments,
 and pass them to the decorated function."""

def args(func):
    def inner1(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return inner1
@args
def decorator(name):
    return "hello" + name
print(decorator(" tony stark"))

# example 

def my_decorator(func):
    # This wrapper can now accept anything you throw at it
    def wrapper(*args, **kwargs): 
        print("Logging: Function is about to run...")
        
        # We unpack the arguments back into the original function
        result = func(*args, **kwargs) 
        
        print("Logging: Function finished.")
        return result
    return wrapper

@my_decorator
def add_numbers(a, b):
    return a + b

# This works perfectly now!
print(add_numbers(5, 10))

# Decorator with Arguments
# decorator can accept their own arguments by adding another wrapper level

def decorator(func):
    def wrapper(*args, **kwargs):
        print("good Morning")
        result = func(*args, **kwargs)
        print(result)
        print("thanks for using this code")
    return wrapper
@decorator
def func1(x):
    return "hello" + x
func1(" heera")
# good morning and thanks for using is what decorator does nd is mostly used for such type of codes
"""good Morning
helloheera
thanks for using this code"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Good Morning")
        result = func(*args, **kwargs)
        print(result)
        print("Thanks for using this code")
        return result
    return wrapper


@decorator
def func1(name, info):
    age = info.get("age", "Unknown")
    return f"Hello {name}, your age is {age}"


func1("heera", {"age": 56})

# decorator with argument

def changecase1(n):
    def decorator12(func):
        def myinner1():
            if n == 1 :
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner1
    return decorator12 # always align the return or the function call below it
@changecase1(3)
def myfunc():
    return "hello heera"
print(myfunc())

# Example 

def case(n):
    def dec(func):
        def inn():
            if n == 1:
                return func().upper()
            else:
                return func().lower()
        return inn
    return dec
@case(1)
def ssup():
    return "hiiiii"
print(ssup())

@case(2)
def sped():
    return "iam speed"
print(sped())

# using multiple decorator on top of one function

def dec0(n):
    def dec1(func):
        def inner(*args,**kwargs):
            if n == 1:
                return "Hello" + func(*args,**kwargs) + "have a great day"
            elif n == 2:
                return "Hello" + func(*args,**kwargs) + "have good evening"
            else:
                return "Hello" + func(*args, **kwargs) + "have a great night"
        return inner
    return dec1


def dec01(func):
    def inn1():
        return func().upper()
    return inn1
@dec0(2)
@dec01
def funcc():
    return " Heera "
print(funcc())
