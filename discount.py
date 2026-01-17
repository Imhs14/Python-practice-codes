age = "22"
student = False
discount = True
if (age>='18' or age<='25') and student or discount:
    print("discount applies")

# you can also use the parentheses for having a clarity
temperature = 40
raining = False
weekend = True 
if (temperature<20 and not raining) or weekend:
    print("great day to go out")

#user authentication 
username = "im_hs14"
password = "heera123"
is_verified = True
if username and password and is_verified:
    print('login successful')
else:
    print("invalid user or password")
