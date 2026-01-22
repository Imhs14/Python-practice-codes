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

