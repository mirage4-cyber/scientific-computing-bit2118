import numpy as np
import matplotlib.pyplot as plt


time = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16], dtype=float)
position = np.array([0.0, 20.0, 36.0, 46.0, 50.0, 53.0, 61.0, 75.0, 94.0])

speed = np.zeros_like(position)


speed[0] = (position[1] - position[0]) / (time[1] - time[0])


for i in range(1, len(time) - 1):
    speed[i] = (position[i + 1] - position[i - 1]) / (time[i + 1] - time[i - 1])


speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, speed={v:.2f} m/s ({v * 3.6:.1f} km/h)")

plt.plot(time, speed * 3.6, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (km/h)")
plt.title("Boda boda speed estimated from GPS data")
plt.grid(True)
plt.show()