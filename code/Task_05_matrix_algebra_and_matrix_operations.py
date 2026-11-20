import numpy as np

# Square coordinates; scale x by 2, y by 1.5, then rotate 45 degrees
points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
angle = np.deg2rad(45)
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle),  np.cos(angle)]])
scaling = np.array([[2., 0.], [0., 1.5]])
transform = rotation @ scaling
transformed = points @ transform.T

print("Original coordinates:\n", points)
print("Transformation matrix:\n", transform)
print("Transformed coordinates:\n", np.round(transformed, 4))
print("Determinant:", np.linalg.det(transform))

# Parameter variation: rotate by 90 degrees
angle2 = np.deg2rad(90)
rotation2 = np.array([[np.cos(angle2), -np.sin(angle2)],
                      [np.sin(angle2),  np.cos(angle2)]])
print("Coordinates after 90-degree rotation:\n", points @ (rotation2 @ scaling).T)
