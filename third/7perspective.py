import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Вершины для кубов с однородными координатами (x, y, z, w)
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

# Матрицы преобразования для перемещения кубов
translation_matrices = [
    np.array([
        [1, 0, 0, i * 1.5 ],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]) for i in range(3)
]

# Применение матрицы перспективы
perspective_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, -1/6, 1]
])

# Цвета для каждого куба
colors = ['cyan', 'magenta', 'yellow']

# Отрисовка трех кубов с применением матрицы перспективы
for i in range(3):
    translated_vertices = np.dot(vertices, translation_matrices[i].T)
    perspective_vertices = np.dot(translated_vertices, perspective_matrix.T)[:, :-1]
    faces = [
        [perspective_vertices[0], perspective_vertices[1], perspective_vertices[5], perspective_vertices[4]],
        [perspective_vertices[7], perspective_vertices[6], perspective_vertices[2], perspective_vertices[3]],
        [perspective_vertices[0], perspective_vertices[4], perspective_vertices[7], perspective_vertices[3]],
        [perspective_vertices[1], perspective_vertices[5], perspective_vertices[6], perspective_vertices[2]],
        [perspective_vertices[4], perspective_vertices[5], perspective_vertices[6], perspective_vertices[7]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=colors[i], linewidths=1, edgecolors='r', alpha=.25))

# Установка новых пределов для осей x, y и z
ax.set_xlim([0, 4])
ax.set_ylim([0, 0.3])
ax.set_zlim([-1, 2.5])

# Убираем подписи шагов у осей
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Установка камеры для видимости только плоскости XZ
ax.view_init(elev=0, azim=-90)

# Отображение графики
plt.show()
