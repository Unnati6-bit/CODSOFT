num1=float(input("enter the first number::"))
num2=float(input("enter the second number::"))
print("eneter 1 for addation\n enter 2 for subtraction\n enter 3 for multiplication\n enter 4 for divsion")
choice=int(input("enter your choice between 1-4::"))
if choice==1:
    print("sum of numbers::",num1+num2)
elif choice==2:
    print("subtraction of numbers::",num1-num2) 
elif choice==3:
    print("multipication of numbers::",num1*num2)
elif choice==4:
    print("division of number::",num1/num2)
else:
    print("please enter correct choice between 1-4")
print("thankyou for using calculator")                   

