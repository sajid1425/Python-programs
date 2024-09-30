import random
from turtle import delay
name=input("Enter Your Name : ")
print("Welcome to Quiz ",name)
score=0
#Square Root
def sqroot():
    global score
    y=random.randint(1,100)
    x=pow(y,2)
    print("What is squareroot of ",x)
    n=int(input())
    if n==y:
        print("Correct ",end="")
        score=score+1
        i =0
        while i<score:
            print("!",end="")
            i+=1
    else:
        print("Incorrect")
        score=0

#Square
def sr():
    global score
    y=random.randint(1,100)
    print("What is square of ",y)
    n=int(input())
    if pow(y,2)==n:
        print("Correct ",end="")
        score=score+1
        i =0
        while i<score:
            print("!",end="")
            i+=1
    else:
        print("Incorrect")
        score=0

#Calling Random Function
while True:
    rd=random.randint(1,2)
    if rd==1:
        sr()
    else: 
        sqroot()
    if score==3:
        delay(4000)
        print(f"\nCongratulations {name}!! \nYou have won the game")
        break
    opt=input("\nDo you wish to continue [YES/NO] : ")
    if opt.lower()=='no':
        delay(4000)
        print("You Loose !!")
        break