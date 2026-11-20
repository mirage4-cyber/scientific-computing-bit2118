import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def heat_balance(T):
    return T - 25 - 10*np.exp(-T/20)

bisect = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10)
def g(T): return 25 + 10*np.exp(-T/20)
T = 30.0
history = [T]
for _ in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10: break
    T = T_new

print(f"Bisection root: {bisect.root:.6f} C")
print(f"Fixed-point root: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history)-1)
x = np.linspace(20, 40, 300)
plt.plot(x, heat_balance(x)); plt.axhline(0); plt.axvline(bisect.root, linestyle="--")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat balance")
plt.title("Equilibrium root"); plt.grid(True); plt.show()
