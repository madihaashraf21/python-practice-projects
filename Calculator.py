print('MINI CALCULATOR ')

num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))

print("OPERATION \n 1.add   \n 2.Subtract \n 3.multiply \n 4.Divide")

enter=int(input ("Enter your choice(1-4): "))
if(enter ==1):
    print("The addition of two number is: ",num1+num2)

elif(enter==2):
   print  ("The Subtration  of two number is: ",num1-num2)

elif(enter==3):
   print  ("The Multiplication of two number is: ",num1*num2)

elif(enter==4):
   print  ("The Division  of two number is: ",num1/num2)

else:
    print("invalid operation :(")

    print("Operation Completed ")

