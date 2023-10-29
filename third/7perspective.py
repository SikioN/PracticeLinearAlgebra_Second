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
        [1, 0, 0, 0],  # Первый куб, не перемещаем
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 1.5],  # Второй куб, смещение по X на 2
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]),
    np.array([
        [1, 0, 0, 3],  # Третий куб, смещение по X на 4
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
]

# Цвета для каждого куба
colors = ['cyan', 'magenta', 'yellow']


# Определение матрицы перспективы
def perspective_matrix(fov, aspect, near, far):
    f = 1.0 / np.tan(fov / 2.0)
    return np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0]
    ])


# Применение матрицы перспективы к вершинам
fov = np.radians(60)  # Угол обзора
aspect = 4.0 / 3.0  # Соотношение сторон
near = 1.0  # Ближняя плоскость отсечения
far = 10.0  # Дальняя плоскость отсечения
perspective_matrix = perspective_matrix(fov, aspect, near, far)

# Отрисовка трех кубов
for i in range(3):
    translated_vertices = np.dot(vertices, translation_matrices[i].T)
    transformed_vertices = np.dot(translated_vertices, perspective_matrix.T)[:, :-1]  # Применение матрицы перспективы
    faces = [
        [transformed_vertices[0], transformed_vertices[1], transformed_vertices[5], transformed_vertices[4]],
        [transformed_vertices[7], transformed_vertices[6], transformed_vertices[2], transformed_vertices[3]],
        [transformed_vertices[0], transformed_vertices[4], transformed_vertices[7], transformed_vertices[3]],
        [transformed_vertices[1], transformed_vertices[5], transformed_vertices[6], transformed_vertices[2]],
        [transformed_vertices[4], transformed_vertices[5], transformed_vertices[6], transformed_vertices[7]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=colors[i], linewidths=1, edgecolors='r', alpha=.25))

# Установка новых пределов для осей x, y и z
ax.set_xlim([0, 4])
ax.set_ylim([0, 0.3])
ax.set_zlim([-3.5, 0])

ax.view_init(elev=0, azim=-90)

# Убираем подписи шагов у осей
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Отображение графики
plt.show()
