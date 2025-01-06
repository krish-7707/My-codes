num1=10
print("g variable num1 =",num1)
def func(num2):
    print("In function - local variable num2 = ",num2)
    global num3
    num3 =30
    print("in function - local variable num3= ",num3)
print(num3)
func(20)
print(num1)