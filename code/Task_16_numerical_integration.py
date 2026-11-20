import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
trapezoid = np.trapezoid(power_kw, time_hours)
simpson_result = simpson(power_kw, x=time_hours)
print(f"Trapezoidal energy: {trapezoid:.3f} kWh")
print(f"Simpson energy: {simpson_result:.3f} kWh")
print(f"Difference: {abs(simpson_result-trapezoid):.3f} kWh")
plt.plot(time_hours, power_kw, marker="o")
plt.fill_between(time_hours, power_kw, alpha=0.2)
plt.xlabel("Time (hours)"); plt.ylabel("Power (kW)")
plt.title("Power readings and accumulated energy"); plt.grid(True); plt.show()
