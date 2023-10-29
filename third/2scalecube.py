import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')  # Две подграфики для отображения начального и масштабированного куба
ax.set_title("Начальный куб")

ax_scaled = fig.add_subplot(122, projection='3d')
ax_scaled.set_title("Масштабированный куб")

# Вершины куба
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Грани куба (задаются в виде индексов вершин)
faces = [
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[7], vertices[6], vertices[2], vertices[3]],
    [vertices[0], vertices[4], vertices[7], vertices[3]],
    [vertices[1], vertices[5], vertices[6], vertices[2]],
    [vertices[4], vertices[5], vertices[6], vertices[7]]
]

# Отрисовка начального куба
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

# Определение матрицы масштабирования (в данном случае увеличение в 2 раза)
scale_matrix = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
])

# Масштабирование вершин куба
scaled_vertices = vertices.dot(scale_matrix)

# Отрисовка масштабированного куба
scaled_faces = [
    [scaled_vertices[0], scaled_vertices[1], scaled_vertices[5], scaled_vertices[4]],
    [scaled_vertices[7], scaled_vertices[6], scaled_vertices[2], scaled_vertices[3]],
    [scaled_vertices[0], scaled_vertices[4], scaled_vertices[7], scaled_vertices[3]],
    [scaled_vertices[1], scaled_vertices[5], scaled_vertices[6], scaled_vertices[2]],
    [scaled_vertices[4], scaled_vertices[5], scaled_vertices[6], scaled_vertices[7]]
]

ax_scaled.add_collection3d(Poly3DCollection(scaled_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax_scaled.set_xlim([0, 2])
ax_scaled.set_ylim([0, 2])
ax_scaled.set_zlim([0, 2])

# Отображение графиков
plt.show()
