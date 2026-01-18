# using the pass statement in the if loop
# it is a null noting happens, it's used when you don't want to wrtie anything inside the if block
haha = 80
ahah = 90
if haha == ahah:
    pass #this is where a pass is placed

#example
a = 40
if a <  18:
    pass #TODO: add underage logic
else:
    print("access granted")

#example
value = -40
if value <=0:
    print("negative number")
elif value == 0:
    pass #no action is required
else:
    print("its a positve number")

# using pass keyword in different scenarios
def hello():
    pass #TODO: implement the logic for discount
# functioin exits but doesn't do anything
hello() 
