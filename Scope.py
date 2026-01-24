# The scope is only availabe from inside the region it is created. This is called Scope
# Local Scope
def Lcl():
    x = 40
    print(x)
Lcl()

#Function inside the Function
def lcl():
    x = 90
    def inner():
        print(x)
    inner()
lcl()

# Global Scope
# whatever you declare here will be available throught the global and local Scope
x = "iam the global scope"
def outer():
    print(x)
outer()
#O/P: iam the global scope

# naming variable
""" When you operate with the same variable inside and outside the functions then they are treated as two seperate variable.
global variable is different and local variable is different  """

# global keyword
def myfun():
    global x
    x = 400
myfun()
print(x)
y = 80
print(x+y)

# using global key word
x = 200
def globe():
    global x
    x = 300
globe()  
print(x)  #changes made in local using global keyword will change value of the variable globally too

#using non local keyboard 
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x # using the nonlocal variable will make the x belong to the outer function, in short it's valid with in the functions
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

"""The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:
Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace"""

x = "globel"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("inner:",x)
    inner()
    print("outer:", x)
outer()
print("globel:",x)

""" O/P: inner: local
outer: enclosing
globel: globel """

