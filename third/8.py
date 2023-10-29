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

# Угол поворота
angle = np.radians(45)

# Поворот относительно оси X на angle градусов
angle_x = angle
rotation_matrix_x = np.array([
    [1, 0, 0, 0],
    [0, np.cos(angle_x), -np.sin(angle_x), 0],
    [0, np.sin(angle_x), np.cos(angle_x), 0],
    [0, 0, 0, 1]
])
vertices = np.dot(vertices, rotation_matrix_x.T)

# Матрицы преобразования для перемещения кубов
translation_matrices = [
    np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 2],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 0],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, -0.5],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 0],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, -1],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 2],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, -0.5],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 2],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, -1],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 2],
        [0, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 2],
        [0, 1, 0, 0],
        [0, 0, 1, 2],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.7, 0, 0, 3],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 3],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.25, 0, 0, 3],
        [0, 0.25, 0, 0],
        [0, 0, 0.25, 3.5],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.4, 0, 0, 2],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 4],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 2],
        [0, 1, 0, 0],
        [0, 0, 1, 3],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.5, 0, 0, 2.5],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 1.5],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.5, 0, 0, 2],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.5, 0, 0, 2],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 3],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.5, 0, 0, 1],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 0.5],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.5, 0, 0, 0],
        [0, 0.5, 0, 0],
        [0, 0, 0.5, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.25, 0, 0, -0.25],
        [0, 0.25, 0, 0],
        [0, 0, 0.25, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.25, 0, 0, -0.15],
        [0, 0.25, 0, 0],
        [0, 0, 0.25, 0.25],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.25, 0, 0, 3],
        [0, 0.25, 0, 0],
        [0, 0, 0.25, 3.5],
        [0, 0, 0, 1]
    ]),
    np.array([
        [0.25, 0, 0, 3],
        [0, 0.25, 0, 1],
        [0, 0, 0.25, 3.5],
        [0, 0, 0, 1]
    ]),
]


# Цвета для каждого куба
colors = ['yellow', 'yellow', 'yellow', 'yellow', 'brown', 'yellow', 'brown', 'yellow', 'yellow', 'yellow', 'brown',
          'yellow', 'yellow', 'brown', 'brown', 'brown', 'brown', 'brown', 'black','brown','black','black']

# Отрисовка трех кубов
for i in range(len(translation_matrices)):
    translated_vertices = np.dot(vertices, translation_matrices[i].T)[:, :-1]
    faces = [
        [translated_vertices[0], translated_vertices[1], translated_vertices[5], translated_vertices[4]],
        [translated_vertices[7], translated_vertices[6], translated_vertices[2], translated_vertices[3]],
        [translated_vertices[0], translated_vertices[4], translated_vertices[7], translated_vertices[3]],
        [translated_vertices[1], translated_vertices[5], translated_vertices[6], translated_vertices[2]],
        [translated_vertices[4], translated_vertices[5], translated_vertices[6], translated_vertices[7]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=colors[i], linewidths=1, edgecolors='black', alpha=.75))

# Установка пределов для осей x, y и z
ax.set_xlim([0, 4])
ax.set_ylim([0, 0.5])
ax.set_zlim([0, 4.])

# Убираем подписи шагов у осей
ax.set_yticks([])
ax.set_xticks([])
ax.set_zticks([])

# Установка камеры для видимости только плоскости XZ
ax.view_init(elev=0, azim=-90)

# Настройка меток осей
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# Отображение графики
plt.show()
