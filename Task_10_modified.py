import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from _helpers import finish


def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)


def g(T):
    return 25 + 10 * np.exp(-T / 20)


def fixed_point(g, x0, tol=1e-10, max_iter=200):
    hist = [x0]
    for _ in range(max_iter):
        new = g(hist[-1])
        hist.append(new)
        if abs(new - hist[-2]) < tol:
            break
    return hist


# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change 1: bisection tolerance 1e-2, 1e-6, 1e-10
for xtol in (1e-2, 1e-6, 1e-10):
    sol = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=xtol)
    print(f"Bisection xtol={xtol:.0e}: root={sol.root:.8f} C, iterations={sol.iterations}")
# Change 2: starting guess of fixed-point iteration 30 -> 100 and 0
root_ref = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-12).root
for start in (30.0, 100.0, 0.0):
    h = fixed_point(g, start)
    print(f"Fixed point from T0={start:>5}: root={h[-1]:.8f} C, iterations={len(h) - 1}")
    plt.semilogy(np.abs(np.array(h) - root_ref) + 1e-16, marker="o", label=f"Start at {start:g} C")

plt.xlabel("Iteration")
plt.ylabel("Distance from the root (C)")
plt.title("Fixed-point iteration from different starting guesses")
plt.legend()
plt.grid(True, which="both")
finish("task_10_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Break-even number of rides per week for a boda boda business (amounts in KES).
# Revenue = 250 per ride. Cost = 4000 fixed + 60 per ride + 0.5 * rides^1.5 (extra wear and fuel).
def profit(x):
    return 250 * x - (4000 + 60 * x + 0.5 * x ** 1.5)


def g_profit(x):
    return (4000 + 60 * x + 0.5 * x ** 1.5) / 250   # x = cost / price per ride


sol = root_scalar(profit, bracket=[1, 100], method="bisect", xtol=1e-8)
h = fixed_point(g_profit, 10.0, tol=1e-8)
print(f"Bisection break-even: {sol.root:.4f} rides per week ({sol.iterations} iterations)")
print(f"Fixed-point break-even: {h[-1]:.4f} rides per week ({len(h) - 1} iterations)")
print(f"Profit at the break-even point: {profit(sol.root):.6f} KES")
print(f"Profit at 30 rides: {profit(30):.2f} KES")

xs = np.linspace(1, 60, 200)
plt.plot(xs, 250 * xs, label="Revenue")
plt.plot(xs, 4000 + 60 * xs + 0.5 * xs ** 1.5, label="Cost")
plt.axvline(sol.root, linestyle="--", label=f"Break-even = {sol.root:.1f} rides")
plt.xlabel("Rides per week")
plt.ylabel("KES")
plt.title("Break-even point of a boda boda business")
plt.legend()
plt.grid(True)
finish("task_10_modified.png")
