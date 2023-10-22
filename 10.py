import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from math import sqrt, pi, cos, sin

# Определите коэффициент растяжения и количество точек для градиента
d = 2  # Пример
kappa = 2

phi = pi / 4
num_points = 100  # Количество точек для градиента

# Матрица линейного оператора для растяжения
stretch_rotation_matrix = np.array([[sqrt(d) * kappa * np.cos(phi), -sqrt(d) * kappa * np.sin(phi)],
                                    [sqrt(d) / kappa * np.sin(phi), sqrt(d) / kappa * np.cos(phi)]])


radius_1 = 1 / sqrt(pi)
# Создание круга на исходной плоскости
circle = Ellipse((0, 0), radius_1, radius_1, fill=False, color='b', label='Круг')

# Применение линейного оператора (растяжения) к кругу
transformed_circle = Ellipse((0, 0), radius_1 * kappa * sqrt(d), (radius_1 / kappa) * sqrt(d), fill=False, color='r',
                             label=f'Растянутый круг (c={d})')

# Создание графика
plt.figure(figsize=(5, 5))
# plt.title('Круг с градиентной границей')

# Добавление круга и границы круга к одному графику
plt.gca().add_patch(circle)
plt.gca().add_patch(transformed_circle)

# Создание градиентного эффекта на границе круга
gradient_colors = plt.cm.viridis(np.linspace(0, 1, num_points))
for i in range(num_points):
    theta = 2 * np.pi * i / num_points
    x = np.cos(theta) * radius_1 / 2
    y = np.sin(theta) * radius_1 / 2
    plt.scatter(x, y, color=gradient_colors[i], s=10)

# Создание градиентного эффекта на границе круга
gradient_colors = plt.cm.viridis(np.linspace(0, 1, num_points))
for i in range(num_points):
    theta = 2 * np.pi * i / num_points
    x = np.cos(theta) * radius_1 / 2
    y = np.sin(theta) * radius_1 / 2
    rotated_point = np.dot(stretch_rotation_matrix, [x, y])
    plt.scatter(rotated_point[0], rotated_point[1], color=gradient_colors[i], s=10)

plt.xlim(-0.8, 0.8)
plt.ylim(-0.8, 0.8)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
# plt.legend()

plt.show()
