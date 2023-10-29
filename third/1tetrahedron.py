import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Вершины тетраэдра
vertices = [
    [1, 1, 1],
    [1, -1, -1],
    [-1, 1, -1],      
    [-1, -1, 1]
]

# Грани тетраэдра
faces = [
    [vertices[0], vertices[1], vertices[2]],
    [vertices[0], vertices[1], vertices[3]],
    [vertices[0], vertices[2], vertices[3]],
    [vertices[1], vertices[2], vertices[3]]
]

# Отрисовка граней тетраэдра
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Установка пределов для осей x, y и z
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

# Настройка меток осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графики
plt.show()
