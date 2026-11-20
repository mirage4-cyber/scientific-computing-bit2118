import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: the cost of one Type B unit rises from 18 to 22 (Type A stays at 12)
def solve_servers(cost_b):
    cons = {"type": "ineq", "fun": lambda z: 100 * z[0] + 170 * z[1] - 1000}
    res = minimize(lambda z: 12 * z[0] + cost_b * z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)], constraints=cons)
    best = None
    for a in range(0, 20):
        for b in range(0, 20):
            if 100 * a + 170 * b >= 1000:
                c = 12 * a + cost_b * b
                if best is None or c < best[0]:
                    best = (c, a, b)
    return res, best


for cost_b in (18, 22):
    res, best = solve_servers(cost_b)
    print(f"Cost of B = {cost_b}: A = {res.x[0]:.3f}, B = {res.x[1]:.3f}, "
          f"cost = {res.fun:.2f}; best whole-server answer (cost, A, B) = {best}")

xs = np.linspace(0, 10, 100)
plt.plot(xs, (1000 - 100 * xs) / 170, label="Capacity = 1000")
plt.fill_between(xs, (1000 - 100 * xs) / 170, 8, alpha=0.15)
for cost_b, marker in ((18, "ko"), (22, "rs")):
    res, _ = solve_servers(cost_b)
    plt.plot(*res.x, marker, label=f"Optimum when B costs {cost_b}: ({res.x[0]:.2f}, {res.x[1]:.2f})")
plt.xlim(0, 10)
plt.ylim(0, 8)
plt.xlabel("Type A units")
plt.ylabel("Type B units")
plt.title("The optimum jumps to a different corner")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_19_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# A farm needs at least 60 kg of nitrogen and 40 kg of phosphorus.
# Bag A: 12 kg N, 4 kg P, costs KES 2,500.  Bag B: 6 kg N, 10 kg P, costs KES 3,200.
def fert_cost(z):
    # cost in thousands of KES (keeps the numbers small so the solver behaves well)
    return 2.5 * z[0] + 3.2 * z[1]


cons = [
    {"type": "ineq", "fun": lambda z: 12 * z[0] + 6 * z[1] - 60},     # nitrogen
    {"type": "ineq", "fun": lambda z: 4 * z[0] + 10 * z[1] - 40},     # phosphorus
]
res = minimize(fert_cost, x0=[5, 5], method="SLSQP", bounds=[(0, None), (0, None)], constraints=cons)
a, b = res.x
print(f"Optimization success: {res.success}")
print(f"Bags of A: {a:.3f}, bags of B: {b:.3f}")
print(f"Nitrogen supplied: {12 * a + 6 * b:.2f} kg, phosphorus supplied: {4 * a + 10 * b:.2f} kg")
print(f"Minimum cost: KES {res.fun * 1000:,.0f}")

best = None
for i in range(0, 15):
    for j in range(0, 15):
        if 12 * i + 6 * j >= 60 and 4 * i + 10 * j >= 40:
            c = 2500 * i + 3200 * j
            if best is None or c < best[0]:
                best = (c, i, j)
print(f"Best whole-bag answer (cost, A, B): {best}")

xs = np.linspace(0, 12, 200)
n_line = (60 - 12 * xs) / 6
p_line = (40 - 4 * xs) / 10
plt.plot(xs, n_line, label="Nitrogen = 60 kg")
plt.plot(xs, p_line, label="Phosphorus = 40 kg")
plt.fill_between(xs, np.maximum(np.maximum(n_line, p_line), 0), 12, alpha=0.15, label="Feasible region")
plt.plot(a, b, "ko", label=f"Optimum ({a:.2f}, {b:.2f})")
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xlabel("Bags of A")
plt.ylabel("Bags of B")
plt.title("Cheapest fertiliser mix")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_19_modified.png")
