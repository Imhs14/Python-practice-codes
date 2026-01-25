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