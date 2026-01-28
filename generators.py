# Generators are the functions that can pause and resume theirexecution
# when a generator function is called it returns a genenrator object, which is an iterator 
# the code inside the fucntion is not executed yet, it is only compiled. the function only executes when you iterate over the generator 

def gen():
    yield 1
    yield 2
    yield 3
for values in gen():
    print(values)

# generator allows you to iterator over the data without storing the entire dataset in memory
# instead of using return, generator uses the yeild keyword
# the yeild keyword is what makes a function a generator

# yeild is encountered, th function's state is saved and the value is returned. 
# The next time generator is called it will continue from where it left out earlier

# generator that yeilds the numbers
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(5):
    print(num)
