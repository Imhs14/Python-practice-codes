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
    if len(numbers) == 0:
        return 0
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(max(2,4,5,6,7,218,12))