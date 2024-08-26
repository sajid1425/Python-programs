days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#Append is used to add elements at last of the list
days.append("Sunday")
print(days)
#Iterate through list
for i in days:
    print(i)
#Remove is used to remove the element from the list
days.remove("Saturday")
print(days)
#insert
days.insert(5,"Saturday")
print(days)
# + operator is used to concatenate two strings
shortdays=["Mon","Tue","Wed","Thrus","Fri","Sat","Sun"]
day=days+shortdays
print(day)
# * is used to repeatively print the list
print(shortdays*2)
#del is used to delete the list
del day
print(day)
