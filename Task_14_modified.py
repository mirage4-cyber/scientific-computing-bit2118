import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: the model. Try a straight line, the original quadratic, and a cubic.
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)


def poly(x, *c):
    return np.polyval(c, x)


x_plot = np.linspace(50, 400, 300)
for degree, name in [(1, "Linear"), (2, "Quadratic (original)"), (3, "Cubic")]:
    params, _ = curve_fit(poly, users, response_ms, p0=np.ones(degree + 1))
    pred = poly(users, *params)
    rmse = np.sqrt(np.mean((response_ms - pred) ** 2))
    print(f"{name}: RMSE = {rmse:.2f} ms, prediction at 400 users = {poly(400, *params):.2f} ms")
    plt.plot(x_plot, poly(x_plot, *params), label=f"{name} (RMSE {rmse:.1f})")
plt.scatter(users, response_ms, color="black", label="Measurements", zorder=3)
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Effect of changing the model")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_14_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Growth of an app's monthly active users (an exponential growth curve).
months = np.arange(1, 8, dtype=float)
active = np.array([120, 150, 190, 240, 300, 380, 480], dtype=float)


def growth(t, a, b):
    return a * np.exp(b * t)


params, cov = curve_fit(growth, months, active, p0=[100, 0.2])
a, b = params
rmse = np.sqrt(np.mean((active - growth(months, a, b)) ** 2))
lin = np.polyfit(months, active, 1)
rmse_lin = np.sqrt(np.mean((active - np.polyval(lin, months)) ** 2))

print(f"Fitted model: users = {a:.2f} * exp({b:.4f} * month)")
print(f"Monthly growth rate: {np.exp(b) - 1:.2%}")
print(f"RMSE exponential = {rmse:.2f}, RMSE straight line = {rmse_lin:.2f}")
print(f"Prediction month 10: exponential = {growth(10, a, b):.0f}, straight line = {np.polyval(lin, 10):.0f}")
print(f"Prediction month 12: exponential = {growth(12, a, b):.0f}, straight line = {np.polyval(lin, 12):.0f}")

tt = np.linspace(1, 12, 200)
plt.scatter(months, active, label="Observed users", zorder=3)
plt.plot(tt, growth(tt, a, b), label="Exponential fit")
plt.plot(tt, np.polyval(lin, tt), "--", label="Straight-line fit")
plt.xlabel("Month")
plt.ylabel("Monthly active users")
plt.title("Growth curve fitting for an app")
plt.legend()
plt.grid(True)
finish("task_14_modified.png")
