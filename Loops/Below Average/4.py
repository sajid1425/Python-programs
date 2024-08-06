# Write a Python Program to Print sum of natural numbres upto n
n=int(input("Enter any number : "))
i=1
sum=0
while i<=n:
    print(i)
    sum+=i
    i+=1
print("The sum is",sum)