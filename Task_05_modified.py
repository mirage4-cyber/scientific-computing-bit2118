import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish


def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])


# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: rotation 45 -> 90 degrees and scale (2, 1.5) -> (3, 1)
points = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
scale = np.diag([3.0, 1.0])
transformation = rot(90) @ scale
transformed = points @ transformation.T
print("Transformation matrix:\n", np.round(transformation, 4))
print("Transformed points:\n", np.round(transformed, 4))
print("Determinant:", round(float(np.linalg.det(transformation)), 4))

closed = lambda p: np.vstack([p, p[0]])
plt.plot(*closed(points).T, marker="o", label="Original")
plt.plot(*closed(transformed).T, marker="o", label="Scale (3, 1) then rotate 90 deg")
plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Changed transformation")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_05_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Two-link robot arm. Link lengths in metres, joint angles in degrees.
L1, L2 = 0.5, 0.4
theta1 = 40.0
configs = [("theta2 = 0", 0.0), ("theta2 = 30", 30.0), ("theta2 = 60", 60.0)]

for label, theta2 in configs:
    elbow = rot(theta1) @ np.array([L1, 0.0])
    tip = elbow + rot(theta1 + theta2) @ np.array([L2, 0.0])
    reach = np.linalg.norm(tip)
    check = np.sqrt(L1**2 + L2**2 + 2 * L1 * L2 * np.cos(np.deg2rad(theta2)))
    print(f"{label}: elbow=({elbow[0]:.3f}, {elbow[1]:.3f}) m, "
          f"tip=({tip[0]:.3f}, {tip[1]:.3f}) m, reach={reach:.3f} m (law of cosines: {check:.3f} m)")
    plt.plot([0, elbow[0], tip[0]], [0, elbow[1], tip[1]], marker="o", label=label)

plt.gca().set_aspect("equal")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Two-link robot arm positions (theta1 = 40 deg)")
plt.legend()
plt.grid(True)
finish("task_05_modified.png")
