set={"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}
print(set)
for i in set:
    print(i)
# Add element 5
set.add(5)
print(set)
# Remove element
set.remove("Monday")
print(set)
#Union of two sets
set2={1,2,3,4,5}
print(set.union(set2))
#Intersection of two sets
print(set.intersection(set2))
#Difference of two sets
print(set.difference(set2))