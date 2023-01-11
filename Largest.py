x=float(input("Enter X\n"))
y=float(input("Enter Y\n"))
z=int(input("Enter Z\n"))
if(x>y) and (x>z):
    largest=x
elif (y > x)and (y > z):
        largest = y
else:
            largest=z
print("The Largest number is",largest)