import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: the 10:00 reading is recorded wrongly as 28.0 C instead of 22.5 C
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
good = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
bad = good.copy()
bad[2] = 28.0
t = np.linspace(8, 14, 121)
for name, data in [("Original", good), ("10:00 reading = 28.0", bad)]:
    lin = interp1d(hours, data)
    cub = CubicSpline(hours, data)
    print(f"{name}: at 09:30 linear={float(lin(9.5)):.2f}, cubic={float(cub(9.5)):.2f}; "
          f"at 10:30 linear={float(lin(10.5)):.2f}, cubic={float(cub(10.5)):.2f}; "
          f"cubic maximum between readings={cub(t).max():.2f} C")

plt.scatter(hours, bad, color="red", zorder=3, label="Readings with error")
plt.plot(t, CubicSpline(hours, bad)(t), label="Cubic spline (with error)")
plt.plot(t, CubicSpline(hours, good)(t), "--", label="Cubic spline (original)")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("One wrong reading changes the whole curve nearby")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_13_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Fuel-gauge calibration: the sensor gives a voltage, and a calibration table gives litres.
volts = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.5])
litres = np.array([0.0, 4.0, 9.0, 16.0, 31.0, 43.0, 48.0])
linear = interp1d(volts, litres)
cubic = CubicSpline(volts, litres)
readings = [1.2, 2.5, 3.6]
for v in readings:
    print(f"Sensor {v:.1f} V: linear = {float(linear(v)):.2f} L, cubic = {float(cubic(v)):.2f} L")
print(f"Largest difference between the two methods over the table range: "
      f"{np.max(np.abs(linear(np.linspace(0.5, 4.5, 400)) - cubic(np.linspace(0.5, 4.5, 400)))):.2f} L")

vv = np.linspace(0.5, 4.5, 200)
plt.scatter(volts, litres, label="Calibration table", zorder=3)
plt.plot(vv, linear(vv), label="Linear")
plt.plot(vv, cubic(vv), label="Cubic spline")
plt.xlabel("Sensor voltage (V)")
plt.ylabel("Fuel in tank (litres)")
plt.title("Fuel-gauge calibration by interpolation")
plt.legend()
plt.grid(True)
finish("task_13_modified.png")
