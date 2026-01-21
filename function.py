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

# positional arguments.
def lol(subject, faculty):
    print(subject," is taught by",faculty)
    print(faculty, subject)
lol("atcd", "buddy")
lol("heera","phy") # this is called the positional arguments,
# in this way you no need to specify the namme or faculty key and its items in functions

# mixing the positional and keyword arguments
