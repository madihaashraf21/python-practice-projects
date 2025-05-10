import random

print("--------Dice Rolling Game--------")
while True:
    a = input("Do You want to Roll the Dice(Y/N): ").lower()
    if(a=='y'):
        die1=random.randint(1,10)
        die2=random.randint(1,10)
        print(f"({die1},{die2})")
    
    elif a=='n':
        print("Thanks for playing ")
        break
    else:
        print("invalid choice")

print("Hope you enjoyed :)")

