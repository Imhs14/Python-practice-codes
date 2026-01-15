mobile = {"brand" : "Oneplus", 
           "model" : "Nord CE5",
           "RAM" : 8,
           "storage" : 128+64,
           "color" : "Nexus Blue"
           }
# demonstrating the copy a dictionary
apple = mobile.copy()
print(apple)
#  using dict() taking a variable and copying items from the 1 dictionary and making another with different name
apple = dict(mobile)
print(apple)
