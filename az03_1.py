import numpy as np
import matplotlib.pyplot as plt


# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество выборок

# Генерируем случайные числа, распределенные в соответствии с нормальным распределением
data = np.random.normal(mean, std_dev, num_samples)

# Создать гистограмму
plt.hist(data, bins=30, edgecolor='black')
plt.title('Гистограмма нормально распределенных данных')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
