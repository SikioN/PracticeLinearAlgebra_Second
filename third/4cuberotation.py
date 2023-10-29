import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Вершины начального куба (x, y, z)
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

# Матрица преобразования для поворота куба на 45 градусов относительно оси Z
angle = np.radians(45)  # Преобразуем угол в радианы
rotation_matrix = np.array([
    [np.cos(angle), -np.sin(angle), 0],
    [np.sin(angle), np.cos(angle), 0],
    [0, 0, 1]
])

# Применяем матрицу преобразования к вершинам куба
rotated_vertices = np.dot(vertices, rotation_matrix.T)  # Транспонируем матрицу для правильного перемножения

# Грани начального куба
faces = [
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[7], vertices[6], vertices[2], vertices[3]],
    [vertices[0], vertices[4], vertices[7], vertices[3]],
    [vertices[1], vertices[5], vertices[6], vertices[2]],
    [vertices[4], vertices[5], vertices[6], vertices[7]]
]

# Грани повернутого куба
rotated_faces = [
    [rotated_vertices[0], rotated_vertices[1], rotated_vertices[5], rotated_vertices[4]],
    [rotated_vertices[7], rotated_vertices[6], rotated_vertices[2], rotated_vertices[3]],
    [rotated_vertices[0], rotated_vertices[4], rotated_vertices[7], rotated_vertices[3]],
    [rotated_vertices[1], rotated_vertices[5], rotated_vertices[6], rotated_vertices[2]],
    [rotated_vertices[4], rotated_vertices[5], rotated_vertices[6], rotated_vertices[7]]
]

# Отрисовка граней начального куба
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Отрисовка граней повернутого куба
ax.add_collection3d(Poly3DCollection(rotated_faces, facecolors='magenta', linewidths=1, edgecolors='g', alpha=.25))

# Установка пределов для осей x, y и z
ax.set_xlim([-0.8, 1.5])
ax.set_ylim([-0.8, 1.5])
ax.set_zlim([0, 2])

# Настройка меток осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графики
plt.show()
