import random

print("--------Number Guessing Game--------")
num_guess=random.randint(1,101)
while True:
    try:
        guess=int (input("Guess the number between one and hundred: "))
        if(guess<num_guess):
            print("TOO LOW! ")
        elif guess>num_guess :
            print("TOO HIGH")
        else:
            print("CONGRATULATIONS! YOU SUCCEEDED")
            break

    except ValueError:
            print("Enter valid number")
    
print("Thanks for playing!!!")


