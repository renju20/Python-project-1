x=int(input("Enter first number"))
y=int(input("Enter second number"))
t=int(input("Enter third number"))
if x>y and x>t:
    print(f"{x} is largest")
elif y>x and y>t:
    print(f"{y} is largest")
else :
    print(f"{t}is largest")