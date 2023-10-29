import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Создаем вершины куба
vertices = np.array([[-1, -1, -1, 1],
                     [-1, -1, 1, 1],
                     [-1, 1, 1, 1],
                     [-1, 1, -1, 1],
                     [1, -1, -1, 1],
                     [1, -1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, -1, 1]])

# Определяем грани куба
faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
         [vertices[4], vertices[5], vertices[6], vertices[7]],
         [vertices[0], vertices[1], vertices[5], vertices[4]],
         [vertices[2], vertices[3], vertices[7], vertices[6]],
         [vertices[1], vertices[2], vertices[6], vertices[5]],
         [vertices[0], vertices[3], vertices[7], vertices[4]]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Отрисовываем грани куба
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

plt.show()
