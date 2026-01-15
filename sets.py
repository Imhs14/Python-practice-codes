# creatnig the a set
seta={"sports","cars","are","love","bikes","also"}
print(seta)
# when a set has dulpicates
"""Note: The values True and 1 are considered the same value in sets,
  and are treated as duplicates, False and 0 are consdiered as same value as well."""
setb = {"apple", "banana", "cherry", "apple", "banana","True","1","2","False","0"}
print(setb)

#to know the length of set
print(len(setb))

#sets data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(type(set1))
 
# can use the set() constructor to make a set
set4 = set(("apple", "banana", "cherry")) # note the double round brackets
print(set4)

#Accessing items in a set.
for x in set4:
    print(x)

#check if any item is present in the set or not
print("banana" in set4)
print("hello" not in set4)

#add items to sets
set4.add("orange")
print(set4)

#update() adding 2 or more sets together
set4.update(set3) 
#set4 being upadted by adding the set3 items to it 
print(set4)

#you can add any iterable items to the set using update 
#it can be a list, tuple, dictionary etc
list1 = ["manogo","grapes","mind"]
set9 = {"avengers","superman","batman"}
set9.update(list1)
print(set9)
# removing items from the set
a = {"hello","hola","namaste","bonjour"}
a.remove("hola")
print(a)
# discard 
a.discard("bonjour")
print(a)
# using the pop() operation
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

#The return value of the pop() method is the removed item.


m = a.pop()
print(m)

#using of the clear operation
#this clears out the whole set but the set still exists
v = {"one","two","three","four"}
v.clear()
print(v)
 
# del operation is being used 
b = {"red","blue","green"}
del b
# print(b) # this will raise an error because the set b no longer exists
# loops in sets
setx = {"apple", "banana", "cherry"}
for x in setx:
    print(x)
""" join sets
 There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""
setk = {"methods","are","fun","apple"}
setl = {"fruits","are","good","for","health"}
setm = setk.union(setl)
setn = setk.update(setm)
# using of seta | setb way of joining the sets
o = {"red","blue","green"}
p = { "black","white","yellow","voilet"}
q = o| p 
print(q)
# you can also add multiple sets together 
r = setk | set1 | setl
print(r)
"""You can use the & operator instead of the intersection() method,
and you will get the same result."""
 #using of intersection() method
setu = {"apple", "banana", "cherry"}
setv = {"google", "microsoft", "apple"}
setz = setu.intersection(setv)
print(setz)
# use of the & operator
setaa = set1 & set2
print(setaa)

"""The intersection_update() method will also keep ONLY the duplicates,
but it will change the original set instead of returning a new set."""
k = {"python","java","c++","ruby","javascript","r"}
l = {"python","c++","swift","go","kotlin"}
l.intersection_update(k)
print(l)

#symmetric_difference() method or either use this or the ^ operator
# returns a set that contains all items from both sets, expect which are commoon in both sets
setc = {"apple", "banana", "cherry"}
setd = {"google", "microsoft", "apple"}     
sete = setc.symmetric_difference(setd)
print(sete)

#using difference() operator
setf = {"apple", "banana", "cherry"}
setg = {"google", "microsoft", "apple"}
seth = setf.difference(setg)
print(seth) #prints what is commoon in the both sets in a new set.
# using of - operator
setvv = setf - setg
print(setvv)
# difference_update() method
# removes tje common items fromt the both the sets and updates the set with the first set'sitems in it 
sety = {"apple", "banana", "cherry"}
setz = {"google", "microsoft", "apple"}
sety.difference_update(setz)
print(sety)

#use of symmertric_difference_update() method
#method to keep the item that are not present in both sets
sett = {"apple", "banana", "cherry"}
set = {"google", "microsoft", "apple"}

sett.symmetric_difference_update(sett)

print(sett)

# o/p:{'google', 'banana', 'microsoft', 'cherry'}