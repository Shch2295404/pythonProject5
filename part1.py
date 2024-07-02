import pandas as pd


df = pd.read_csv("recipes.csv")
print(df.head(10))

def read_csv(file):
    return pd.read_csv(file)

print(read_csv("recipes.csv"))
