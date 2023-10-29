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

# Применяем последовательные преобразования к вершинам начального куба
# Сдвиг на вектор (-1, -1, -1)
translation_matrix1 = np.array([
    [1, 0, 0, -1],
    [0, 1, 0, -1],
    [0, 0, 1, -1],
    [0, 0, 0, 1]
])
# Угол поворота
angle = np.radians(90)
# Поворот относительно оси X на angle градусов
angle_x = angle
rotation_matrix_x = np.array([
    [1, 0, 0, 0],
    [0, np.cos(angle_x), -np.sin(angle_x), 0],
    [0, np.sin(angle_x), np.cos(angle_x), 0],
    [0, 0, 0, 1]
])
# Поворот относительно оси Y на angle градусов
angle_y = angle
rotation_matrix_y = np.array([
    [np.cos(angle_y), 0, np.sin(angle_y), 0],
    [0, 1, 0, 0],
    [-np.sin(angle_y), 0, np.cos(angle_y), 0],
    [0, 0, 0, 1]
])
# Поворот относительно оси Z на angle градусов
angle_z = angle
rotation_matrix_z = np.array([
    [np.cos(angle_z), -np.sin(angle_z), 0, 0],
    [np.sin(angle_z), np.cos(angle_z), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
# Сдвиг на вектор (1, 1, 1)
translation_matrix2 = np.array([
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])
# Выполняем последовательные преобразования
transformed_vertices = vertices
transformed_vertices = np.dot(transformed_vertices, translation_matrix1.T)
transformed_vertices = np.dot(transformed_vertices, rotation_matrix_x.T)
transformed_vertices = np.dot(transformed_vertices, rotation_matrix_y.T)
transformed_vertices = np.dot(transformed_vertices, rotation_matrix_z.T)
transformed_vertices = np.dot(transformed_vertices, translation_matrix2.T)

# Убираем однородные координаты (последний столбец) для начального и преобразованного кубов
vertices = vertices[:, :-1]
transformed_vertices = transformed_vertices[:, :-1]

# Грани начального куба
faces = [
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[7], vertices[6], vertices[2], vertices[3]],
    [vertices[0], vertices[4], vertices[7], vertices[3]],
    [vertices[1], vertices[5], vertices[6], vertices[2]],
    [vertices[4], vertices[5], vertices[6], vertices[7]]
]

# Грани преобразованного куба
transformed_faces = [
    [transformed_vertices[0], transformed_vertices[1], transformed_vertices[5], transformed_vertices[4]],
    [transformed_vertices[7], transformed_vertices[6], transformed_vertices[2], transformed_vertices[3]],
    [transformed_vertices[0], transformed_vertices[4], transformed_vertices[7], transformed_vertices[3]],
    [transformed_vertices[1], transformed_vertices[5], transformed_vertices[6], transformed_vertices[2]],
    [transformed_vertices[4], transformed_vertices[5], transformed_vertices[6], transformed_vertices[7]]
]

# Отрисовка граней начального куба
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Отрисовка граней преобразованного куба
ax.add_collection3d(Poly3DCollection(transformed_faces, facecolors='magenta', linewidths=1, edgecolors='g', alpha=.25))

# Отмечаем фиксированную вершину красным маркером
ax.scatter(1, 1, 1, color='red', s=100, label='Fixed Vertex')

# Установка пределов для осей x, y и z
ax.set_xlim([-0.5, 1])
ax.set_ylim([-0.5, 1])
ax.set_zlim([0, 1.5])

# Настройка меток осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графики
plt.show()
