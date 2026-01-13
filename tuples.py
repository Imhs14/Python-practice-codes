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



