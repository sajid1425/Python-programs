import array
a = array.array('i', [1, 2, 3, 4,]) # use i for integer
print(a)
#accessing array by index
print(a[0]) 
print(a[2])
#append or insert element at last in array 
a.append(6)
print(a[4])
#remove elements from array 
a.remove(1)
print(a[3])
print(a)
#inserting element at a particular index
a.insert(1,12)
print(a)
#update element at a particular index
a[2]= 9
print(a)
#using range function
for element in a:
    print(element)
