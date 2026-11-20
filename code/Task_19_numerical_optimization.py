import numpy as np
from scipy.optimize import minimize

# Minimize cost C(x) = (x-4)^2 + 3, subject to x >= 0
def cost(x): return (x[0]-4)**2 + 3
result = minimize(cost, x0=[0.0], method="BFGS")
print("Optimal x:", result.x[0])
print("Minimum cost:", result.fun)
print("Success:", result.success, result.message)

# Parameter variation: change target from 4 to 7
def changed_cost(x): return (x[0]-7)**2 + 3
changed = minimize(changed_cost, x0=[1.0], method="BFGS")
print("Changed optimum:", changed.x[0], "minimum:", changed.fun)
