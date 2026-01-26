# Arbitrary Arguments *args
def fam(*kids): 
    print("the youngest child is",kids[0])

fam("bob","danny","tony","thor") #out of these 4 the specified kids[0] will be printed according to the postion
#the youngest child is bob

# *args is a keyword that allows to accept any number of positional arguments
# accessing the individual arguments
def acc(*args):
    print("Type:",type(args))
    print("first argument:",args[0])
    print("second argument:",args[1])
    print("third argument:",args[2])
    print("all arguments:",args) # you can either write just args or use string slicer [0:3]. both works just fine
acc("tony","stark","thor","captain")

#using *args with regular arguments
def cars(company,*models): 
    for model in models:
        print(company, model)
cars("BMW","M5","M2","GT","i8") 
""" o/p:BMW M5
        BMW M2
        BMW GT  """
# as you can see that the company is printing for every model of company. bcs *args allows you to print number of arguments

# practical example with *args
def adding(*numbers):
    total = 0 #initializing the total
    for num in numbers: #loop for adding each number given as arguments
        total += num # sum total = total + num
    return total #always align return with the for keyword else it won't work properly
print(adding(1, 2, 3, 4, 5))
print(adding(9, 8, 7, 6, 5, 4))

# finding the maximum number

def max(*numbers):
    if len(numbers) == 0: # checks the length of the numbers parameter
        return None # returns 0 if there's nothing
    max_num = numbers[0] # making the 1st element as our max_num
    for num in numbers: # comparision loop starts for the numbers -> arguments i.e integers are compared
        if num > max_num: # if the current num is > then the initialized number then change cur no to max_num
            max_num = num # changing happens
    return max_num #returns the max_num after completion

print(max(2,4,5,6,7,218,12)) # print statements is imp bcs return will only return the values but it won't print

# **kwargs
def kwargs(**kids):
    print('the kid names are '+kids["fname"]+" "+kids["mname"]+" "+ kids["lname"])
# the arguments  ["fname"] like strings we are passing the arguments and then we are defining the arguments in the function call
kwargs(fname = "heera" , mname = "shanker", lname = "malathakar" )

# using **kwargs as the regular arguments

def login(username, **passwords):
    print("give the username", username)
    print("the password is", passwords["characters"])
    for key, value in passwords.items():
        print(" ", key + ":", value)

login("imhs14",characters = "A-Z", speacial_characters = "@#$%&*", numbers = "0-9")
"""
O/P : give the username imhs14
the password is A-Z
  characters: A-Z
  speacial_characters: @#$%&*
  numbers: 0-9"""

# Example-2
def cars(company, **models):
    print("The car brand is", company)
    for key, value in models.items():
        print(" ",key+" : ",value)
cars("mclaren",model = "720s", horsepower = 720, color = "orange", price = "$650,000")
cars("mclaren", model = "senna", horsepower = 1000, color = 'racing livery', price = "$1,000,000")
# TypeError: cars() takes 1 positional argument but 5 were given -> gives this error when you don't specify the keys while calling the function
# first word when calling the function goes to company, rest of them goes to model but for it you have to specify the key and it's values else the above error will occur

def bikes(model, *args, **kwargs):
    print("The model is ",model)
    print("postional arguments args",args)
    print("keyword arguments",kwargs)
bikes("GSA","1250","1350", release = 2024,horsepower = "240hp")
""" The model is  GSA
postional arguments args ('1250', '1350')
keyword arguments {'release': 2024, 'horsepower': '240hp'} """

# unpacking the arguments 
# * and ** can be used for unpacking i.e expanding or unpack the list or dictionary into seperate arguments

# using the * to unpack the list
def myfunc(a,b,c):
    return a + b + c
numbers = [1,2,3] # this variable will used while calling the function
result = myfunc(*numbers) # calling the above numbers using *numbers, # Same as: my_function(1, 2, 3)
print(result)

# example 2
def unpack(fname,mname, lname):
    return fname + mname + lname
name = ["heera ","shanker ","Malathkar"]
result = unpack(*name) # before we gave 1 parameter and many arguments, but now we have given many parameters and 1 argument.
print(result)
# O/P: heera shanker Malathkar

# using the ** kwargs
def unpacking(ffname,llname):
    print("Hello",ffname,llname)
person = {"ffname":"emil","llname":"goffer"} # while doing this don't forget to add{} bcs we are adding different things which is only supported by the dictionary
unpacking(**person) # Same as: my_function(fname="Emil", lname="Refsnes")


# *args saves items as tuples 
# **kwargs saves items as dictionary