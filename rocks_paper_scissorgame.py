import random

print("--------Rock,Paper,Scissor Game-------")
emoji={'r':'🪨','s':'✂️' ,'p':'📝'}
choice=('r','p','s')
while True:

    user_input=input("Rock,Paper,Scissor(r/p/s): ").lower()
    if user_input not in choice:
        print ("Invalid option ")
        continue

    comp_input=random.choice(choice)

    print(f"You choose: {emoji[user_input]}")
    print(f"computer choose: {emoji[comp_input]}")

    if (user_input==comp_input):
        print("Match Tie")

    elif((user_input=='r' and comp_input=='p') or(user_input=='p' and comp_input=='s')
          or (user_input=='s' and comp_input=='r')):
        print("You loss ")

    elif(user_input=='r' and comp_input=='s') or(user_input=='p' and comp_input
    =='r') or (user_input=='s' and comp_input=='p') :
        print("You Win ")


    more_continue=input("Do you want to play more(y/n): ").lower()
    if (more_continue=='y'):
        continue
    elif(more_continue=='n'):
                print("thanks for playing ")
                break
    else:
                print("Enter valid choice")
    
