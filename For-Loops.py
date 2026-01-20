a = ["heera","shanker","malathkar","name"]
for x in a:
    print(x)

# we can loop through even a string as they have a sequence of indexing
for x in "heera":
    print(x) 

# using the break in the for loop
fruits = ["apple","banana","cherry","watermelon","orange"]
for x in fruits:
    print(x)
    if x == "watermelon":
        break

# using the Continue statement
b = ["apple","banana","kiwi","orange"]
for x in b:
    if x == "kiwi": # kiwi will be skipped, 
        continue
    print(x)

tuple1 = ("hello","how","are","you","haha")
for x in tuple1:
    if x == "are":
        continue
    print(x)
 
 # usn=ing the range 
"""o loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""
for x in range(6):
    print(x)
# prints 0-5 vertically

# using range(6, 30, 6)
# usually range increments by 1, but in this case we specify the starting point, end point, increment by 1 or any number that we want
for x in range(6, 31, 6):
    print(x)
""" 6
    12
    18
    24
here the starting point is 0 in counting the range"""
# using the else block
for x in range(5, 50, 5):
    if x == 45:
        print(x)
else:
    print("process finished")
# the else block does't exceutes when the above conditions fails
# it executes when the above process is compeleted.

# using the break in the for loop
# if the condition satisfies then the else block code will not execute
for x in range(5, 50, 5):
    if x == 45: break
    print(x)
else:
    print("process finished")

# nested for loops
# The "inner loop" will be executed one time for each iteration of the "outer loop":

a = ["heera", "shanker", "malathkar"]
b = ["one", "two","three"]
for x in a:
    for y in b:
        print(x,y)

# using the pass keyword
for x in ["apple","orange","mango","watermelon"]:
    pass
