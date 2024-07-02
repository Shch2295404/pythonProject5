import pandas as pd


df0 = pd.read_csv("recipes.csv")
print(df0.head(3))
print(df0.tail(1))

df1=pd.DataFrame(df0)
print(df1.head())
print(df1.tail())

def read_csv(file):
    return pd.read_csv(file)

print(read_csv("recipes.csv"))
