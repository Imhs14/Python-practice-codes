def case(n):
    def dec(func):
        def inn():
            if n == 1:
                return func().upper()
            else:
                return func().lower()
        return inn
    return dec
@case(1)
def ssup():
    return "hiiiii"
print(ssup())

@case(2)
def sped():
    return "iam speed"
print(sped())

# using multiple decorator on top of one function

def dec0(n):
    def dec1(func):
        def inner(*args,**kwargs):
            if n == 1:
                return "Hello" + func(*args,**kwargs) + "have a great day"
            elif n == 2:
                return "Hello" + func(*args,**kwargs) + "have good evening"
            else:
                return "Hello" + func(*args, **kwargs) + "have a great night"
        return inner
    return dec1


def dec01(func):
    def inn1():
        return func().upper()
    return inn1
@dec0(2)
@dec01
def funcc():
    return " Heera "
print(funcc())