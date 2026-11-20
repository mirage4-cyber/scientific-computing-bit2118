import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: capacitance C = 0.001 F -> 0.002 F (time constant RC = 1 s -> 2 s)
Vs, R = 5.0, 1000.0
t_eval = np.linspace(0, 5, 501)
for C in (0.001, 0.002):
    sol = solve_ivp(lambda t, V: [(Vs - V[0]) / (R * C)], (0, 5), [0.0],
                    t_eval=t_eval, rtol=1e-9, atol=1e-11)
    V = sol.y[0]
    t63 = np.interp(0.632 * Vs, V, sol.t)          # time to reach 63.2 % of the supply
    print(f"C = {C} F (RC = {R * C:.0f} s): V(1 s) = {np.interp(1, sol.t, V):.3f} V, "
          f"V(5 s) = {V[-1]:.3f} V, time to 63.2 % = {t63:.2f} s")
    plt.plot(sol.t, V, label=f"C = {C} F (RC = {R * C:.0f} s)")

plt.axhline(0.632 * Vs, color="grey", linestyle=":", label="63.2 % of supply")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("Larger capacitance charges more slowly")
plt.legend(fontsize=8)
plt.grid(True)
finish("task_18_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# SIR epidemic model for a campus of 5,000 students.
# S' = -beta*S*I/N, I' = beta*S*I/N - gamma*I, R' = gamma*I
N = 5000.0
gamma = 0.1                      # recovery rate per day (about 10 days infectious)


def sir(t, y, beta):
    S, I, Rr = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]


days = np.linspace(0, 160, 1601)
plt.figure()
for beta, label in [(0.4, "beta = 0.4 (normal contact)"), (0.2, "beta = 0.2 (reduced contact)")]:
    sol = solve_ivp(sir, (0, 160), [N - 5, 5, 0], args=(beta,), t_eval=days, rtol=1e-8, atol=1e-8)
    S, I, Rr = sol.y
    peak = I.argmax()
    print(f"{label}: R0 = {beta / gamma:.1f}, peak infected = {I[peak]:.0f} students on day {sol.t[peak]:.1f}, "
          f"total ever infected = {Rr[-1]:.0f} ({Rr[-1] / N:.1%})")
    plt.plot(sol.t, I, label=label)

plt.xlabel("Day")
plt.ylabel("Students infected at the same time")
plt.title("SIR epidemic on a campus of 5,000 students")
plt.legend()
plt.grid(True)
finish("task_18_modified.png")
