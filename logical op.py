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

#combinig the multiple operators
#in this case we are using the and, or, not.
age = 25
is_student = False
has_discount_code = True
if (age<18 or age >65) and not is_student or has_discount_code:
    print("discount applies")