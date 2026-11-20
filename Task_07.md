# Task 7: Gaussian Elimination and LU Decomposition

**Program files:** `code/Task_07_gaussian_lu.py` (original program) and `code/Task_07_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A simulation uses the same coefficient matrix A every second but receives a new measurement vector b each time. Instead of repeating full elimination, we factor A once with LU decomposition and reuse the factors.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: A = [[4, −1, 0], [−1, 4, −1], [0, −1, 3]] and three measurement vectors b = [15, 10, 10], [16, 11, 9] and [14, 12, 11].
- Operation: `lu_factor(A)` writes A as PA = LU (with pivoting) once, then `lu_solve()` finds x for each b by cheap forward and backward substitution. The residual b − Ax checks each answer, and `np.linalg.solve()` is used for comparison.

## 3. Original output
```
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

![Original output graph](images/task_07_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The first set gives x = [5, 5, 5]. By hand: 4(5) − 5 = 15, −5 + 4(5) − 5 = 10 and −5 + 3(5) = 10.
- The other two sets give similar values, such as [5.317, 5.268, 4.756], because their b vectors are close to the first.
- The residual norms are about 10⁻¹⁵ or zero, which is just round-off. The direct solution for the first set matches the LU result.
- The bar chart compares the three solutions, which are similar but not identical.

## 5. Changing a parameter (Requirement C)
- What I changed: I changed one coefficient, A[1,1], from 4 to 8, and solved with the first measurement vector b = [15, 10, 10].
- New output:

```
Original solution: [5. 5. 5.]
Changed solution : [4.3258427  2.30337079 4.1011236 ]
Residual norm (changed): 2.5121479338940403e-15
```

![Graph after the change](images/task_07_changed.png)

- What changed and why:
  - The solution changed from [5, 5, 5] to [4.326, 2.303, 4.101].
  - The biggest change is in x2, which dropped from 5 to 2.30. The middle equation now has a larger coefficient on x2, so the same right-hand side (10) needs a smaller x2.
  - x1 and x3 also changed because the three equations are linked.
  - The residual is still about 10⁻¹⁵, so the new answer is just as accurate.

## 6. Modified real-world case (Requirement E)
- Scenario: Heat conduction along a metal rod, solved step by step in time with an implicit method. The matrix is the same at every time step, so LU is ideal.
- Assumptions:
  - One-dimensional rod with 300 interior points and 2,000 time steps.
  - The diffusion number r = α·Δt/Δx² = 0.5 (a fixed value).
  - The left end is held at 100 °C, the right end at 20 °C, and the rod starts at 20 °C.
  - An implicit (backward Euler) scheme is used, so each step solves (I + r·L)·T_new = T_old + boundary terms.
- New input data: A 300 × 300 tridiagonal matrix with 2.0 on the diagonal and −0.5 on the off-diagonals. The right-hand side is the previous temperatures plus the boundary terms.
- New output:

```
Rod nodes: 300, time steps: 2000
LU (factor once) time: 0.048 s
Solve every step time: 1.544 s
Speed-up: 32.0x
Largest difference between the two results: 0.00e+00 C
Temperature at node 10 after 2000 steps: 84.45 C
```

![Modified case graph](images/task_07_modified.png)

- Interpretation:
  - Factoring once and reusing the factors gave exactly the same temperatures as solving from scratch at every step (largest difference 0.00 °C), but it was many times faster. The speed-up line in the output shows tens of times. The exact time depends on the computer.
  - The reason is that factoring costs about n³ operations but each substitution only costs about n², so doing the expensive part once pays off over 2,000 steps.
  - The graph shows heat spreading from the hot end. After 10 steps only the first few points have warmed, and after 2,000 steps the heat has travelled much further and the temperature at point 10 is 84.45 °C.
  - Limitation: if the matrix changed at every step (for example if the material properties changed with temperature), the factors could not be reused.

## 7. Conclusion
LU decomposition splits the expensive part of solving Ax = b from the cheap part, so one factorization can serve many right-hand sides. In the heat-rod example it gave identical answers to repeated direct solving in a fraction of the time. Its main limitation is that it only helps when the coefficient matrix stays the same.
