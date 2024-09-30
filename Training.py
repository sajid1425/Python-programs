import random
# x=input("Enter Your Name : ")
# while True:
#     y=random.randint(1,100)
#     print("What is square of ",y)
#     n=int(input())
#     if n==0:
#         break
#     if pow(y,2)==n:
#         print("Correct")
#     else:
#         print("Incorrect") 

while True:
    y=random.randint(1,100)
    x=y*y
    print("What is squareroot of ",x)
    n=int(input())
    if n==0:
        break
    if n==y:
        print("Correct")
    else:
        print("Incorrect")       
