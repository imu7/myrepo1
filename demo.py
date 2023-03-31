import pandas as pd
di={"name":['abc','def','ghi'],'Roll':[20,30,40]}
df=pd.DataFrame(di)
print(df)
d=pd.read_excel("sales data Tablue.xlsx")
df=pd.DataFrame(d)
print(df)