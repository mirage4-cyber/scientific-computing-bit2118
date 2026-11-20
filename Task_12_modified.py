import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: circle radius 2 -> 1 (circle x^2 + y^2 = 1, parabola y = x^2 - 1)
def equations(z):
    x, y = z
    return [x**2 + y**2 - 1, y - (x**2 - 1)]


found = []
for guess in ([1.0, 0.5], [-1.0, 0.5], [0.3, -0.8], [0.0, -0.5]):
    sol = root(equations, guess)
    res_norm = np.linalg.norm(equations(sol.x))
    if res_norm < 1e-6:
        found.append(sol.x)
    print(f"Guess {guess}: result = {np.round(sol.x, 6) + 0.0}, "
          f"residual norm = {res_norm:.1e}, solver reports converged = {sol.success}")

theta = np.linspace(0, 2 * np.pi, 400)
xs = np.linspace(-1.6, 1.6, 200)
plt.plot(np.cos(theta), np.sin(theta), label="Circle x^2 + y^2 = 1")
plt.plot(xs, xs**2 - 1, label="Parabola y = x^2 - 1")
f = np.array(found)
plt.plot(f[:, 0], f[:, 1], "ko", label="Intersections")
plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Smaller circle: two crossings and one touching point")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_12_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# A ball is kicked at 45 degrees and follows y = x - 0.01 x^2 (metres).
# A camera with a circular range of 60 m is placed at the origin.
# Where does the ball path cross the edge of the camera range?
RANGE = 60.0


def equations(z):
    x, y = z
    return [x**2 + y**2 - RANGE**2, y - (x - 0.01 * x**2)]


for label, guess in [("Ball leaves camera range", [55.0, 20.0]),
                     ("Other crossing (backwards along the parabola)", [-35.0, -45.0])]:
    sol = root(equations, guess)
    print(f"{label}: x = {sol.x[0]:.3f} m, y = {sol.x[1]:.3f} m, "
          f"distance = {np.hypot(*sol.x):.3f} m, converged = {sol.success}")
    if label.startswith("Ball"):
        exit_point = sol.x

landing = 100.0
print(f"The ball lands at x = {landing:.0f} m (y = 0), so the exit point is before landing: {exit_point[0] < landing}")

theta = np.linspace(0, 2 * np.pi, 400)
xs = np.linspace(0, 100, 200)
plt.plot(RANGE * np.cos(theta), RANGE * np.sin(theta), label="Camera range (60 m)")
plt.plot(xs, xs - 0.01 * xs**2, label="Ball path")
plt.plot(*exit_point, "ko", label=f"Exit point ({exit_point[0]:.1f}, {exit_point[1]:.1f})")
plt.xlim(-10, 105)
plt.ylim(-10, 65)
plt.gca().set_aspect("equal")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Where the ball path leaves the camera range")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_12_modified.png")
