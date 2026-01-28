# recursion means a function calls it self, but you have to be very careful while using the recursion
# that means a function calls itself  which can be very helpful to loop through the data and get the result

def countdown(n):
    if n<0:
        print("done")
    else:
        print(n)
        countdown(n-1)
countdown(5)
