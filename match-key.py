# instead of using the if..else statements you use match
# this match will exceute only once 
# match selects one block out of many blocks to be executed

# demonstrating it's use using week days example

day = 5
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

# default value " _ " after case if you place this
# your code will execute if your input doesn't match

dayout = 8
match dayout:
    case 6:
        print("today is saturday, let's party")
    case 7:
        print("today is sunday, let's go out")
    case _ : #using the default value, it will execute when the above 2 cases will show up an error
        print("looking for the next weeknd")
    
# using the pipe character | as an or operator 
# In the case evaluator we use this to compare more then 1 case options
days = 2
match days:
    case 1 | 2 | 3 | 4 | 5:
        print("it's a weekday")
    case 6 | 7:
        print("it's weekend")

# using the if statement as Guard
# we can add if statement as the extra condition-check

month = input("enter the month:")
weeks = input("enter the days you want to check:")
match dayss:
    case 1 | 2 | 3 | 4 if month <= 6 :
        print("its the ")
    case 1 | 2 | 3 | 4  if month >=7:
        print("its the 2nd half") 