# Working with dates via Pandas functions
# part5.py
```python
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

```
# part3.py
```python
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

```
# part1.py
```python
import pandas as pd # импортирует библиотеку pandas под именем pd


"""
 Этот фрагмент кода выполняет следующие действия:
 Импортирует библиотеку pandas под именем pd.
 Считывает CSV-файл с именем "recipes.csv" в DataFrame df0 и выводит первые 3 строки и последнюю строку из него.
 Создает новый DataFrame df1 на основе df0 и печатает его первую и последнюю строки.
 Определяет функцию read_csv, которая считывает CSV-файл и возвращает DataFrame.
 Вызывает функцию read_csv для чтения файла "recipes.csv" и печатает возвращаемый ею DataFrame.
"""
df0 = pd.read_csv("recipes.csv")
print(df0.info()) # печатает информацию о DataFrame
print(df0.shape) # печатает количество строк и столбцов
print(df0.describe()) # печатает описательные статистики
print(df0.columns) # печатает названия столбцов
print(df0.index) # печатает индексы строк
print(df0["RecipeName"]) # печатает столбец RecipeName
print(df0[["RecipeId", "RecipeName"]]) # печатает столбцы RecipeId и RecipeName
print(df0.loc[1234]) # печатает строку с индексом 1234
print(df0.head(3))
print(df0.tail(1))
print(df0.loc[1234,'RecipeDescription']) # печатает описание рецепта с индексом 1234
print(df0[df0['RecipeDescription'].str.contains('Chicken Pizziola Salad')],"\n") # печатает рецепты, содержащие "Chicken Pizziola Salad"

df1=pd.DataFrame(df0)
print(df1.head(2)) # печатает первые 2 строки
print(df1.tail(1))

def read_csv(file):
    """
    Считывает CSV-файл и возвращает pandas DataFrame.
    Параметры:
    file (str): Путь к файлу CSV, который нужно прочитать.
    Возвращает:
    pandas DataFrame: DataFrame, содержащий данные, считанные из CSV-файла.

    Этот код определяет функцию read_csv, которая считывает CSV-файл,
    указанный параметром file, и возвращает данные в виде pandas DataFrame.
    Функция принимает путь к файлу в качестве строкового входного параметра и
    выводит DataFrame, содержащий данные,
    считанные из CSV-файла с помощью функции pandas read_csv.
    """
    return pd.read_csv(file)

print(read_csv("recipes.csv"))
```
