import pandas as pd

df = pd.read_csv("dz.csv")  # считывает данные из CSV-файла в DataFrame

print(df.head())  # печатает первые 5 строк DataFrame
print(df.info())  # печатает информацию о DataFrame
print(df.describe())  # печатает статистические характеристики DataFrame

'''
заполняет пропущенные значения в столбце Salary нулями
'''
df.fillna(0, inplace=True)
print(df)

'''
 группирует DataFrame по столбцу City и считает среднее значение в столбце Salary
'''
grouped_df = df.groupby('City')['Salary'].mean()
print(grouped_df)

'''
 группирует DataFrame по столбцу City и считает минимальное и максимальное значение в столбце Salary
'''
grouped_df = df.groupby('City')['Salary'].agg(['min', 'max'])
print(grouped_df.agg(['min', 'max']))
