print("--------LCM OF TWO NUMBERS-----------")
a=int(input("Enter first number: "))
b=int(input("Enter Second number: "))

MaxNum=max(a,b)

while(True):
    if(MaxNum%a==0 and MaxNum%b==0):
        break
    MaxNum+=1;

print(f"The LCM of two number {a} and {b} is {MaxNum}")
    

