# While Loop
print("While Loop")
i =0
while i<5:
    print("Hello")
    i+=1
    
print("While with else")
while i<5:
    print(i)
else:
    print("Program Ends")
    
# For Loop
print("For Loop - Tuple")
mytup=['DYPCET','DYPSEM','DYPATU']
for value in mytup:
    print(value)

print("For Loop - len")
for i in range(len(mytup)):
    print(i)

print("For Loop Using range(5)")
for i in range(5):
    print(i)
print("For Loop Using range(4,9)")
for i in range(4,9):
    print(i)
print("For Loop Using range(4,9,2)")
for i in range(4,9,2):
    print(i)