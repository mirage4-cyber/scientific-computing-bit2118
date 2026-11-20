# Task 6: Solution of Systems of Linear Equations

**Program files:** `code/Task_06_linear_systems.py` (original program) and `code/Task_06_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
Two server types consume different amounts of CPU and memory. Given the total usage, we find how many servers of each type are active.

## 2. Inputs and mathematical operation (Requirement B)
- Unknowns: x = number of Type A servers and y = number of Type B servers.
- Inputs: Type A uses 4 CPU units and 8 GB, Type B uses 2 CPU units and 12 GB, and the totals are 20 CPU units and 72 GB. This gives A = [[4, 2], [8, 12]] and b = [20, 72].
- Operation: solve Ax = b with `np.linalg.solve()`, then check with `A @ x` and the residual b − Ax.

## 3. Original output
```
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

![Original output graph](images/task_06_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The solution is 3 Type A servers and 4 Type B servers. By hand: 4(3) + 2(4) = 20 and 8(3) + 12(4) = 72, so both totals are matched.
- `A @ solution` gives [20, 72] and the residual is 0, which confirms the solution.
- On the graph each equation is a straight line, and the solution is the single point where the two lines cross, at (3, 4).

## 5. Changing a parameter (Requirement C)
- What I changed: Change 1: I changed the totals from 20 CPU / 72 GB to 22 CPU / 80 GB. Change 2: I made the second row proportional to the first, A = [[4, 2], [8, 4]].
- New output:

```
New totals [22.0, 80.0]: Type A = 3.25, Type B = 4.50
Residual norm: 0.0
Proportional rows [[4, 2], [8, 4]]: LinAlgError -> Singular matrix
Determinant of the proportional matrix: 0.0
```

![Graph after the change](images/task_06_changed.png)

- What changed and why:
  - With totals 22 and 80 the solution is 3.25 Type A and 4.50 Type B servers. The equations are still solved exactly (residual 0), but we cannot have part of a server, so those totals could not come from a whole number of servers. In a real system this would suggest a measurement error.
  - With proportional rows, NumPy raises `LinAlgError: Singular matrix` and the determinant is 0. The two equations carry the same information, so there is no single answer. The lines would be parallel or the same line.
  - A system has exactly one solution only when the determinant is not zero.

## 6. Modified real-world case (Requirement E)
- Scenario: A two-loop DC electrical circuit. Using the mesh-current method we find the current in each loop and in the resistor they share.
- Assumptions:
  - R1 = 10 Ω, R2 = 20 Ω (shared by both loops) and R3 = 30 Ω; batteries V1 = 12 V and V2 = 6 V.
  - Both mesh currents are assumed to flow clockwise. The battery V2 opposes the positive direction of loop 2, so it appears as −V2.
  - The batteries are ideal and the resistors are constant.
- New input data: A = [[30, −20], [−20, 50]] and b = [12, −6], from (R1+R2)·I1 − R2·I2 = V1 and −R2·I1 + (R2+R3)·I2 = −V2.
- New output:

```
Mesh current I1 = 0.4364 A, I2 = 0.0545 A
Current through the shared resistor R2 = 0.3818 A
Check loop 1: R1*I1 + R2*(I1 - I2) = 12.0000 V (supply 12.0 V)
Residual norm: 0.0
```

![Modified case graph](images/task_06_modified.png)

- Interpretation:
  - The mesh currents are I1 = 0.4364 A and I2 = 0.0545 A, and both are positive, so both flow in the assumed directions.
  - The shared resistor R2 carries the difference, I1 − I2 = 0.3818 A.
  - Check: R1·I1 + R2·(I1 − I2) = 12.0000 V, which equals the supply, so Kirchhoff's voltage law holds. The residual is 0.
  - Limitation: a circuit with more loops gives a bigger matrix, and the method assumes linear resistors.

## 7. Conclusion
A set of simultaneous equations can be written as Ax = b and solved directly with `np.linalg.solve()`, and the residual is a quick check of the answer. Changing the data can produce answers that do not make physical sense, such as fractional servers, and a singular matrix means there is no unique solution. The same method works for server counts and electrical circuits alike.
