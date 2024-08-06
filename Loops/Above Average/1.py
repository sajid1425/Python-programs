# Write a python program to check the entered number is prime or not
n=int(input("Enter any number : "))
f=False
i=1
for value in range(2,n):
    if n%i ==0:
        flag=True
        break
if flag:
    print("Number is not a prime number")
else:
    print("Number is prime")
    