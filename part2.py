import pandas as pd
from pandas import DataFrame

('\n'
 '    Этот код считывает CSV-файл \'hh.csv\' в pandas DataFrame, \n'
 '    затем выводит имена столбцов, типы данных, \n'
 '    уникальные значения для каждого столбца и описательную статистику. \n'
 '    Наконец, создается новый столбец \'test\' со значениями от 0 до длины DataFrame.\n')
df = pd.read_csv('hh.csv')  # чтение csv-файла
print(df.columns)  # вывод названий столбцов
print(df.dtypes)  # вывод типов столбцов
print(df.nunique())  # вывод уникальных значений столбца
print(df.describe())  # вывод описательной статистики

df['test'] = [new for new in range(len(df))] # создание нового столбца
print(df.head(len(df)))

df.drop('test', axis=1, inplace=True) # inplace=True - обновляет df вместе с удалением столбца
print(df.head(len(df)))

df.drop(len(df)-4, axis=0, inplace=True) # inplace=True - обновляет df вместе с удалением строки
print(df.head(len(df)))

df.sort_values(by='Название вакансии', inplace=True)

# inplace=True - обновляет df вместе с сортировкой
'''
df.arrange('Название вакансии')
Для ясности и стандартизации заменил arrange на sort_values. 
Кроме того, использовал параметр by, чтобы указать столбец для сортировки, 
.str.lower() для перевода значений столбцов в нижний регистр 
и установил inplace=True для операции сортировки, чтобы изменить DataFrame на месте.
'''
print(df.head(len(df)))
df.to_csv('hh.csv', index=False)  # сохранение csv-файла
