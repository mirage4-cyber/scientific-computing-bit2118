# Task 12: Polynomial and Nonlinear Equation Solving

**Program files:** `code/Task_12_nonlinear_equations.py` (original program) and `code/Task_12_modified.py` (parameter change and new real-world case). Graphs are saved in `docs/images/`.

## 1. Problem
Find the intersection points between a circle and a parabola, which gives two nonlinear equations in x and y.

## 2. Inputs and mathematical operation (Requirement B)
- Inputs: the circle x² + y² = 4 and the parabola y = x² − 1, written as two residual equations that must both equal zero; starting guesses (1, 1) and (−1, 1).
- Operation: `scipy.optimize.root` improves a guess step by step until both residuals are close to zero. The residuals are printed as a check.

## 3. Original output
```
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [-2.47801779e-13 -2.41584530e-13]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [-2.47801779e-13 -2.41584530e-13]
Converged: True
```

![Original output graph](images/task_12_original.png)

## 4. Interpretation of the output and graph (Requirement D)
- The two intersections found are (1.5175, 1.3028) and (−1.5175, 1.3028), and the residuals are about 10⁻¹³, so both equations are satisfied.
- By hand: substituting x² = y + 1 into the circle gives y² + y − 3 = 0, so y = (−1 + √13)/2 = 1.3028 and x = ±√2.3028 = ±1.5175, which matches.
- The other root of the quadratic, y ≈ −2.30, would need x² to be negative, so it gives no real intersection.
- The graph shows the circle and the parabola crossing at those two points. Each starting guess led to the intersection nearest to it.

## 5. Changing a parameter (Requirement C)
- What I changed: I changed the circle radius from 2 to 1 (x² + y² = 1) and used four starting guesses.
- New output:

```
Guess [1.0, 0.5]: result = [1. 0.], residual norm = 1.1e-14, solver reports converged = True
Guess [-1.0, 0.5]: result = [-1.  0.], residual norm = 1.1e-14, solver reports converged = True
Guess [0.3, -0.8]: result = [ 0. -1.], residual norm = 1.1e-15, solver reports converged = False
Guess [0.0, -0.5]: result = [ 0.  -0.5], residual norm = 9.0e-01, solver reports converged = False
```

![Graph after the change](images/task_12_changed.png)

- What changed and why:
  - With radius 1 the curves meet at (1, 0), (−1, 0) and (0, −1). The first two are crossings, but at (0, −1) the circle only touches the parabola at its lowest point.
  - Guesses (1, 0.5) and (−1, 0.5) found (1, 0) and (−1, 0) normally.
  - Guess (0.3, −0.8) found (0, −1) with a residual of about 10⁻¹⁵, but the solver reported `converged = False`. At a touching point the two curves have the same slope, so the Jacobian is singular and the solver struggles even though the answer is correct. This shows why the residuals should always be checked as well as the success flag.
  - Guess (0, −0.5) failed outright (residual about 0.9), because at x = 0 the Jacobian is already singular. Choosing a better starting point fixes this.

## 6. Modified real-world case (Requirement E)
- Scenario: A ball is kicked at 45° and follows the parabola y = x − 0.01x² (in metres). A camera at the launch point has a circular range of 60 m. Where does the ball path cross the edge of the camera range?
- Assumptions:
  - No air resistance, so the path is an exact parabola, and everything is in a flat 2-D plane.
  - The camera is at the origin (the launch point) and sees everything within exactly 60 m.
  - The path coefficient 0.01 is chosen for illustration. The ball lands at x = 100 m.
  - Only the part of the path with x > 0 is physically meaningful.
- New input data: Equations x² + y² − 3600 = 0 and y − (x − 0.01x²) = 0, with starting guesses (55, 20) and (−35, −45).
- New output:

```
Ball leaves camera range: x = 54.642 m, y = 24.785 m, distance = 60.000 m, converged = True
Other crossing (backwards along the parabola): x = -35.610 m, y = -48.290 m, distance = 60.000 m, converged = True
The ball lands at x = 100 m (y = 0), so the exit point is before landing: True
```

![Modified case graph](images/task_12_modified.png)

- Interpretation:
  - The ball leaves the camera range at (54.64 m, 24.79 m), where its distance from the camera is exactly 60.000 m. This is before it lands at x = 100 m.
  - The ball is therefore visible from launch until about 55 m along the ground, at a height of about 25 m, and it lands out of view.
  - The solver also finds a second crossing at (−35.61, −48.29), which is a valid mathematical solution but physically meaningless because the ball never goes to negative x.
  - Limitation: the model ignores air resistance, so a real ball would not follow an exact parabola. Solutions should always be checked against the physical situation.

## 7. Conclusion
Nonlinear systems can be solved numerically by writing each equation as a residual and letting a solver search from a starting guess, and different guesses can find different solutions. The residual check is important because the solver's success flag was wrong at a touching point and the solver failed from a bad start. Solutions must also be checked against the real situation, since some roots of the equations have no physical meaning.
