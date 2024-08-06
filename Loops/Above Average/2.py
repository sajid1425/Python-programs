# Write a python program to find sum of digits of given number
n=int(input("Enter any number : "))
sum=0
while n>0:
    i = n%10
    sum+=i
    n/=10
print(sum)