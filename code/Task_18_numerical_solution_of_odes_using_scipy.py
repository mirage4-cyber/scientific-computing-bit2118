import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# RC circuit discharge: dV/dt = -V/(RC)
R = 1000.0       # ohms
C = 0.001        # farads
V0 = 12.0        # volts
tau = R*C
def rhs(t, voltage): return -voltage/tau

solution = solve_ivp(rhs, (0, 5), [V0], dense_output=True, rtol=1e-8, atol=1e-10)
time = np.linspace(0, 5, 200)
voltage = solution.sol(time)[0]
exact = V0*np.exp(-time/tau)
print(f"Voltage at 5 seconds: {solution.y[0,-1]:.4f} V")
print(f"Exact value: {exact[-1]:.4f} V")
print(f"Error: {abs(solution.y[0,-1]-exact[-1]):.8f} V")
plt.plot(time, voltage, label="solve_ivp")
plt.plot(time, exact, "--", label="Exact")
plt.xlabel("Time (s)"); plt.ylabel("Voltage (V)")
plt.title("RC capacitor discharge"); plt.grid(True); plt.legend(); plt.show()
