# BIT 2118 Scientific Computing - Group Work

Individual repository for the BIT 2118 Scientific Computing group work.

**Name:** Annah Waitita BSCCS/2025/67059
**Course:** BIT 2118 Scientific Computing, Mount Kenya University


## Repository structure

```
code/
  Task_NN_<topic>.py        original program from the handout
  Task_NN_modified.py       parameter change + modified real-world case
  _helpers.py               saves each graph into docs/images (and shows it)
docs/
  Task_NN.md                write-up for each task
  images/                   graphs for every task
requirements.txt
```

## Tasks

| Task | Topic | Modified real-world case |
|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | IoT water-tank level sensor |
| 3 | Mathematical Functions and Vectorization | Soil-moisture outlier detection |
| 4 | Floating-Point Arithmetic and Numerical Errors | Accumulating mobile-money fees |
| 5 | Matrix Algebra and Matrix Operations | Two-link robot arm |
| 6 | Solution of Systems of Linear Equations | Two-loop electrical circuit |
| 7 | Gaussian Elimination and LU Decomposition | Heat conduction along a rod |
| 8 | Iterative Methods for Linear Systems | Steady-state temperature of a plate |
| 9 | Eigenvalues and Eigenvectors | PageRank of a small website |
| 10 | Root Finding: Bisection and Fixed-Point | Boda boda break-even point |
| 11 | Root Finding: Newton-Raphson and Secant | True interest rate of a loan |
| 12 | Polynomial and Nonlinear Equation Solving | Ball path against a camera range |
| 13 | Interpolation | Fuel-gauge calibration |
| 14 | Curve Fitting and Approximation | App user growth curve |
| 15 | Numerical Differentiation | Boda boda speed from GPS data |
| 16 | Numerical Integration | Distance from speed readings |
| 17 | ODEs - Euler Method | Cup of tea cooling |
| 18 | Numerical Solution of ODEs Using SciPy | SIR epidemic on a campus |
| 19 | Numerical Optimization | Cheapest fertiliser mix |
| 20 | Random Numbers and Monte Carlo Methods | Matatu trip-time risk |

## Requirements

- Python 3.9 or later
- NumPy, SciPy, Matplotlib

```
pip install -r requirements.txt
```

## How to run

From the project folder, run any program, for example:

```
python code/Task_08_iterative_linear.py
python code/Task_08_modified.py
```

Each program prints its results, saves its graph(s) into `docs/images/` and opens the graph window. Close the window to finish the program. The modified programs print a `PARAMETER CHANGE` section and a `MODIFIED CASE` section.

Note: run times in Tasks 3 and 7 depend on the computer, so your timings will differ from those in the write-ups.
