"""
    Считывает CSV-файл с именем "dz.csv" в pandas DataFrame.
    Печатает первые 5 строк DataFrame.
    Выводит информацию о DataFrame.
    Выводит статистическую информацию о DataFrame.
    Заполняет все отсутствующие значения в DataFrame значением 0.
    Группирует кадры данных по столбцу "Город" и вычисляет среднюю зарплату для каждого города.
    Группирует кадр данных по столбцу "Город" и вычисляет минимальную
    и максимальную зарплату для каждого города.
"""
import pandas as pd


df = pd.read_csv("dz.csv")
print(df.head())
print(df.info())
print(df.describe())

df.fillna(0, inplace=True)
print(df)

grouped_df = df.groupby('City')['Salary'].mean()
print(grouped_df)

grouped_df = df.groupby('City')['Salary'].agg(['min', 'max'])
print(grouped_df.agg(['min', 'max']))
