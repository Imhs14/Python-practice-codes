age = 35
if age>=18:
    print("you can vote")
    print("you are legally eligible to vote")
    print('1 vote per person will be recorded')
     # like this you can have multiple statements in the if block
is_logged_in = True
if is_logged_in:
    print("welcome back")

# using the ELif Loops 
a = 20
b = 90
c = 100
if a>=b:
    print("a is greater")
elif c<=a:
    print("b is greater then a ")
elif a==b:
    print("a and b are equal")
elif c>b:
    print("c is greater then b")

 #Only the first true condition will be executed. 
 # Even if multiple conditions are true, Python stops after executing the first matching block.
 
d = 4
if d==1:
   print("its monday")
elif d == 2:
    print("its tuesday")
elif d == 3:
    print("its wednesday")
elif d == 4:
    print("its thrusday")
elif d ==5:
    print("its friday")
elif d == 6:
    print("its saturday")
elif d == 7:
    print("its sunday")

#if-elif-else chain
temperature = 22
if temperature > 30:
    print("it's going to be a sunny day.")
elif temperature <20:
    print("its going to be cold day ahead.")
else:
    print("it's going to be normal day.")

#short Hand If
#when you have only 1 statement you can put if condition and the statement in the same line

n = 30
m = 40
if n<=m: print("yes n is less then the m")

#short hand if-else block

print(m) if m>=n else print("m is low")

# else as fallback

username = "imhs14"
if len(username)>0:
    print(f"welcome, {username}!")
else:
    print("username can't be empty")

#Assign a Value with if.. else

a = 3
b = 5
big = a if b<a  else b

# big is a if b is less then a
# or else b is big .

print("big is", big)
# here we have assigned big variable to the correct big number
# syntax Pattern : variable = value_if_true if condition else value_if_false

#multiple conditions on the one line
s = 8234
t = 7432
print("s") if s<t else print("=") if s == t else print("t") 

# you can do various stuff with multiple condotions on one line

name = "heera"
print("9") if len(name) == 9 else print("6") if len(name) == 6 else print("5 letters") if len(name) == 5 else print("no string")

# ternary operators ## conditional operator a practical example of the ternary operator
# helps to assign and return a value
p = 40
q = 80
max = p if q<p else q 
print("max val", max)
