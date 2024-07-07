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

print(f"Средняя оценка - {math_mean}")
print(f"Медианная оценка - {math_median}")
print(f"Q1 - {Q1_math}, Q3 - {Q3_math}, IQR - {IQR_math}")
print(f"Стандартное отклонение - {std_dev_math}")
print(f"Нижняя граница - {downside}, верхняя граница - {upside}")

# Фильтрация данных по отклонениям
df_filtered_math = df_students[(df_students['Math'] >= downside) & (df_students['Math'] <= upside)]

# Визуализация отфильтрованных оценок по математике
df_filtered_math.boxplot(column='Math')
plt.show()
