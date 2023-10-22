import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt

# Определите угол поворота
a = 0
b = 2
# d = 0

# Базисные вектора
basis_vector1 = np.array([1, 0])
basis_vector2 = np.array([0, 1])

# Матрица линейного оператора для отражения относительно прямой y = ax
transformation_matrix = np.array(
    [[1 / sqrt(1 + a ** 2), a / sqrt(1 + a ** 2)],
     [1 / sqrt(1 + b ** 2), b / sqrt(1 + b ** 2)]])

transformation_matrix = np.linalg.inv(transformation_matrix)

# reflection_matrix = np.array([[(1 - a ** 2) / (1 + a ** 2), 2 * a / (1 + a ** 2)],
#                               [2 * a / (1 + a ** 2), (a ** 2 - 1) / (1 + a ** 2)]])
# rotate_matrix = np.array([[cos(d), sin(d)],
#                           [-sin(d), cos(d)]])
# transformation_matrix = np.dot(rotate_matrix, reflection_matrix)

# # Прямая y = ax
x_line = np.arange(-10, 11, 1)
y_line = a * x_line
#
# Прямая y = bx
x_line_2 = np.arange(-10, 11, 1)
y_line_2 = b * x_line

# Применение унитарного оператора к базисным векторам
rotated_basis_vector1 = basis_vector1.dot(transformation_matrix)
rotated_basis_vector2 = basis_vector2.dot(transformation_matrix)

# Генерация сетки точек в исходной плоскости с шагом 1 и целыми координатами
x = np.arange(-5, 6, 1)
y = np.arange(-5, 6, 1)
X, Y = np.meshgrid(x, y)
points = np.vstack((X.flatten(), Y.flatten())).T

# Применение унитарного оператора (поворота) к каждой точке
rotated_points = points.dot(transformation_matrix)

# Разделение исходных и преобразованных точек
x1, y1 = points[:, 0], points[:, 1]
x2, y2 = rotated_points[:, 0], rotated_points[:, 1]

# Создание градиентного массива точек
color_array = np.linspace(0, 1, len(points))

# Создание графиков
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.title('Исходная плоскость')
plt.quiver(0, 0, basis_vector1[0], basis_vector1[1], angles='xy', scale_units='xy', scale=1, color='c')
plt.quiver(0, 0, basis_vector2[0], basis_vector2[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.plot(x_line, y_line, color='mediumaquamarine', linestyle='--', label=f'Прямая y = ax')
plt.plot(x_line_2, y_line_2, color='mediumpurple', linestyle='--', label=f'Прямая y = bx')
plt.scatter(x1, y1, c=color_array, cmap='viridis')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.subplot(122)
plt.title('Плоскость после поворота')
plt.quiver(0, 0, rotated_basis_vector1[0], rotated_basis_vector1[1], angles='xy', scale_units='xy', scale=1, color='c')
plt.quiver(0, 0, rotated_basis_vector2[0], rotated_basis_vector2[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.plot(x_line, y_line, color='mediumaquamarine', linestyle='--', label=f'Прямая y = ax')
plt.plot(x_line_2, y_line_2, color='mediumpurple', linestyle='--', label=f'Прямая y = bx')
plt.scatter(x2, y2, c=color_array, cmap='viridis')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.show()
