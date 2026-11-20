import math
import numpy as np
import matplotlib.pyplot as plt
from _helpers import finish

# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change: use more and more digits of sqrt(2) as the approximation
true_value = np.sqrt(2)
approximations = [1.4, 1.41, 1.414, 1.4142, 1.41421, 1.414213562]
abs_errs, rel_errs = [], []
for approx in approximations:
    ae = abs(true_value - approx)
    re = ae / true_value
    abs_errs.append(ae)
    rel_errs.append(re)
    print(f"approx={approx:<12}: absolute error={ae:.3e}, relative error={re:.4%}")

plt.semilogy(range(1, 7), rel_errs, marker="o")
plt.xticks(range(1, 7), [str(a) for a in approximations], rotation=30)
plt.xlabel("Approximation used for sqrt(2)")
plt.ylabel("Relative error (log scale)")
plt.title("More digits give a smaller error")
plt.grid(True, which="both")
finish("task_04_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# Mobile-money fee totals: a fee of KES 0.10 is added once per transaction.
# Naive floating-point sum versus math.fsum versus exact integer cents.
fee = 0.10
counts = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
naive_errors = []
for n in counts:
    naive = 0.0
    for _ in range(n):
        naive += fee
    exact = (n * 10) / 100          # integer cents / 100
    fsum = math.fsum([fee] * n)
    err = abs(naive - exact)
    naive_errors.append(err)
    print(f"n={n:>9,}: naive={naive:.10f}, fsum={fsum:.10f}, exact={exact:.2f}, naive error={err:.3e}")

plt.loglog(counts, np.maximum(naive_errors, 1e-17), marker="o")
plt.xlabel("Number of transactions")
plt.ylabel("Absolute error in total fees (KES)")
plt.title("Round-off error accumulates when adding 0.10 repeatedly")
plt.grid(True, which="both")
finish("task_04_modified.png")
