import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
# Estimate probability that two dice total at least 10
n = 100_000
die1 = rng.integers(1, 7, n)
die2 = rng.integers(1, 7, n)
success = (die1 + die2 >= 10)
estimate = success.mean()
exact = 6/36
standard_error = np.sqrt(estimate*(1-estimate)/n)
print(f"Monte Carlo estimate: {estimate:.5f}")
print(f"Exact probability: {exact:.5f}")
print(f"Estimated standard error: {standard_error:.5f}")
print(f"Absolute error: {abs(estimate-exact):.5f}")

# Parameter variation: increase number of trials
for trials in [100, 1000, 10000, 100000]:
    a = rng.integers(1, 7, trials)
    b = rng.integers(1, 7, trials)
    print(f"{trials:>6} trials -> {(a+b>=10).mean():.5f}")
plt.bar(["Monte Carlo", "Exact"], [estimate, exact])
plt.ylabel("Probability"); plt.title("Dice probability estimate"); plt.show()
