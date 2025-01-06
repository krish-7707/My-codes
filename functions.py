'''def calculator(a,b):
    add=a+b
    print(add)
c=1
d=3
calculator(6,9)'''


def registernames(**names):
    print("your f name and l name ",names["fname"], names["lname"])
    return registernames
x=int(input("enter the no. of employes"))
for i in range (x):
    f2name=str(input("first name"))
    l2name=str(input("last name"))
    registernames(fname=f2name,lname=l2name)
print(registernames)



