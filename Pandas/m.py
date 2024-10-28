import pandas as pd
data={'Name':['Atharv','Varad','Sourabh','Sajid','Sarvesh'],'Age':[24,27,22,32,29]}
df=pd.DataFrame(data)
print(df)
print(df['Age'])