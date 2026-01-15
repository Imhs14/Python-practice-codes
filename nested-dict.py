myfamily = {
    "child1" : {
        "name" : "heera",
        "year" :2005,
        "gender" : "male"
        },
    "child2" : {
        "name" : "shanker",
        "year" : 2002,
        "gender" : "male"
    },
    "child3" : {
        "name" : "girl",
        "year" : 1995,
        "gender" : "female"
    }
}
print(myfamily)

# Creating a new nested dict
# giving the internal items to it.

child4 = {
  "name" : "Emil",
  "year" : 2004
}
child5 = {
  "name" : "Tobias",
  "year" : 2007
}
child6 = {
  "name" : "Linus",
  "year" : 2011
}
#after the data is given 
# lets connect the upper data to a dictionary i.e a nested dictionary

fam2 = {
    "child4" : child4,
    "child5" : child5,  
    "child36" : child6
}
print(fam2)
 
 #Accessing the items of nested dictionary

print(fam2["child4"]["year"])
print(myfamily["child1"]["name"])

#You can loop through a dictionary by using the items() method like this:
for x, obj in fam2.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
"""Loop 1: for x, obj in myfamily.items():
What it does: It opens the "File Cabinet" (myfamily).

x: Grabs the label on the drawer (e.g., "child1").

obj: Grabs the entire dictionary sitting inside that drawer (e.g., {"name": "Emil", "year": 2004}).

Why we need it: Without this loop, Python wouldn't know which child's information you want to look at.

Loop 2: for y in obj:
What it does: It looks inside the drawer we just opened (obj).

y: Grabs the keys inside that specific child's dictionary (e.g., "name", then "year").

obj[y]: Grabs the actual value (e.g., "Emil", then 2004).

Why we need it: Since you don't know exactly how many pieces of information are inside the "child" dictionary (maybe some have "school" and others don't), this loop goes through every single detail one by one.

What happens if you only use ONE loop?
If you only use the first loop, you can't see the "inner" details easily"""