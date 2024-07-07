"""
Есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
1. Создать DataFrame с данными
data = {
                'name': ['Мария','Иван', 'Сергей', 'Александр', 'Инна', 'Ира', 'Инна', 'Дмитрий', 'Елена', 'Николай'],
                'gender': ['female', 'male', 'male', 'male', 'female', 'female', 'female', 'male', 'female','male'],
                'lesson': ['Математика', 'Физика', 'Химия', 'Информатика', 'Литература']
 }
2. Вывести первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
3. Вычислить среднюю оценку по каждому предмету
print(f"Средняя оценка - {df['Математика'].mean()}")
4. Вычислить медианную оценку по каждому предмету
print(f"Медианная оценка - {df['Математика'].median()}")
5. Вычислить Q1 и Q3 для оценок по математике:
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
downside = Q1_math - 1.5 * IQR_math
upside = Q3_math + 1.5 * IQR_math
df_new = df[(df['Математика'] >= downside) & (df['Математика'] <= upside)]
df_new.boxplot(column='Математика')
plt.show()
6. Вычислить стандартное отклонение
print(f"Стандартное отклонение - {df['Математика'].std()}")

"""
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'name': ['Мария', 'Иван', 'Сергей', 'Александр', 'Инна', 'Ира', 'Инна', 'Дмитрий', 'Елена', 'Николай'],
    'gender': ['female', 'male', 'male', 'male', 'female', 'female', 'female', 'male', 'female', 'male'],
    'lesson': ['Математика', 'Физика', 'Химия', 'Информатика', 'Литература'],
    'Математика': [3, 4, 5, 3, 4, 5, 3, 4, 5, 3],
    'Физика': [4, 3, 4, 4, 3, 4, 4, 3, 4, 4],
    'Химия': [4, 3, 3, 4, 3, 3, 4, 3, 3, 4],
    'Информатика': [4, 4, 5, 4, 4, 5, 4, 4, 5, 4],
    'Литература': [4, 3, 3, 4, 3, 3, 4, 3, 3, 3]
}

df = pd.DataFrame(data)

# Преобразуем столбцы в категориальные данные для столбцов "name" и "gender" и "lesson":
df['name'] = df['name'].astype('category')
df['gender'] = df['gender'].astype('category')
df['lesson'] = df['lesson'].astype('category')
# Команда astype преобразует gender и lesson в категориальный тип,
# что позволяет работать с этими данными как с категориями.

print(df['name'].cat.categories)
print(df['gender'].cat.categories)
print(df['lesson'].cat.categories)

df['name'] = df['name'].cat.codes
df['gender'] = df['gender'].cat.codes
df['lesson'] = df['lesson'].cat.codes
print(df['gender'].cat.codes)
# сохранили внесённые изменения в изначальном датафрейме
df['lesson'] = df['lesson'].cat.add_categories(['Экономика'])
print(df['lesson'].cat.categories)

df['lesson'] = df['lesson'].cat.remove_categories(['Экономика'])
print(df['lesson'].cat.categories)

print(df)

print(f"Средняя оценка - {df['Математика'].mean()}")
print(f"Медианная оценка - {df['Математика'].median()}")
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"Стандартное отклонение - {df['Математика'].std()}")

downside = Q1_math - 1.5 * IQR_math
upside = Q3_math + 1.5 * IQR_math
df_new = df[(df['Математика'] >= downside) & (df['Математика'] <= upside)]
df_new.boxplot(column='Математика')
plt.show()
