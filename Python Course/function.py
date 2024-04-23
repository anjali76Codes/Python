#   Receive -->formal parameters( function definition)
# def add(p,q):  
#     z= p+q
#     print("Addition is :",z)
# x = int(input("Enter the first number:"))
# y = int(input("Enter the first number:"))

#  this will call two times but with same result 
# add(x,y)  // During call --> Actual parameters(function calling)
# add(x,y)


# def add():
#  x = int(input("Enter the first number:"))
#  y = int(input("Enter the first number:"))
#  z = x+y
#  print("Addition is:",z)
#  this will call three times and with  different value( pr we can give different value)
# add()
# add()
# add()


# def fun(x,y,z=0):
#     print(x+y+z)
#     print(y)
    #  This is accroding to positional
# fun(12,3,4)
# fun(12,34)
#  We can give according to us  using Keywords -->
#  And this is done in the order of  the first positional and then keywords(PK)--> here 10 is positional and 23,10 is --> keywords  Or we can give  value to all three using keywords
# fun(10,z=23,y=10)



def fun(*t):
    print(t)
#  if I want to any change in it first I have to convert this tuple into the list cause tuple is immutable 
    li = list(t) 
    print(li)
#  it shows me error cause no argument is pass or  fun function have not any formal parameters
#  To solve this type of error we can use tuple or --> * that acts as a tuple
fun(10,5) 
fun(10,5,4,6,8,9,90) 
fun(10,25,45,67,89,99,11,34,11,22,333,44,55,66,777,88,88,999,77,88,98,76,54,34,22,221,11,1) 
  