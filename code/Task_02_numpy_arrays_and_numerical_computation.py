import numpy as np

# Hourly temperature readings from a weather station (degrees Celsius)
temperatures = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8,
                          25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6,
                          26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])

print(f"Mean: {np.mean(temperatures):.2f} C")
print(f"Minimum: {np.min(temperatures):.2f} C")
print(f"Maximum: {np.max(temperatures):.2f} C")
fahrenheit = temperatures * 9/5 + 32
print("First six Fahrenheit values:", np.round(fahrenheit[:6], 2))

# Parameter variation: add 2 C to every reading (a warmer day)
warmer = temperatures + 2
print(f"Warmer-day mean: {np.mean(warmer):.2f} C")
