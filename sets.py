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