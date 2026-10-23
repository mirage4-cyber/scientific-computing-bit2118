import numpy as np
import matplotlib.pyplot as plt

# Tea cooling: dT/dt = -k(T - T_ambient)
T_ambient = 22.0
T_initial = 85.0
k = 0.08
h = 1.0  # minutes
end_time = 30.0

def cooling_rate(T):
    return -k * (T - T_ambient)

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * cooling_rate(temperature[i])

exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

# First time the tea is at or below 60 C
drinkable = time[temperature <= 60][0]

print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} C")
print(f"Tea reaches 60 C after about {drinkable:.0f} minutes (Euler)")

plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.axhline(60, linestyle="--", linewidth=0.8, label="60 C")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a cup of tea")
plt.legend()
plt.grid(True)
plt.show()