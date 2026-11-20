import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
def model(x, a, b, c): return a*x**2 + b*x + c
params, covariance = curve_fit(model, users, response_ms)
predicted = model(users, *params)
rmse = np.sqrt(np.mean((response_ms-predicted)**2))
print(f"Model: y={params[0]:.6f}x^2 + {params[1]:.4f}x + {params[2]:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Prediction at 400 users: {model(400, *params):.2f} ms")
x = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measured")
plt.plot(x, model(x, *params), label="Quadratic fit")
plt.xlabel("Concurrent users"); plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fit"); plt.grid(True); plt.legend(); plt.show()
