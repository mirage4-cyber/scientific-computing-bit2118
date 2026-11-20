import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish


def jacobi(A, b, tol=1e-8, max_iter=20000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        x = x_new
        if error < tol:
            break
    return x, errors


def gauss_seidel(A, b, tol=1e-8, max_iter=20000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ old[i + 1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            break
    return x, errors


# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: the stopping tolerance 1e-8 -> 1e-3, 1e-6 and 1e-10
A = np.array([
    [2., -1., 0., 0., 0.], [-1., 2., -1., 0., 0.], [0., -1., 2., -1., 0.],
    [0., 0., -1., 2., -1.], [0., 0., 0., -1., 2.]
])
b = np.array([100., 0., 0., 0., 20.])
exact = np.linalg.solve(A, b)
tols = [1e-3, 1e-6, 1e-10]
it_j, it_gs = [], []
for tol in tols:
    xj, ej = jacobi(A, b, tol=tol)
    xg, eg = gauss_seidel(A, b, tol=tol)
    it_j.append(len(ej))
    it_gs.append(len(eg))
    print(f"tol={tol:.0e}: Jacobi {len(ej):>3} iterations (max error {np.max(np.abs(xj - exact)):.2e}), "
          f"Gauss-Seidel {len(eg):>3} iterations (max error {np.max(np.abs(xg - exact)):.2e})")

w = 0.35
idx = np.arange(len(tols))
plt.bar(idx - w / 2, it_j, w, label="Jacobi")
plt.bar(idx + w / 2, it_gs, w, label="Gauss-Seidel")
plt.xticks(idx, [f"{t:.0e}" for t in tols])
plt.xlabel("Tolerance")
plt.ylabel("Iterations needed")
plt.title("Stricter tolerance needs more iterations")
plt.legend()
plt.grid(True, axis="y")
finish("task_08_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Steady-state temperature of a square metal plate on a 10 x 10 grid of interior points.
# Top edge = 100 C, other three edges = 0 C. Each point is the average of its 4 neighbours.
m = 10
N = m * m
A = np.zeros((N, N))
b = np.zeros(N)
for i in range(m):
    for j in range(m):
        k = i * m + j
        A[k, k] = 4.0
        if i > 0: A[k, k - m] = -1.0
        if i < m - 1: A[k, k + m] = -1.0
        if j > 0: A[k, k - 1] = -1.0
        if j < m - 1: A[k, k + 1] = -1.0
        if i == 0:
            b[k] = 100.0      # neighbour is the hot top edge

x_j, err_j = jacobi(A, b, tol=1e-6)
x_gs, err_gs = gauss_seidel(A, b, tol=1e-6)
x_direct = np.linalg.solve(A, b)

print(f"Unknown temperatures: {N}")
print(f"Jacobi iterations: {len(err_j)}, Gauss-Seidel iterations: {len(err_gs)}")
print(f"Largest difference from the direct solution: Jacobi {np.max(np.abs(x_j - x_direct)):.2e}, "
      f"Gauss-Seidel {np.max(np.abs(x_gs - x_direct)):.2e}")
grid = x_direct.reshape(m, m)
print(f"Temperature at the plate centre (row 5, column 5): {grid[5, 5]:.2f} C")
print(f"Temperature next to the hot edge (row 0, column 5): {grid[0, 5]:.2f} C")

plt.imshow(grid, cmap="hot", origin="upper")
plt.colorbar(label="Temperature (C)")
plt.xlabel("Column")
plt.ylabel("Row (0 is next to the hot edge)")
plt.title("Steady-state temperature of a heated plate")
finish("task_08_modified.png")
