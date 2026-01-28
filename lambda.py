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
