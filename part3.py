import pandas as pd
from pandas import DataFrame


df = pd.read_csv('animal.csv')
print(df.head(len(df)))


print(df.head(len(df)))

df.to_csv('animal.csv', index=False)
