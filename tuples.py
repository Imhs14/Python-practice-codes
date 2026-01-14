#creating a tuple and accessing its items
tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[1])
print(tuple1[2:5]) #2 included and 5 not included
print(tuple1[:5])
print(tuple1[-1])
print(tuple1[3:])
print(tuple1[-1:-5]) #RANGE OF TUPLES STARTED 
#to check if a items exists
if "apple" in tuple1:
    print("its there")
else :
    print("it doesn't")
 # to change a tuple's item value we can convert it a list
 #list can be changed and then convert it back to tuple.

a = tuple(("hello", "world","python","java","c++"))
b = list(a)
b[1]= "whatssapp" # adding items to list
b.append("instagram")
b.remove("c++") # removing items from list
a= tuple(b) # converting list back to tuple
print(a)

# adding tuple to another tuple
c= ("apple", "banana", "cherry")
d= ("orange",)
c += d  
""" 1:Before: The name c tuple points to Address A, where the values ("apple", "banana", "cherry") live.

The Operation: Python creates a new set of values ("apple", "banana", "cherry", "orange") at Address B.

After: The name a tuple is updated to point to Address B.

Result: Address A is now "empty" because nothing is pointing to it anymore, so Python automatically deletes it to save memory. """
print(c)

#to Delete a tuple entirely
e= ("apple", "banana", "cherry")
del e 

# print(e) # this will raise an error because the tuple e no longer exists

#packing and unpacking of tuples
#packing 
g = ("apple", "banana", "cherry","promogranate","kiwi")
#unpacking  FEW ITEMS
(apple,banana,cherry,*others) = g #if you want to unpack just a few use *others at the end
print(apple)
print(banana)
print(cherry)
 
 #unpacking all items 

f = ("apple", "banana", "cherry","promogranate","kiwi")
(apple,banana,cherry,promogranate,kiwi) = f #
print(apple)
print(banana)
print(cherry)
print(promogranate)
print(kiwi)
#looping in the tuple
# using the for loop
k=("apple", "banana", "cherry")
for x in k:
    print(x)

ab=("apple", "banana", "cherry")
for i in range(len((ab))):
    print(ab[i])

#using the zip() in for loop
thistuple = ("apple", "banana", "cherry")
price=("100","200","300")
"""The zip() function takes multiple tuples and "zips" them together like a zipper, 
pairing the first items together, then the second, and so on."""
for thistuple,price in zip(thistuple,price):
  print(f"the {thistuple} price is {price}")

# use of range() & len() in loop helps print each items according to its indexes
C=("apple", "banana", "cherry")
for i in range(len(C)):
    print(C[i])

#use of for loop in tuples
L = ("apple", "banana", "cherry")
while i<len(L): #len()< the tuple 
   print(L[i]) 
   i = i + 1

#joining of two tuples
tuple3 = ("going","down","for","real")
tuple4 = ("lets","do","some","awwesome","stuff") 
tuple5 = tuple3 + tuple4 
# adds tuple3 and tuple4
tuple6 = tuple3*3 
# multiples the tuple3 3 times 1 
print(tuple4)
print(tuple6)
print(tuple5)

#tuple methods
#count -> Returns the number of times a specified value occurs in a tuple
x=(1,2,3,4,2,5,2)
y = x.count(2) #counts how many times apartaicular item is repeated in the tuple
print(y)

#index()
h=("hello","world","hello","python","hello")
z = h.index("python") #gives the index of the item thats in the bracket of index()
print(z)