import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from _helpers import finish

# x = number/capacity units of Type A server
# y = number/capacity units of Type B server
#
# Cost per unit: A = 12, B = 18
# Capacity per unit: A = 100, B = 170
# Required total capacity: at least 1000

def cost(z):
    x, y = z
    return 12*x + 18*y


def capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000


constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# If whole servers are required, test nearby integer combinations.
best_integer = None
for a in range(0, 20):
    for b in range(0, 20):
        capacity = 100*a + 170*b
        if capacity >= 1000:
            total_cost = 12*a + 18*b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("Best nearby integer solution (cost, A, B, capacity):", best_integer)

xs = np.linspace(0, 10, 100)
plt.plot(xs, (1000 - 100 * xs) / 170, label="Capacity = 1000")
plt.fill_between(xs, (1000 - 100 * xs) / 170, 8, alpha=0.15, label="Feasible region")
plt.plot(x, y, "ko", label=f"Optimum ({x:.2f}, {y:.2f})")
plt.xlim(0, 10)
plt.ylim(0, 8)
plt.xlabel("Type A units")
plt.ylabel("Type B units")
plt.title("Minimum-cost server allocation")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_19_original.png")
