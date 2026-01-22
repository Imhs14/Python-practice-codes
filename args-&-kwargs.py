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