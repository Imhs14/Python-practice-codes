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

