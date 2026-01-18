# you can place a if block inside a if block, this is known as nested if statements
x = 14
if x > 10: #outer if statement 
    print("x is above 10")
    if x >20: #inner if statement executes only when outer if is true
        print("x is greater then 20")
    else: # when outer if is true but inner if is false it will be executed
      # for the x<20
        print("not above 20")
else: # when the outer if is false this will be executed 
# for the x<10
    print("x is not even 10")

# checking multiple condtions with nesting
age = 21
legal_to_drive = True
if age>=18:
    if legal_to_drive:
        print("you can ride")
    else:
        print("get your licenses")
else:
    print("not eligible to drive")

# using the nested if statements in different scenarios
score = 80
attendance = 75
submitted = True
if score >= 75:
    if attendance >=75:
        if submitted:
            print("you've passed with good grades")
        else:
            print("you have passed but missing the assignment")
    else:
        print("you have passed but not maintained the attendance")
else:
    print("you've failed, get your parents to meet with your subject teacher")

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