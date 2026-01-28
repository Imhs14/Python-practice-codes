def fdmx(num):
    if len(num) == 1:
        return num[0]
    else:
        mxrst = fdmx(num[1:])
        return num[0] if num[0] > mxrst else  mxrst
lst = [1,3,4,5,6,6,7,6,3,2,2,3,2323,5,23,2,4,24,24,2,2,5,235,235,234,24]
print(fdmx(lst))

def cfx(n):
    count = 1
    while count<=n:
        yield count
        count += 1
for num in cfx(9):
    print(num)