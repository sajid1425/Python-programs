# Student performance
n=int(input("Enter Percentage of Student : "))
if n>=90:
    print("Excellent Performance")
elif n>=80 and n<90:
    print("Very Good Performance")
elif n>=70 and n<80:
    print("Good Performance")
elif n>=60 and n<70:
    print("Average Performance ")
else:
    print("Poor Performance")