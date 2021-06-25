# Program make a simple calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def multiply(x,y):
    return x*y
def square(x,y):
    return x**y
print("1.addition:")
print("2.substrate:")
print("3.division:")
print("4.multiplication:")
print("5.square:")
operator=float(input("enter which operation do u want apply:"))
if operator>5:
    print("operator is out of range")
print("operator")
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
if operator==1:
    print(add(num1,num2))
elif operator==2:
    print(sub(num1,num2))
elif operator==3:
    print(div(num1,num2))
elif operator==4:
    print(multiply(num1,num2))
elif operator==5:
    print(square(num1,num2))
else:
    print("entered wrong input")