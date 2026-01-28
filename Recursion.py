# recursion means a function calls it self, but you have to be very careful while using the recursion
# that means a function calls itself  which can be very helpful to loop through the data and get the result

def countdown(n):
    if n<0:
        print("done")
    else:
        print(n)
        countdown(n-1)
countdown(5)


"""Base Case and Recursive Case
Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error."""

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))            
