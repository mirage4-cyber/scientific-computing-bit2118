# Task 10: Root Finding: Bisection and Fixed-Point Methods

**Program files:** `code/Task_10_bisection_fixed_point.py` (original program) and `code/Task_10_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
Determine the temperature at which a nonlinear heat-balance equation becomes zero, meaning that heat gain equals heat loss.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: the function f(T) = T − 25 − 10·e^(−T/20); a bracket [20, 40] where f changes sign (f(20) < 0 and f(40) > 0); and a tolerance of 10⁻¹⁰. For fixed-point iteration, the rewritten equation T = g(T) = 25 + 10·e^(−T/20) with starting guess T = 30.
- Operations: bisection repeatedly halves the bracket and keeps the half where the sign changes. Fixed-point iteration repeats T_new = g(T_old) until two successive values differ by less than 10⁻¹⁰.

## 3. Original output
```
Bisection equilibrium temperature: 27.525211 C
Bisection iterations: 38
Fixed-point equilibrium temperature: 27.525211 C
Fixed-point iterations: 13
```

![Original output graph](images/task_10_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- Both methods give the same equilibrium temperature, 27.525211 °C. At this temperature the heat gained equals the heat lost.
- Bisection needed 38 iterations and fixed-point iteration only 13.
- The graph shows f(T) negative below about 27.5 °C and positive above it. The dashed line marks the point where the curve crosses zero.
- Fixed-point iteration was faster here because the slope of g near the root is small (|g′| ≈ 0.13), so the error shrinks by about that factor every step, while bisection only halves the interval each time.

## 5. Changing a parameter (Requirement C)
- What I changed: Change 1: I changed the bisection tolerance to 10⁻², 10⁻⁶ and 10⁻¹⁰. Change 2: I changed the starting guess of the fixed-point iteration from 30 °C to 100 °C and 0 °C.
- New output:

```
Bisection xtol=1e-02: root=27.52929688 C, iterations=11
Bisection xtol=1e-06: root=27.52521098 C, iterations=25
Bisection xtol=1e-10: root=27.52521082 C, iterations=38
Fixed point from T0= 30.0: root=27.52521082 C, iterations=13
Fixed point from T0=100.0: root=27.52521082 C, iterations=14
Fixed point from T0=  0.0: root=27.52521082 C, iterations=15
```

![Graph after the change](images/task_10_changed.png)

- What changed and why:
  - Bisection needed 11, 25 and 38 iterations for the three tolerances. Each extra 10⁻⁴ of accuracy costs about 14 more iterations, because every iteration halves the interval (the number needed is about log₂(width / tolerance)).
  - Fixed-point iteration reached the same root from every start, in 13 (start 30), 14 (start 100) and 15 (start 0) iterations. The graph shows the distance from the root falling along almost the same line.
  - The start hardly matters here because |g′(T)| = 0.5·e^(−T/20) is below 1 everywhere we start, so the iteration converges from any guess. For other equations this may not be true.

## 6. Modified real-world case (Requirement E)
- Scenario: Break-even point of a boda boda business: the number of rides per week at which revenue equals cost.
- Assumptions:
  - Revenue is KES 250 per ride.
  - Cost = 4,000 fixed + 60 per ride + 0.5 × rides^1.5 (the last term models extra wear and fuel as the bike is used more).
  - The figures are made up for illustration. Rides are treated as a continuous number during the calculation.
  - Bisection is used on the bracket [1, 100]. For fixed-point iteration, the equation is rewritten as rides = cost / 250.
- New input data: Profit(x) = 250x − (4000 + 60x + 0.5x^1.5). Bracket [1, 100]. Fixed-point form x = (4000 + 60x + 0.5x^1.5) / 250 starting at x = 10.
- New output:

```
Bisection break-even: 21.3115 rides per week (34 iterations)
Fixed-point break-even: 21.3115 rides per week (16 iterations)
Profit at the break-even point: 0.000000 KES
Profit at 30 rides: 1617.84 KES
```

![Modified case graph](images/task_10_modified.png)

- Interpretation:
  - Both methods give a break-even of 21.31 rides per week, with the profit at that point equal to 0.000000 KES.
  - Bisection took 34 iterations and fixed-point took 16.
  - Below about 21.3 rides per week the business loses money, and above it makes a profit. At 30 rides the weekly profit is about KES 1,618, as the graph shows where the revenue line rises above the cost curve.
  - Limitation: rides are whole numbers, so the rider really needs at least 22 rides per week to be in profit. The cost figures are assumptions that would have to be measured in practice.

## 7. Conclusion
Bisection always works when the bracket has a sign change but needs many iterations, while fixed-point iteration can be much faster when the slope of g is small. The number of bisection iterations depends mainly on the tolerance, while fixed-point iteration depended very little on the starting guess in this problem. A limitation of fixed-point iteration is that it only converges when |g′| is less than 1.
