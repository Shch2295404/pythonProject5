# Bot API, пожалуйста, ознакомьтесь с руководством:
/newbot - создать нового бота

/mybots - редактировать ваших ботов

# Редактировать ботов
/setname - изменить имя бота

/setdescription - изменить описание бота

/setabouttext - изменить информацию о боте

/setuserpic - изменить фотографию профиля бота

/setcommands - изменить список команд

/deletebot - удалить бота

# Настройки бота
/token - сгенерировать токен авторизации

/revoke - отозвать токен доступа к боту

/setinline - переключить режим инлайна

/setinlinegeo - переключить запросы местоположения в режиме инлайн

/setinlinefeedback - изменить настройки обратной связи в режиме инлайн

/setjoingroups - может ли ваш бот быть добавлен в группы?

/setprivacy - переключить режим конфиденциальности в группах

# Веб-приложения
/myapps - редактировать ваши веб-приложения

/newapp - создать новое веб-приложение

/listapps - получить список ваших веб-приложений

/editapp - редактировать веб-приложение

/deleteapp - удалить существующее веб-приложение

# Игры
/mygames - редактировать ваши игры

/newgame - создать новую игру

/listgames - получить список ваших игр

/editgame - редактировать игру

/deletegame - удалить существующую игру


# Working with dates via Pandas functions
# az02_1.py
```python
"""
This code snippet creates a DataFrame with student data,
calculates statistical data like mean, median, quartiles,
inter quartile range, standard deviation,
and filters the data based on deviations from the quartiles.
It then visualizes the filtered math scores using a boxplot.
"""
import pandas as pd
import matplotlib.pyplot as plt


# Создаем DataFrame с данными о студентах
student_data = {
    'name': ['Мария', 'Иван', 'Сергей', 'Александр', 'Инна', 'Ира', 'Инна', 'Дмитрий', 'Елена', 'Николай'],
    'gender': ['female', 'male', 'male', 'male', 'female', 'female', 'female', 'male', 'female', 'male'],
    'Math': [3, 4, 5, 3, 4, 5, 3, 4, 5, 3],
    'Physics': [4, 3, 4, 4, 3, 4, 4, 3, 4, 4],
    'Chemistry': [4, 3, 3, 4, 3, 3, 4, 3, 3, 4],
    'Computer Science': [4, 4, 5, 4, 4, 5, 4, 4, 5, 4],
    'Literature': [4, 3, 3, 4, 3, 3, 4, 3, 3, 3]
}

df_students = pd.DataFrame(student_data)

# Подсчет статистических данных и визуализация
math_mean = df_students['Math'].mean()
math_median = df_students['Math'].median()
Q1_math = df_students['Math'].quantile(0.25)
Q3_math = df_students['Math'].quantile(0.75)
IQR_math = Q3_math - Q1_math
std_dev_math = df_students['Math'].std()
downside = Q1_math - 1.5 * IQR_math
upside = Q3_math + 1.5 * IQR_math

print(f"Средняя оценка - Math {math_mean:.2f}")
print(f"Медианная оценка - Math {math_median:.2f}")
print(f"Q1 - {Q1_math:.2f}, Q3 - {Q3_math:.2f}, IQR - {IQR_math:.2f}")
print(f"Стандартное отклонение - Math {std_dev_math:.3f}")
print(f"Нижняя граница - {downside}, верхняя граница - {upside:.3f}")

# Фильтрация данных по отклонениям
df_filtered_math = df_students[(df_students['Math'] >= downside) & (df_students['Math'] <= upside)]

# Визуализация отфильтрованных оценок по математике
df_filtered_math.boxplot(column='Math')
plt.show()
```
#
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
# math_dispersion.py

```python
"""
Этот фрагмент кода вычисляет дисперсию, стандартное отклонение и коэффициент вариации для заданного набора данных.
Он состоит из следующих шагов:
Вычисление среднего значения
Нахождение отклонений каждого элемента от среднего значения
Возведение отклонений в квадрат
Суммирование квадратов отклонений
Вычисление дисперсии
Вычисление стандартного отклонения
Вычисление коэффициента вариации
Затем вычисленные значения сравниваются с ожидаемыми и утверждается их близость.
"""
import math


# Данные
data = [12, 23, 45, 33, 65, 54, 54]

# Шаг 1: Вычисление среднего значения
mean = sum(data) / len(data)
print(f"Среднее значение: {mean:.3f}")

# Шаг 2: Вычисление отклонений каждого элемента от среднего значения
deviations = [x - mean for x in data]
print(f"Отклонения от среднего значения: {[round(dev, 3) for dev in deviations]}")

# Шаг 3: Вычисление квадратов отклонений
squared_deviations = [dev ** 2 for dev in deviations]
print(f"Квадраты отклонений: {[round(sd, 3) for sd in squared_deviations]}")

# Шаг 4: Вычисление суммы квадратов отклонений
sum_squared_deviations = sum(squared_deviations)
print(f"Сумма квадратов отклонений: {sum_squared_deviations:.3f}")

# Шаг 5: Вычисление дисперсии (с учетом исправления)
n = len(data)
variance = sum_squared_deviations / (n - 1)
print(f"Дисперсия: {variance:.4f}")

# Шаг 6: Вычисление стандартного отклонения
std_deviation = math.sqrt(variance)
print(f"Стандартное отклонение: {std_deviation:.3f}")

# Шаг 7: Вычисление коэффициента дисперсии
coefficient_of_variation = std_deviation / mean
print(f"Коэффициент дисперсии: {coefficient_of_variation:.4f}")

# Проверка результатов
expected_variance = 359.80952
expected_std_deviation = 18.9686
expected_coefficient_of_variation = 0.4643

print("\nПроверка результатов:")
print(f"Ожидаемая дисперсия: {expected_variance:.4f}, Вычисленная дисперсия: {variance:.4f}")
print(f"Ожидаемое стандартное отклонение: {expected_std_deviation:.4f}, Вычисленное стандартное отклонение: {std_deviation:.4f}")
print(f"Ожидаемый коэффициент дисперсии: {expected_coefficient_of_variation:.4f}, Вычисленный коэффициент дисперсии: {coefficient_of_variation:.4f}")

'''
Этот фрагмент кода выполняет утверждения для проверки того, 
достаточно ли близки вычисленные статистики (дисперсия, стандартное отклонение и коэффициент вариации) 
к ожидаемым значениям в пределах допуска 1e-4. 
Если вычисленные значения не соответствуют заданному допуску, 
выдается сообщение об ошибке, указывающее, 
какая статистика не соответствует ожидаемому значению.
'''
assert abs(variance - expected_variance) < 1e-4, "Дисперсия не соответствует ожидаемому значению"
assert abs(std_deviation - expected_std_deviation) < 1e-4, "Стандартное отклонение не соответствует ожидаемому значению"
assert abs(coefficient_of_variation - expected_coefficient_of_variation) < 1e-4, "Коэффициент дисперсии не соответствует ожидаемому значению"

print("Все результаты вычислений соответствуют ожидаемым значениям.")
```

