# using global key word
x = 200
def globe():
    global x
    x = 300
globe()  
print(x)  #changes made in local using global keyword will change value of the variable globally too

#using non local keyboard 
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x # using the nonlocal variable will make the x belong to the outer function, in short it's valid with in the functions
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

