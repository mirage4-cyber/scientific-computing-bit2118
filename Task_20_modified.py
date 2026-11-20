import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from _helpers import finish

rng = np.random.default_rng(42)

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
capacity, mean_demand = 1000.0, 850.0
# Change 1: number of simulations N
exact = norm.sf(capacity, loc=mean_demand, scale=120.0)
print(f"Exact overload probability (normal distribution, std 120): {exact:.4%}")
sizes = [100, 1_000, 10_000, 100_000, 1_000_000]
estimates = []
for n in sizes:
    est = (rng.normal(mean_demand, 120.0, n) > capacity).mean()
    estimates.append(est)
    print(f"N = {n:>9,}: estimate = {est:.4%}, error = {abs(est - exact):.4%}")

# Change 2: demand becomes more variable (std 120 -> 200)
exact2 = norm.sf(capacity, loc=mean_demand, scale=200.0)
est2 = (rng.normal(mean_demand, 200.0, 100_000) > capacity).mean()
print(f"Std = 200, N = 100,000: estimate = {est2:.4%}, exact = {exact2:.4%}")

plt.semilogx(sizes, np.array(estimates) * 100, marker="o", label="Monte Carlo estimate")
plt.axhline(exact * 100, color="red", linestyle="--", label=f"Exact = {exact:.2%}")
plt.xlabel("Number of simulations N")
plt.ylabel("Overload probability (%)")
plt.title("More simulations give a more stable estimate")
plt.legend()
plt.grid(True, which="both")
finish("task_20_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# A matatu trip is made of three random parts (minutes):
#   town traffic ~ Normal(15, 3), highway ~ Uniform(10, 20), stops ~ Exponential(mean 8).
# What is the chance that the trip takes longer than 45 minutes?
N = 200_000
traffic = rng.normal(15, 3, N)
highway = rng.uniform(10, 20, N)
stops = rng.exponential(8, N)
trip = traffic + highway + stops
late = trip > 45

p = late.mean()
se = np.sqrt(p * (1 - p) / N)
print(f"Simulated trips: {N:,}")
print(f"Mean trip time: {trip.mean():.2f} min, standard deviation: {trip.std():.2f} min")
print(f"95th percentile trip time: {np.percentile(trip, 95):.2f} min")
print(f"Probability of taking longer than 45 minutes: {p:.3%} (standard error about {se:.3%})")

plt.hist(trip, bins=80, color="steelblue", alpha=0.8)
plt.axvline(45, color="red", linestyle="--", label=f"45 min limit ({p:.1%} of trips are longer)")
plt.xlabel("Trip time (minutes)")
plt.ylabel("Number of simulated trips")
plt.title("Monte Carlo simulation of matatu trip times")
plt.legend()
finish("task_20_modified.png")
