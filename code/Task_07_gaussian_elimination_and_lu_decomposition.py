import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
measurements = [np.array([15., 10., 10.]),
                 np.array([16., 11., 9.]),
                 np.array([14., 12., 11.])]

# Factor the coefficient matrix once, then reuse for each right-hand side
lu, piv = lu_factor(A)
for index, b in enumerate(measurements, start=1):
    x = lu_solve((lu, piv), b)
    print(f"Set {index}: solution={np.round(x, 5)}")
    print("Residual norm:", np.linalg.norm(b - A @ x))

print("Direct comparison:", np.linalg.solve(A, measurements[0]))
