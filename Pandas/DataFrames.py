import pandas as pd
#DataFrame
a=[10,20,30,40]
a1=pd.DataFrame(a)
print(a1)

#labelled column
data={"Calories":[420,380,120],"Duration":[50,45,45]}
myvar=pd.DataFrame(data)
print(myvar)

#using csv
df = pd.read_csv("C:/Users/mahab/Downloads/Python/Pandas/customers.csv")
s=df[["First Name","Last Name","City"]]
print(s)

#Head Function
print("Head Function")
print(s.head(10))

#Tail Function
print("Tail Function")
print(s.head(2))