# Task 8: Iterative Methods for Linear Systems

**Program files:** `code/Task_08_iterative_linear.py` (original program) and `code/Task_08_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
A grid model of temperatures produces many linear equations, most of whose coefficients are zero. We use the Jacobi and Gauss-Seidel iterative methods and track the error at each iteration.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: a 5 × 5 matrix with 2 on the diagonal and −1 beside it, b = [100, 0, 0, 0, 20] (left boundary 100 °C, right boundary 20 °C), starting guess of all zeros, tolerance 10⁻⁸ and at most 500 iterations.
- Operation: Jacobi updates every unknown using only the previous iteration's values. Gauss-Seidel uses the newest values straight away within the same sweep. Both stop when the largest change between iterations is below the tolerance.

## 3. Original output
```
Jacobi temperatures: [86.66666665 73.33333331 59.99999997 46.66666664 33.33333332]
Gauss-Seidel temperatures: [86.66666665 73.3333333  59.99999997 46.66666665 33.33333332]
Direct solution: [86.66666667 73.33333333 60.         46.66666667 33.33333333]
Jacobi iterations: 150
Gauss-Seidel iterations: 75
```

![Original output graph](images/task_08_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- Both methods give temperatures of about [86.67, 73.33, 60.00, 46.67, 33.33] °C, the same as the direct solution to about 7 decimal places.
- The temperatures fall in a straight line from the 100 °C side to the 20 °C side, as expected for steady heat flow.
- Jacobi needed 150 iterations and Gauss-Seidel needed 75, so Gauss-Seidel took half as many because it reuses fresh values immediately.
- On the semi-log graph both curves are straight lines (the error shrinks by a constant factor each iteration), and the Gauss-Seidel line is steeper.

## 5. Changing a parameter (Requirement C)
- What I changed: I changed the stopping tolerance from 10⁻⁸ to 10⁻³, 10⁻⁶ and 10⁻¹⁰.
- New output:

```
tol=1e-03: Jacobi  70 iterations (max error 3.39e-03), Gauss-Seidel  35 iterations (max error 2.87e-03)
tol=1e-06: Jacobi 118 iterations (max error 3.40e-06), Gauss-Seidel  59 iterations (max error 2.88e-06)
tol=1e-10: Jacobi 182 iterations (max error 3.42e-10), Gauss-Seidel  91 iterations (max error 2.90e-10)
```

![Graph after the change](images/task_08_changed.png)

- What changed and why:
  - Jacobi needed 70, 118 and 182 iterations for 10⁻³, 10⁻⁶ and 10⁻¹⁰. Gauss-Seidel needed 35, 59 and 91.
  - Every extra three or four digits of accuracy cost a similar number of extra iterations, because the error falls by a constant factor each time.
  - Gauss-Seidel took about half as many iterations as Jacobi at every tolerance.
  - The actual error was close to the tolerance in each case (for example about 3 × 10⁻⁶ for a tolerance of 10⁻⁶), so the tolerance is a useful guide to accuracy here.

## 6. Modified real-world case (Requirement E)
- Scenario: Steady-state temperature of a square metal plate, using a 10 × 10 grid of interior points. This gives 100 unknowns, with at most 5 non-zero coefficients per equation.
- Assumptions:
  - The temperature no longer changes with time (steady state).
  - The top edge is held at 100 °C and the other three edges at 0 °C.
  - Each interior point equals the average of its four neighbours (the discretised heat equation), so the matrix has 4 on the diagonal and −1 for each neighbour.
  - No heat is lost from the surfaces of the plate.
- New input data: A 100 × 100 matrix built from the 4-neighbour rule, with b = 100 for the points next to the top edge and 0 elsewhere. The tolerance is 10⁻⁶.
- New output:

```
Unknown temperatures: 100
Jacobi iterations: 347, Gauss-Seidel iterations: 181
Largest difference from the direct solution: Jacobi 2.30e-05, Gauss-Seidel 1.10e-05
Temperature at the plate centre (row 5, column 5): 21.25 C
Temperature next to the hot edge (row 0, column 5): 81.52 C
```

![Modified case graph](images/task_08_modified.png)

- Interpretation:
  - Jacobi needed 347 iterations and Gauss-Seidel 181, again about half.
  - Both agree with the direct solution to about 10⁻⁵. The error is larger than the tolerance of 10⁻⁶ because convergence is slow, so a small change between iterations does not guarantee a small error.
  - The heat-map shows the hottest region along the top edge. The temperature at the middle of the top row is 81.52 °C and falls quickly to 21.25 °C at the centre of the plate.
  - The picture is symmetric left to right, as expected.
  - Limitation: a finer grid has many more unknowns and needs many more iterations, so faster methods are used for large problems.

## 7. Conclusion
Jacobi and Gauss-Seidel solve large sparse systems by repeated improvement of a guess, and tracking the error shows how fast they converge. Gauss-Seidel needed about half the iterations of Jacobi in every test. A limitation is that they only converge for suitable matrices (such as diagonally dominant ones) and the convergence slows down as the system gets larger.
