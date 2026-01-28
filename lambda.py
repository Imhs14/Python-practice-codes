# The lambda function is small anonymous function
# syntax lambda argument: expression 
# lambda can take any number of arguments but only 1 expression
x = lambda a : a+15
print(x(5))

# giving 2 arguments 
v = lambda a,b : a+b
print(v(5,6))
 
 # using 3 arguments 
y = lambda a, b, c : a*b+c
print(y(4, 5, 3))

def myfunc(n):
    return lambda a: a*n

result = myfunc(2) # this goes to the function n
print(result(11)) # this goes to the lambda function a

# by using the sorted to sort a list's items
words = ["apple","banana","Mexico", "daytona"]
result = sorted(words, key = lambda x : len(x))
print (result)

# you can also do this send both the functions at the same time
def fx(n):
    return lambda a :a *n
result1 = fx(2)
result2 = fx(3)
print(result1(11))
print(result2(11))

# Use lambda functions when an anonymous function is required for a short period of time.

# usually the lambda function is used in built-in functions like
# map(), filter(), sorted()

# using lambda with map()
# the map() function applies a function to every item in an iterable:


number = [1,2,3,4,5,5,6,6,67,]
double = list(map(lambda x : x * 2 , number))
print(double)
#[2, 4, 6, 8, 10, 10, 12, 12, 134]

# using the lambda with filter()
# The filter() fun created a list of items for which a function returns True :
# it returns the values which satifies them 
numbers = [1,124,24,24,2,43,23,9,23,123,4,1239]
odd_num = list(filter(lambda x : x % 2 != 0 , numbers))
print(odd_num)

#[1, 43, 23, 9, 23, 123, 1239]

# using the sorted()
# The sorted function can use a lambda as a key for custom sorting
students = [("abc",89),("gsa",34),("sfa",32)]
sorted_students = sorted(students,key=lambda x:x[1])
print(sorted_students)

# [('sfa', 32), ('gsa', 34), ('abc', 89)]
# got sorted based on the numbers that we gave as the inputs

#example
students1 = [("roll1",21),("roll2",2),("roll3",73),("roll21",96)]
sorting = sorted(students1, key= lambda x:x[0] ) # here only 1, 0 can be entered 1 sorts it , 0 doesn't sorts it , gives the data as it is.
print(sorting)

