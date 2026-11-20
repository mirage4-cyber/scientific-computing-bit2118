import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu_factor, lu_solve
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: the middle diagonal coefficient A[1,1] from 4 to 8
A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
A_new = A.copy()
A_new[1, 1] = 8.0
b = np.array([15.0, 10.0, 10.0])
x_old = lu_solve(lu_factor(A), b)
x_new = lu_solve(lu_factor(A_new), b)
print("Original solution:", x_old)
print("Changed solution :", x_new)
print("Residual norm (changed):", np.linalg.norm(b - A_new @ x_new))

idx = np.arange(3)
plt.bar(idx - 0.2, x_old, 0.4, label="A[1,1] = 4")
plt.bar(idx + 0.2, x_new, 0.4, label="A[1,1] = 8")
plt.xticks(idx, ["x1", "x2", "x3"])
plt.ylabel("Solution value")
plt.title("Effect of changing one coefficient")
plt.legend()
plt.grid(True, axis="y")
finish("task_07_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Transient heat conduction in a metal rod (implicit time stepping).
# The same matrix is used at every time step, so it is factored once.
n, r, steps = 300, 0.5, 2000
T_left, T_right = 100.0, 20.0
M = (np.diag(np.full(n, 1 + 2 * r))
     + np.diag(np.full(n - 1, -r), 1)
     + np.diag(np.full(n - 1, -r), -1))
bc = np.zeros(n)
bc[0], bc[-1] = r * T_left, r * T_right


def run_lu():
    lu, piv = lu_factor(M)
    T = np.full(n, 20.0)
    snaps = {}
    for s in range(1, steps + 1):
        T = lu_solve((lu, piv), T + bc)
        if s in (10, 100, 500, 2000):
            snaps[s] = T.copy()
    return T, snaps


def run_direct():
    T = np.full(n, 20.0)
    for _ in range(steps):
        T = np.linalg.solve(M, T + bc)
    return T


t0 = time.perf_counter(); T_lu, snaps = run_lu(); t_lu = time.perf_counter() - t0
t0 = time.perf_counter(); T_direct = run_direct(); t_direct = time.perf_counter() - t0

print(f"Rod nodes: {n}, time steps: {steps}")
print(f"LU (factor once) time: {t_lu:.3f} s")
print(f"Solve every step time: {t_direct:.3f} s")
print(f"Speed-up: {t_direct / t_lu:.1f}x")
print(f"Largest difference between the two results: {np.max(np.abs(T_lu - T_direct)):.2e} C")
print(f"Temperature at node 10 after {steps} steps: {T_lu[10]:.2f} C")

pos = np.arange(1, n + 1)
for s, prof in snaps.items():
    plt.plot(pos, prof, label=f"After {s} steps")
plt.xlabel("Position along rod (node)")
plt.ylabel("Temperature (C)")
plt.title("Heat spreading along a rod (hot end 100 C)")
plt.legend()
plt.grid(True)
finish("task_07_modified.png")
