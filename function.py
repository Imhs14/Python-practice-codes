def fun():
    print("hello said by the function")
fun()
# function helps avoid the code repetation
# converting farenheit to celcius using functions
def f_to_c(farenheit):
    return (farenheit - 32) * 5/9
print(f_to_c(90)) # here only we need to call the function, and that will give you the output.
print(f_to_c(100))

# using the return function
def use_return():
    return "hello from the funtion"
message = use_return()
print(message)
print(use_return())

# using the pass statement
def funcc():
    pass

# Arguments
# you can send the arguments with (key = value) syntax , see example to understand 
def pets(animal, name ):
    print("my", animal+"'s" ,"name is", name)
    print("i have a ", animal)
pets( animal="dog", name="bhaw")
pets( animal="cat", name="moew")

# number of arguments 
"""By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.
"""
def fun1(fname,lname):
    print(fname+" ",lname)
fun1("heera","shanker") # also known as positional arguments 
fun1("shruthi","malathkar") # these are in positional to fname and lname.
fun1("keerthi","malathkar")

# default parameters values

def func(fname = "unknown", lname = "friend"):
    print("hello",fname, lname)
func("heera","shanker")
func("shruthi","malathkar")
func() # this function will take default because no arguments were passed to it.

#example no2
def country( name = "india"):
    print("I am from", name)
country("sweden")
country("uae")
country() # this function call will take the default values.

# positional arguments.
def lol(subject, faculty): # parameter could be of any number but separte them with a comma
    print(subject," is taught by",faculty)
    print(faculty, subject)
lol("atcd", "buddy") # arguments
lol("heera","phy") # this is called the positional arguments,
# in this way you no need to specify the namme or faculty key and its items in functions

# keyword arguments 
# you can send the aruguments in this way -> key = value syntax
def auto(car, horsepower):
    print("My car is",car,"and its horsepower is",horsepower)
auto(car = "buggatti", horsepower = 1600)
auto(car = "rimac", horsepower = 1900)
auto(car="rolls royce",horsepower=1000)
auto(car="mclaren 720s",horsepower=720)

# mixing positional and keyword arguments
def func3(bikemodel, horsepower = 210, company = "BMW"):
    print("bike model is", bikemodel,"its horsepower is",horsepower,"& it is from",company)
func3("gsa 1250",horsepower= 250, company="BMW")
func3("Tiger",800,"triumph")
func3("panigale",horsepower=230,company="ducati")

#passing different data types

def func4(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["apple","mango","pineapple",]
your_fruits = ["watermelon","orange","kiwi","staberry"]
func4(my_fruits)
func4(your_fruits)

# Returning the different data types
def myfun():
    return ["apple","mango","shake"]
fruits = myfun()
for x in fruits:
    print(x)
    # or
print(fruits[0:3])

# postional only arguments
def bikes(name,/):
    return f"hello {name}" # you can either use return in this way
print(bikes("BMW"))
# or
def bikes1(name,/):
    print("that's a",name) # you can use the print statement in this way
bikes1("BMW")

# Keyword only argument
def cars(*, name):
    return f"this is {name}"
print(cars(name="buggatti"))
print(cars(name="mercedes"))
print(cars(name="Mustang"))

# combining the positional and keyword only 
def maths(a,/,*,b, c): #first you have to give positional-only then keyword-only or else it will through an error as / should be ahead of *. vice versa hota hai
    return c- a+b          
print(maths(10,b=20,c=5))