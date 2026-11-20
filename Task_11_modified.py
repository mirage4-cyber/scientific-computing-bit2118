import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from _helpers import finish


def make_functions(cash_flows):
    def npv(rate):
        return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))

    def d_npv(rate):
        return sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cash_flows) if t > 0)

    return npv, d_npv


# ---------------------------------------------------------------
print("=== PARAMETER CHANGE ===")
# Change 1: initial investment 10,000 -> 9,000 and 12,000
rates = np.linspace(0, 0.5, 200)
for invest in (9000, 10000, 12000):
    cfs = [-invest, 3000, 3500, 4000, 2500]
    npv, d_npv = make_functions(cfs)
    nw = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
    print(f"Investment {invest:>6}: IRR = {nw.root:.4%} (Newton, {nw.iterations} iterations)")
    plt.plot(rates * 100, [npv(r) for r in rates], label=f"Investment {invest}")
# Change 2: starting guess 0.10 -> 0.50 for the original investment
npv, d_npv = make_functions([-10000, 3000, 3500, 4000, 2500])
for x0 in (0.10, 0.50):
    nw = root_scalar(npv, fprime=d_npv, x0=x0, method="newton", xtol=1e-12)
    print(f"Newton from x0={x0}: IRR = {nw.root:.4%}, iterations = {nw.iterations}")

plt.axhline(0, color="black", linewidth=0.8)
plt.xlabel("Discount rate (%)")
plt.ylabel("Net present value")
plt.title("NPV curves for different initial investments")
plt.legend()
plt.grid(True)
finish("task_11_changed.png")

# ---------------------------------------------------------------
print("=== MODIFIED CASE ===")
# True monthly cost of a loan. The borrower receives 100,000 but pays a 2,000 fee up front,
# then repays 9,500 at the end of each of 12 months.
cash_flows = [98000] + [-9500] * 12
npv, d_npv = make_functions(cash_flows)
newton = root_scalar(npv, fprime=d_npv, x0=0.01, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.01, x1=0.05, method="secant", xtol=1e-12)
monthly = newton.root
annual = (1 + monthly) ** 12 - 1
flat_rate = (9500 * 12 - 100000) / 100000

print(f"Monthly rate (Newton-Raphson): {monthly:.4%} ({newton.iterations} iterations)")
print(f"Monthly rate (Secant): {secant.root:.4%} ({secant.iterations} iterations)")
print(f"Effective annual rate: {annual:.2%}")
print(f"Quoted flat rate for comparison: {flat_rate:.2%} per year")
print(f"NPV at the solution: {npv(monthly):.6f}")

rs = np.linspace(0.0, 0.06, 200)
plt.plot(rs * 100, [npv(r) for r in rs])
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(monthly * 100, linestyle="--", label=f"Monthly rate = {monthly:.2%}")
plt.xlabel("Monthly rate (%)")
plt.ylabel("NPV of the borrower's cash flows (KES)")
plt.title("Finding the true monthly interest rate of a loan")
plt.legend()
plt.grid(True)
finish("task_11_modified.png")
