loop = True
from math import sqrt
while loop == True:
    operation = input("What is the operation symbol:")
    x = float(input("What is the first number:"))
    y = float(input("What is the second number or 0 if square root:"))
    if operation == "+":
        print (x,operation,y,"=",x+y)
    elif operation == "-":
        print (x,operation,y,"=",x-y)
    elif operation == "/":
        if y == 0 :
            print ("you cannot divide by zero")
        else :
            print (x,operation,y,"=",x/y)
    elif operation == "*":
        print (x,operation,y,"=",x*y)
    elif operation == "**":
        print (x,operation,y,"=",x**y)
    elif operation == "sq2" :
        print (x,operation,"=",sqrt(x))