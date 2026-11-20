import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
from _helpers import finish

# Find intersections of:
# Circle: x^2 + y^2 = 4
# Parabola: y = x^2 - 1
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]

points = []
for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    points.append(solution.x)
    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", np.array(equations(solution.x)))
    print("Converged:", solution.success)
    print()

theta = np.linspace(0, 2 * np.pi, 400)
plt.plot(2 * np.cos(theta), 2 * np.sin(theta), label="Circle x^2 + y^2 = 4")
xs = np.linspace(-2.2, 2.2, 200)
plt.plot(xs, xs**2 - 1, label="Parabola y = x^2 - 1")
pts = np.array(points)
plt.plot(pts[:, 0], pts[:, 1], "ko", label="Intersections")
plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Circle and parabola intersections")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_12_original.png")
