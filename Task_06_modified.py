import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change 1: totals 20 CPU / 72 GB  ->  22 CPU / 80 GB
A = np.array([[4.0, 2.0], [8.0, 12.0]])
b_new = np.array([22.0, 80.0])
sol = np.linalg.solve(A, b_new)
print(f"New totals {b_new.tolist()}: Type A = {sol[0]:.2f}, Type B = {sol[1]:.2f}")
print("Residual norm:", np.linalg.norm(b_new - A @ sol))

# Change 2: both server types use memory and CPU in the same ratio
A_bad = np.array([[4.0, 2.0], [8.0, 4.0]])
try:
    np.linalg.solve(A_bad, np.array([20.0, 72.0]))
except np.linalg.LinAlgError as err:
    print("Proportional rows [[4, 2], [8, 4]]: LinAlgError ->", err)
print("Determinant of the proportional matrix:", np.linalg.det(A_bad))

x = np.linspace(0, 6, 100)
plt.plot(x, (22 - 4 * x) / 2, label="CPU: 4x + 2y = 22")
plt.plot(x, (80 - 8 * x) / 12, label="Memory: 8x + 12y = 80")
plt.plot(*sol, "ko", label=f"Solution ({sol[0]:.2f}, {sol[1]:.2f})")
plt.ylim(0, 10)
plt.xlabel("Type A servers (x)")
plt.ylabel("Type B servers (y)")
plt.title("Changed totals give non-whole server counts")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_06_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Two-loop DC circuit (mesh current method)
R1, R2, R3 = 10.0, 20.0, 30.0     # ohms
V1, V2 = 12.0, 6.0                # volts
# Loop 1: (R1 + R2) I1 - R2 I2 = V1
# Loop 2: -R2 I1 + (R2 + R3) I2 = -V2
A = np.array([[R1 + R2, -R2], [-R2, R2 + R3]])
b = np.array([V1, -V2])
I1, I2 = np.linalg.solve(A, b)
shared = I1 - I2
print(f"Mesh current I1 = {I1:.4f} A, I2 = {I2:.4f} A")
print(f"Current through the shared resistor R2 = {shared:.4f} A")
print(f"Check loop 1: R1*I1 + R2*(I1 - I2) = {R1 * I1 + R2 * shared:.4f} V (supply {V1} V)")
print("Residual norm:", np.linalg.norm(b - A @ np.array([I1, I2])))

plt.bar(["I1 (loop 1)", "I2 (loop 2)", "I through R2"], [I1, I2, shared])
plt.ylabel("Current (A)")
plt.title("Mesh currents in the two-loop circuit")
plt.grid(True, axis="y")
finish("task_06_modified.png")
