'''
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
'''
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

# Проверка соответствия
assert abs(variance - expected_variance) < 1e-4, "Дисперсия не соответствует ожидаемому значению"
assert abs(std_deviation - expected_std_deviation) < 1e-4, "Стандартное отклонение не соответствует ожидаемому значению"
assert abs(coefficient_of_variation - expected_coefficient_of_variation) < 1e-4, "Коэффициент дисперсии не соответствует ожидаемому значению"

print("Все результаты вычислений соответствуют ожидаемым значениям.")
