'''
Считывает CSV-файл с именем 'animal.csv' в pandas DataFrame.
Заполняет отсутствующие значения в DataFrame значением 0.
Сохраняет обновленный DataFrame обратно в 'animal.csv' без включения значений индексов.
Группирует DataFrame по столбцу "Пища" и вычисляет среднее значение столбца "Средняя продолжительность жизни".
'''
import pandas as pd


df = pd.read_csv('animal.csv')
print(df.head(len(df)))

df.fillna(0, inplace=True)  # inplace=True - обновляет df вместе с заменой пропущенных значений
print(df.head(len(df)))

'''
df.dropna(inplace=True) # inplace=True - обновляет df вместе с удалением пропущенных значений
print(df.head(len(df)))
'''

df.to_csv('animal.csv', index=False)  # index=False - не сохраняет индексы

grouped_df = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
'''
    Пища - название столбца, Средняя продолжительность жизни - столбец с средней продолжительностью жизни
'''
print(grouped_df)
