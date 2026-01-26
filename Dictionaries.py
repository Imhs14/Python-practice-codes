# creating a dictionary
car ={ "brand": "honda",
      "model": "city",
      "year": 2025,
      "new": True #bool and numerics don't need to be in the quotes.
    }
print(car)
print(car["brand"]) 

"""When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index."""

# duplicates are not allowed take an example
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)"""
print(len(car))
print(type(car))
#using the constructor
watch = dict(brand = "seiko", model = "submariner", dialsize = "39mm", moment = "automatic", new = True)
print(watch)
# Accessing the Specific item
print(watch["brand"])
print(watch.keys()) # gives the key values with their values.
watch["moment"] = "quartz"
print(watch)
#{'brand': 'seiko', 'model': 'submariner', 'dialsize': '39mm', 'moment': 'quartz', 'new': True}

#to get the values
print(watch.values())

# to add more items value to the dictionary
car["color"]= 'red'
print(car)

#item() will return each item in a dictionary in a tuple or a list.
v = watch.items()
print(v)
#dict_items([('brand', 'seiko'), ('model', 'submariner'), ('dialsize', '39mm'), ('moment', 'quartz'), ('new', True)])
watch["price"]= 100000
#after the change
print(v) 
# Adding items to dictionary
watch["moment"] = "automatic"
print(watch)
watch.update({"brand":"tissot"})
print(watch)
#o/p: {'brand': 'tissot', 'model': 'submariner', 'dialsize': '39mm', 'moment': 'automatic', 'new': True, 'price': 100000}

# Removing the items from the dictionary
# First using th pop()
watch.pop("new")
print(watch)

# popitem() removes the last added item to the dictionary
print(car) # let's compare & see before we popitem
car.popitem()
print(car) #after the operation we will know what was removed
"""{'brand': 'honda', 'model': 'city', 'year': 2025, 'new': True, 'color': 'red'}
{'brand': 'honda', 'model': 'city', 'year': 2025, 'new': True}"""

mobile = {"brand" : "Oneplus", 
           "model" : "Nord CE5",
           "RAM" : 8,
           "storage" : 128+64,
           "color" : "Nexus Blue"
           }
print(mobile)



# demonstration of del & clear() item
del mobile["color"]
print(mobile)

icecream = {"brand" : "Amul",
            "type" : "cup",
            "flavour": "choco Brownie",
            "price" : 35,
            "place" : "India"}

icecream.clear()
print(icecream)



# using del to delete the dictionary
del icecream



#Loops in the dictionaries

for x in mobile:
    print(x)

# for printing the specific value from the dictionary
for brand in mobile:
    print(mobile["brand"])
    
    #using the values() returns all the values in a dictionary
    for brand in mobile.values():
        print(brand)
# using the keys() returns the all the keys in the dictionary
for x in mobile.keys():
    print(x)
# using the items() return key and its values
for x,y in mobile.items():
    print(x,y)
h = {"brand" : "Oneplus", 
           "model" : "Nord CE5",
           "RAM" : 8,
           "storage" : 128+64,
           "color" : "Nexus Blue"
           }
# demonstrating the copy a dictionary
apple = h.copy()
print(apple)
#  using dict() taking a variable and copying items from the 1 dictionary and making another with different name
apple = dict(h)
print(apple)
