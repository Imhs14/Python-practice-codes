# Logical operator
"""AND - Returns True if both statements are true
OR - Returns True if one of the statements is true
NOT - Reverses the result, returns False if the result is true
"""
a = 70
b = 90 
if a<b and b>a:
    print("both are true")

#Using the OR operator
if a>b or b>a:
    print("any one is true")

#using the NOT
if not b<a: # give false value so the block inside will be executed.
    print("a is not greater then b")