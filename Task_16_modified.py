import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from _helpers import finish

trapezoid = getattr(np, "trapezoid", None) or np.trapz

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
t = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
p = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
print(f"Original: trapezoid = {trapezoid(p, t):.3f} kWh, Simpson = {simpson(p, x=t):.3f} kWh")

# Change 1: the 06:00 reading rises from 1.8 kW to 2.6 kW
p2 = p.copy()
p2[3] = 2.6
print(f"Peak reading 1.8 -> 2.6 kW: trapezoid = {trapezoid(p2, t):.3f} kWh, Simpson = {simpson(p2, x=t):.3f} kWh")

# Change 2: only every second reading is kept (sampling every 4 hours)
t4, p4 = t[::2], p[::2]
print(f"Sampling every 4 h ({t4.tolist()}): trapezoid = {trapezoid(p4, t4):.3f} kWh, Simpson = {simpson(p4, x=t4):.3f} kWh")

plt.plot(t, p, marker="o", label="Original (every 2 h)")
plt.plot(t, p2, marker="o", label="Peak raised to 2.6 kW")
plt.plot(t4, p4, marker="s", linestyle="--", label="Every 4 h only")
plt.xlabel("Time (hours)")
plt.ylabel("Power (kW)")
plt.title("Effect of changing the readings")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_16_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Distance travelled by a vehicle from speed readings every 5 s.
# The true speed is v(t) = 20 * (1 - exp(-t / 15)) m/s, so the exact distance is
# d(60) = 20 * (60 + 15 * exp(-60 / 15) - 15). The readings are rounded to 2 decimals.
tt = np.arange(0, 65, 5, dtype=float)
v = np.round(20 * (1 - np.exp(-tt / 15)), 2)
exact = 20 * (60 + 15 * np.exp(-60 / 15) - 15)
d_trap = trapezoid(v, tt)
d_simp = simpson(v, x=tt)
print(f"Readings: {len(tt)} speeds from t = 0 s to t = 60 s")
print(f"Distance by trapezoidal rule: {d_trap:.2f} m (error {abs(d_trap - exact):.2f} m)")
print(f"Distance by Simpson's rule: {d_simp:.2f} m (error {abs(d_simp - exact):.2f} m)")
print(f"Exact distance: {exact:.2f} m")
print(f"Average speed over the minute: {d_simp / 60:.2f} m/s ({d_simp / 60 * 3.6:.1f} km/h)")

fine = np.linspace(0, 60, 300)
plt.plot(fine, 20 * (1 - np.exp(-fine / 15)), label="True speed")
plt.plot(tt, v, "o", label="Readings every 5 s")
plt.fill_between(tt, v, alpha=0.2, label=f"Area = distance = {d_simp:.0f} m")
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Distance from speed readings")
plt.legend()
plt.grid(True)
finish("task_16_modified.png")
