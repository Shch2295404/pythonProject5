import pandas as pd

df = pd.read_csv("dz.csv")

print(df.head())
print(df.info())  # печатает информацию о DataFrame
print(df.describe())  # печатает описательные статистики

df.fillna(0, inplace=True)  # inplace=True - обновляет df вместе с заменой пропущенных значений
print(df)

'''
 группирует DataFrame по столбцу City и считает среднее значение в столбце Salary
'''
grouped_df = df.groupby('City')['Salary'].mean()
print(grouped_df)
print(grouped_df.agg(['min', 'max'])) # печатает минимальное и максимальное значение для каждого города
