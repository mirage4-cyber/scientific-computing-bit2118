import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: add 5 C to the afternoon readings (10:00 to 16:00) to simulate a hot day
base = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])
hot = base.copy()
hot[10:17] += 5.0

for name, data in [("Original", base), ("Hot afternoon (+5 C, 10:00-16:00)", hot)]:
    print(f"{name}: mean={data.mean():.2f} C, min={data.min():.2f} C, max={data.max():.2f} C")
print("First six Fahrenheit readings (unchanged hours):", (1.8 * hot + 32)[:6])

hours = np.arange(24)
plt.plot(hours, base, marker="o", label="Original")
plt.plot(hours, hot, marker="o", label="Hot afternoon")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Effect of changing the afternoon readings")
plt.legend()
plt.grid(True)
finish("task_02_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# IoT water-tank level sensor: 24 hourly readings in cm.
# Tank floor area = 0.5 m^2, so 1 cm of water = 5 litres.
tank_cm = np.array([
    92, 91, 90.5, 90, 89.5, 88,
    80, 70, 62, 58, 55, 52,
    50, 47, 45, 42, 40, 38,
    60, 85, 95, 94, 93, 92
], dtype=float)
litres = tank_cm * 5          # vectorized conversion
alert_level_cm = 45.0
below = tank_cm < alert_level_cm

print(f"Mean level: {tank_cm.mean():.2f} cm ({litres.mean():.0f} litres)")
print(f"Lowest level: {tank_cm.min():.1f} cm ({litres.min():.0f} litres) at hour {tank_cm.argmin()}")
print(f"Highest level: {tank_cm.max():.1f} cm at hour {tank_cm.argmax()}")
print(f"Hours below the {alert_level_cm:.0f} cm alert level: {below.sum()} (hours {np.flatnonzero(below).tolist()})")

plt.plot(hours, tank_cm, marker="o", label="Water level")
plt.axhline(alert_level_cm, color="red", linestyle="--", label="Refill alert (45 cm)")
plt.xlabel("Hour of day")
plt.ylabel("Water level (cm)")
plt.title("IoT water-tank level over 24 hours")
plt.legend()
plt.grid(True)
finish("task_02_modified.png")
