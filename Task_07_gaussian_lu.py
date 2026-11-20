import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu_factor, lu_solve
from _helpers import finish

# The same coefficient matrix is reused for several measurement vectors.
A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

# Factor A only once
lu, piv = lu_factor(A)
solutions = []

for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    solutions.append(x)
    residual = b - A @ x
    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()

# Direct solution for comparison
print("Direct solution for first set:",
      np.linalg.solve(A, measurement_sets[0]))

width = 0.25
idx = np.arange(3)
for k, sol in enumerate(solutions):
    plt.bar(idx + k * width, sol, width, label=f"Measurement set {k + 1}")
plt.xticks(idx + width, ["x1", "x2", "x3"])
plt.ylabel("Solution value")
plt.title("LU solutions for three measurement sets")
plt.legend()
plt.grid(True, axis="y")
finish("task_07_original.png")
