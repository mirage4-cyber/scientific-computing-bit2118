# Task 4: Floating-Point Arithmetic and Numerical Errors

**Program files:** `code/Task_04_numerical_errors.py` (original program) and `code/Task_04_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A program compares 0.1 + 0.2 with 0.3 and unexpectedly reports `False`. We also measure absolute and relative error and show a formula that loses accuracy because of round-off.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: the numbers 0.1, 0.2 and 0.3; √2 compared with the approximation 1.414; and x = 10⁻⁴, 10⁻⁸ and 10⁻¹² in the expression (√(1+x) − 1) / x.
- Operations: an exact `==` comparison versus `np.isclose()`; absolute error |true − approximate|; relative error = absolute error / |true|; and two algebraically equal formulas, the direct one and the stable one, 1 / (√(1+x) + 1).

## 3. Original output
```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

![Original output graph](images/task_04_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- 0.1 + 0.2 is stored as 0.30000000000000004, so `==` returns False, while `np.isclose()` returns True. Computers store most decimals as approximate binary fractions.
- Using 1.414 for √2 gives an absolute error of 0.00021356, which is a relative error of about 0.0151 %.
- For x = 10⁻⁴ the direct and stable formulas agree. For x = 10⁻⁸ they already differ in the ninth digit, and for x = 10⁻¹² the direct formula gives 0.500044 while the stable one gives the correct 0.5. The direct formula subtracts two almost equal numbers (√(1+x) and 1), which wipes out most of the correct digits.
- The graph shows the error of the direct formula growing as x gets smaller.

## 5. Changing a parameter (Requirement C)
- What I changed: I used more and more digits of √2 as the approximation: 1.4, 1.41, 1.414, 1.4142, 1.41421 and 1.414213562.
- New output:

```
approx=1.4         : absolute error=1.421e-02, relative error=1.0051%
approx=1.41        : absolute error=4.214e-03, relative error=0.2979%
approx=1.414       : absolute error=2.136e-04, relative error=0.0151%
approx=1.4142      : absolute error=1.356e-05, relative error=0.0010%
approx=1.41421     : absolute error=3.562e-06, relative error=0.0003%
approx=1.414213562 : absolute error=3.731e-10, relative error=0.0000%
```

![Graph after the change](images/task_04_changed.png)

- What changed and why:
  - The relative error fell from 1.0051 % (for 1.4) to about 0.0003 % (for 1.41421), and the absolute error with nine decimals is only 3.7 × 10⁻¹⁰.
  - Each extra digit (up to 1.41421) reduced the error by a factor of roughly 3 to 20. It is not exactly 10 because the size of the error depends on the digits that come next. The last approximation adds four digits at once, so its error is thousands of times smaller.
  - The graph shows the error falling steadily on a log scale.

## 6. Modified real-world case (Requirement E)
- Scenario: A mobile-money system adds a fee of KES 0.10 for every transaction and totals the fees. We compare adding 0.10 repeatedly in floating point with `math.fsum` and with exact integer cents.
- Assumptions:
  - Every transaction carries exactly the same fee of KES 0.10.
  - The exact total is the number of transactions × 10 cents, calculated in integers and divided by 100.
  - Numbers of transactions from 10 up to 1,000,000 are tested.
- New input data: Number of transactions n = 10, 100, 1,000, 10,000, 100,000 and 1,000,000, each with a fee of 0.10.
- New output:

```
n=       10: naive=1.0000000000, fsum=1.0000000000, exact=1.00, naive error=1.110e-16
n=      100: naive=10.0000000000, fsum=10.0000000000, exact=10.00, naive error=1.954e-14
n=    1,000: naive=100.0000000000, fsum=100.0000000000, exact=100.00, naive error=1.407e-12
n=   10,000: naive=1000.0000000002, fsum=1000.0000000000, exact=1000.00, naive error=1.588e-10
n=  100,000: naive=10000.0000000188, fsum=10000.0000000000, exact=10000.00, naive error=1.885e-08
n=1,000,000: naive=100000.0000013329, fsum=100000.0000000000, exact=100000.00, naive error=1.333e-06
```

![Modified case graph](images/task_04_modified.png)

- Interpretation:
  - The naive loop total drifts away from the exact total as n grows. The error is about 10⁻¹⁶ for 10 additions and about 1.3 × 10⁻⁶ for a million additions. Each 10× increase in n made the error roughly 100× larger in these runs.
  - `math.fsum` gives the exact total every time, because it tracks the lost low-order digits.
  - The error in a single run is tiny in money terms, but it can still break exact comparisons (such as total == expected) and reconciliation checks.
  - Limitation: the safest fix for money is to work in integer cents or use Python's `decimal` module, and to compare with a tolerance instead of `==`.

## 7. Conclusion
Floating-point numbers are approximations, so tiny round-off errors appear even in simple sums like 0.1 + 0.2. These errors can accumulate over many operations and can be made much worse by subtracting nearly equal numbers. Comparing with a tolerance, rewriting formulas in a stable form and using exact summation are practical ways to control them.
