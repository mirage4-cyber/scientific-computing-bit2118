import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish

# Four corners of a square: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

angle = np.deg2rad(45)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combined transformation
transformation = rotation @ scale

# Row-vector form requires multiplication by transpose
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))

closed = lambda p: np.vstack([p, p[0]])
plt.plot(*closed(points).T, marker="o", label="Original")
plt.plot(*closed(transformed_points).T, marker="o", label="Scaled then rotated")
plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scaling and rotating a square")
plt.legend()
plt.grid(True)
finish("task_05_original.png")
