import numpy as np

# Two server types: CPU and memory resource equations
# Type A: 4 CPU units, 8 GB RAM; Type B: 2 CPU units, 12 GB RAM
A = np.array([[4., 2.], [8., 12.]])
b = np.array([20., 72.])
solution = np.linalg.solve(A, b)
print(f"Type A servers: {solution[0]:.2f}")
print(f"Type B servers: {solution[1]:.2f}")
print("Check A @ x =", A @ solution)
print("Residual =", b - A @ solution)

# Parameter variation: CPU total rises to 24
b_changed = np.array([24., 72.])
print("Changed resource solution:", np.linalg.solve(A, b_changed))
