def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select operation")
print("1.Add")
print("2. Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice=input("Enter choice")
    if choice in("1","2","3","4"):
        num=float(input("Enter first number"))
        num1 =float(input("Enter second number"))
        if choice =="1":
            print(num,"+",num1,"=",add(num,num1))
        elif choice =="2":
            print(num,"-",num1,"=",subtract(num,num1))
        elif choice == "3":
            print(num, "*" ,num1,"=", multiply(num,num1))
        elif choice =="4":
            print(num,"/",num1,"=",divide(num,num1))
            break
        else:
            print("Invalid Input")

