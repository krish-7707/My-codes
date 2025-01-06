x=int(input("enter the no 1 ="))
y=int(input("enter the no 2 ="))
z=int(input("enter the no 3 ="))
if(x <= y and x <= z):
    print(x, "is the smallest")
 
elif(y <= x and y <= z):
    print(y, "is the smallest")
else:
    print(z, "is the smallest")