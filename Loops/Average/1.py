# Write a Python program to print sum of odd numbers upto n
n=int(input("Enter any number : "))
i=1
count=0
while i<=n:
    if i%2!=0:
        count+=i
    i+=1
print("The sum of Odd numbers is ",count)