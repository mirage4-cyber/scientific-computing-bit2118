import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from _helpers import finish

trapezoid = getattr(np, "trapezoid", None) or np.trapz  # works on old and new NumPy

# Smart-meter readings taken every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

energy_trapezoid = trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson-energy_trapezoid):.3f} kWh")

plt.plot(time_hours, power_kw, marker="o")
plt.fill_between(time_hours, power_kw, alpha=0.3,
                 label=f"Area = energy = {energy_trapezoid:.2f} kWh")
plt.xlabel("Time (hours)")
plt.ylabel("Power (kW)")
plt.title("Smart-meter power and energy used")
plt.legend()
plt.grid(True)
finish("task_16_original.png")
