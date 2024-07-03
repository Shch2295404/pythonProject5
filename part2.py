import pandas as pd

df = pd.read_csv('hh.csv')  # чтение csv-файла
print(df.columns)  # вывод названий столбцов
print(df.dtypes)  # вывод типов столбцов
print(df.nunique())  # вывод уникальных значений столбца
print(df.describe())  # вывод описательной статистики
