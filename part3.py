import pandas as pd


df = pd.read_csv('animal.csv')
print(df.head(len(df)))

df.fillna(0, inplace=True) # inplace=True - обновляет df вместе с заменой пропущенных значений
print(df.head(len(df)))

'''
df.to_csv('animal.csv', index=False)
'''