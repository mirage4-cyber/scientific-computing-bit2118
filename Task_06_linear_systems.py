import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish

# x = number of Type A servers
# y = number of Type B servers
#
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total observed usage: 20 CPU units and 72 GB memory
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])
b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

x = np.linspace(0, 6, 100)
plt.plot(x, (b[0] - A[0, 0] * x) / A[0, 1], label="CPU: 4x + 2y = 20")
plt.plot(x, (b[1] - A[1, 0] * x) / A[1, 1], label="Memory: 8x + 12y = 72")
plt.plot(*solution, "ko", label=f"Solution ({solution[0]:.0f}, {solution[1]:.0f})")
plt.xlabel("Type A servers (x)")
plt.ylabel("Type B servers (y)")
plt.title("Two equations, one intersection")
plt.ylim(0, 10)
plt.legend()
plt.grid(True)
finish("task_06_original.png")
