import numpy as np
import matplotlib.pyplot as plt


# Генерируем два набора случайных данных
num_points = 100
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Создаем диаграмму рассеивания
plt.scatter(x_data, y_data, c='blue', alpha=0.5)
plt.title('Диаграмма рассеивания случайных данных')
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.show()
