import numpy as np

calculated = 0.1 + 0.2
expected = 0.3
print("0.1 + 0.2 =", calculated)
print("Exact equality:", calculated == expected)
print("Tolerance comparison:", np.isclose(calculated, expected))

true_value = np.sqrt(2)
approximation = 1.414
absolute_error = abs(true_value - approximation)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# Cancellation example: stable alternative
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:g}: direct={direct:.12f}, stable={stable:.12f}")
