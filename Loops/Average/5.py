# Write a Python program to find a factorial of given number
n=int(input("Enter any number : "))
fact=1
while n>=1:
    fact*=n
    n-=1
print("Factorial : ",fact)