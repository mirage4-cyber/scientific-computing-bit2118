# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Program files:** `code/Task_11_newton_secant.py` (original program) and `code/Task_11_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A financial application must compute the interest rate (the internal rate of return, IRR) that makes the net present value (NPV) of a project equal to zero.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: cash flows [−10000, 3000, 3500, 4000, 2500] (an investment followed by four yearly inflows); Newton-Raphson starting at 0.10 with the derivative of NPV; secant starting at 0.05 and 0.20; tolerance 10⁻¹².
- Operations: NPV(r) = Σ cashflow_t / (1 + r)^t. Newton-Raphson repeats r_new = r − NPV(r)/NPV′(r). The secant method does the same but estimates the slope from the last two points, so no derivative is needed.

## 3. Original output
```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
Newton iterations: 4, Secant iterations: 7
```

![Original output graph](images/task_11_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- Both methods give an IRR of 11.542461 % per year, and the NPV at that rate is 0.000000.
- This means the project earns about 11.5 % a year on the money invested. It is worthwhile if the cost of borrowing is lower than that.
- Newton-Raphson needed 4 iterations and the secant method 7. Newton is faster because it uses the exact slope, while the secant method has to estimate it.
- The graph shows NPV falling as the discount rate rises, crossing zero at the IRR.

## 5. Changing a parameter (Requirement C)
- What I changed: Change 1: I changed the initial investment from 10,000 to 9,000 and 12,000. Change 2: I changed the Newton starting guess from 0.10 to 0.50.
- New output:

```
Investment   9000: IRR = 16.7302% (Newton, 5 iterations)
Investment  10000: IRR = 11.5425% (Newton, 4 iterations)
Investment  12000: IRR = 3.3298% (Newton, 5 iterations)
Newton from x0=0.1: IRR = 11.5425%, iterations = 4
Newton from x0=0.5: IRR = 11.5425%, iterations = 8
```

![Graph after the change](images/task_11_changed.png)

- What changed and why:
  - The IRR changed to 16.73 % for an investment of 9,000, 11.54 % for 10,000 and 3.33 % for 12,000. Paying more for the same inflows (13,000 in total) lowers the return a lot, and the NPV curve on the graph shifts downward.
  - Starting Newton at 0.50 gave the same IRR of 11.5425 %, but took 8 iterations instead of 4.
  - A start further from the root costs more iterations but still reaches the root here because the NPV curve is smooth and falls steadily.

## 6. Modified real-world case (Requirement E)
- Scenario: Finding the true monthly interest rate of a loan, and comparing it with the advertised flat rate.
- Assumptions:
  - The borrower is offered 100,000 but a 2,000 fee is deducted up front, so only 98,000 is received.
  - It is repaid with 12 equal payments of 9,500 at the end of each month (114,000 in total).
  - There are no other charges. The figures are invented for the exercise.
  - The monthly rate is converted to an annual rate with (1 + r)¹² − 1.
- New input data: Cash flows [+98000, then twelve payments of −9500]. Newton starts at 0.01, and the secant method starts at 0.01 and 0.05.
- New output:

```
Monthly rate (Newton-Raphson): 2.4070% (5 iterations)
Monthly rate (Secant): 2.4070% (6 iterations)
Effective annual rate: 33.03%
Quoted flat rate for comparison: 14.00% per year
NPV at the solution: -0.000000
```

![Modified case graph](images/task_11_modified.png)

- Interpretation:
  - The true cost is 2.4070 % per month. Newton-Raphson took 5 iterations and the secant method 6, and they agree.
  - The effective annual rate is 33.03 %. The loan looks like a 14 % flat rate (14,000 extra on 100,000), but the real cost is more than double that.
  - The difference arises because the borrower repays gradually, so on average much less than 100,000 is owed during the year, and because the fee reduces the money actually received.
  - Limitation: it assumes equal payments on fixed dates, and real loans may have other charges that would raise the rate further.

## 7. Conclusion
Newton-Raphson and the secant method find a root much faster than bisection when they are started reasonably well, and Newton needs fewer iterations because it uses the exact derivative. Solving NPV(r) = 0 gives the true rate of return or the true cost of borrowing. A limitation is that a poor starting guess costs more iterations and, for some functions, can fail to converge.
