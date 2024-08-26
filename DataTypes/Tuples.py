#Tuples are immutable so we cannot insert elements
mytup =("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(mytup)
for i in mytup:
    print(i)

#Concat Tupes
wtup=(1,2,3,4,5)
ctup = wtup+mytup
print(ctup)
#To delete tuples
del mytup
