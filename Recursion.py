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

# Fibonacci sequence using recursions

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
print(fibo(7))      
#O/P: 13  


# using recursions to add all the elements of a list 
def sumlist(num):
    if len(num) == 0:
        return 0
    else:
        return num[0]  + sumlist(num[1:])
mylist =[13,43,532,532,5533,887,642,632]    
print(sumlist(mylist))    

# Finding maximum value in a list
def findmax(num):
   if len(num) == 1:
       return num[0]
   else:
       maxrst = findmax(num[1:])
       return num[0] if num[0] > maxrst else maxrst

mylist = [1223,45,78,89,56,78,55,88,44,67,445]  
print(findmax(mylist))

# Recursion in depth 
# python has the limit how deep recursion can go usually it is 1000 recursive calls
# checking the recursive limit

import sys
print(sys.getrecursionlimit())

#O/P : 1000

# you can set higher recursion limits but be careful as this can cause crashes:
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

#O/P : 2000

# Increasing the recursion limit should be done with caution. 
# For very deep recursion, consider using iteration instead.