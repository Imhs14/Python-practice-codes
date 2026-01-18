# python has 2 primitive loop commands:
# while loops and for loops
# with the while we can execute a set of statements as long as they are true
i = 1
while i < 6:
    print(i)
    i+=1

print("1st loop executed")
# use of the break statement
# you can stop the loop even when it is true 
# break is used to come out of the loop
a = 1
while a<=5:
    print(a)
    if a == 4:
        break
    a += 1

print("2nd Loop executed")

# using the continue statement 
# with continue statement we can stop the current iteration and continue with the next iteration
b = 0
while b < 6:
    b += 1
    if b == 5:
        continue
    print(b)

print("3rd Loop executed")

#using the else statement in the while loops
c = 0
while c <5:
    c += 1 # never keep 0 here if you kept 0 at the starting point i.e c = 0 
        # it creates a infinite loop and will never get to else block neither will it break out of the while loop
    print(c)
else:
    print("c is no longer less then 5")