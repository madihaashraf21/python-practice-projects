import random 
'''
snake=1
water=-1
gun=0'''
print("Welcome To Our Snake,Water and Gun Game \n")
computer=random.choice([-1,0,1])
youstr=input("enter your choice(s,g,w): ")
youdict={"s":1 , "w":-1 ,"g":0}
reversestr={1:"Snake" , -1: "Water" , 0:"Gun"}
you=youdict[youstr]
print(f"You choose: {reversestr[you]} \ncomputer choose: {reversestr[computer]}")

if(you == computer):
    print("match draw")

else:
    if(you==1 and computer==-1):
        print("you won :)")
    elif(you==0 and computer==-1):
        print("you lose :(")
    elif(you==-1 and computer==1):
        print("you lose :(")
    elif(you==0 and computer==1):
        print("you won :)")
    elif(you==-1 and computer==0):
        print("you won :)")
    elif(you==1 and computer==0):
        print("you lose :(")
    else:
        print("Something went wrong :|")

print ("    Match Finish ;)")
