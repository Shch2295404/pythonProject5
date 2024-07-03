import pandas as pd

df = pd.read_csv("dz.csv")

print(df.head())
print(df.info())  # печатает информацию о DataFrame
print(df.describe())  # печатает описательные статистики

'''
 группирует DataFrame по столбцу City и считает среднее значение в столбце Salary
'''
grouped_df = df.groupby('City')['Salary'].mean()

print(df.head(len(grouped_df)))
print(grouped_df)
