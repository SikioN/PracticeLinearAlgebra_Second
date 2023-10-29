import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Вершины квадрата (основание пирамиды)
vertices = [
    [1, 1, 0],
    [1, -1, 0],
    [-1, -1, 0],
    [-1, 1, 0]
]

# Вершина вершины пирамиды
apex_vertex = [0, 0, 2]

# Грани пирамиды и основание пирамиды
face = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [apex_vertex, vertices[0], vertices[1]],
    [apex_vertex, vertices[1], vertices[2]],
    [apex_vertex, vertices[2], vertices[3]],
    [apex_vertex, vertices[3], vertices[0]]
]


# Отрисовка граней квадрата (основания) и пирамиды
ax.add_collection3d(Poly3DCollection(face, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
# ax.add_collection3d(Poly3DCollection(side_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Установка пределов для осей x, y и z
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2.5])

# Настройка меток осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графики
plt.show()
