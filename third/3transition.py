import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Вершины начального куба с однородными координатами (x, y, z, w)
vertices = np.array([
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
])

# Матрица преобразования для перемещения начального куба (в данном случае, на 1 по оси X, 2 по оси Y и 3 по оси Z)
translation_matrix = np.array([
    [1, 0, 0, 1],
    [0, 1, 0, 2],
    [0, 0, 1, 3],
    [0, 0, 0, 1]
])

# Применяем матрицу преобразования к вершинам начального куба
translated_vertices = np.dot(vertices, translation_matrix.T)  # Транспонируем матрицу для правильного перемножения

# Убираем однородные координаты (последний столбец) для начального куба
vertices = vertices[:, :-1]

# Убираем однородные координаты (последний столбец) для перемещенного куба
translated_vertices = translated_vertices[:, :-1]

# Грани начального куба
faces = [
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[7], vertices[6], vertices[2], vertices[3]],
    [vertices[0], vertices[4], vertices[7], vertices[3]],
    [vertices[1], vertices[5], vertices[6], vertices[2]],
    [vertices[4], vertices[5], vertices[6], vertices[7]]
]

# Грани перемещенного куба
translated_faces = [
    [translated_vertices[0], translated_vertices[1], translated_vertices[5], translated_vertices[4]],
    [translated_vertices[7], translated_vertices[6], translated_vertices[2], translated_vertices[3]],
    [translated_vertices[0], translated_vertices[4], translated_vertices[7], translated_vertices[3]],
    [translated_vertices[1], translated_vertices[5], translated_vertices[6], translated_vertices[2]],
    [translated_vertices[4], translated_vertices[5], translated_vertices[6], translated_vertices[7]]
]

# Отрисовка граней начального куба
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Отрисовка граней перемещенного куба
ax.add_collection3d(Poly3DCollection(translated_faces, facecolors='magenta', linewidths=1, edgecolors='g', alpha=.25))

# Вектор, по которому перемещается куб
vector_start = [0, 0, 0]
vector_end = [1, 2, 3]
ax.quiver(vector_start[0], vector_start[1], vector_start[2],
          vector_end[0], vector_end[1], vector_end[2], color='b')

# Установка пределов для осей x, y и z
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])

# Настройка меток осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графики
plt.show()
