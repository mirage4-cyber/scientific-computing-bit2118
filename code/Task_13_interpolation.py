import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18., 20., 22.5, 24., 25., 25.5, 25.])
linear = interp1d(hours, temperature)
cubic = CubicSpline(hours, temperature)
target = 10.5
print(f"Linear estimate at 10:30: {float(linear(target)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(target)):.2f} C")
fine = np.arange(8, 14 + 1/6, 1/6)
plt.scatter(hours, temperature, label="Measurements")
plt.plot(fine, linear(fine), label="Linear")
plt.plot(fine, cubic(fine), label="Cubic spline")
plt.xlabel("Hour"); plt.ylabel("Temperature (C)")
plt.title("Hourly temperature interpolation"); plt.grid(True); plt.legend(); plt.show()
