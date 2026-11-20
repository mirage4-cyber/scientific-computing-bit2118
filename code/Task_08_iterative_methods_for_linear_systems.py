import numpy as np
import matplotlib.pyplot as plt

A = np.array([[ 2., -1., 0., 0., 0.],
              [-1., 2., -1., 0., 0.],
              [ 0., -1., 2., -1., 0.],
              [ 0., 0., -1., 2., -1.],
              [ 0., 0., 0., -1., 2.]])
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        new_x = (b - R @ x) / D
        error = np.linalg.norm(new_x - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return new_x, errors
        x = new_x
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x.copy(), errors
    return x, errors

xj, ej = jacobi(A, b)
xgs, egs = gauss_seidel(A, b)
print("Jacobi:", np.round(xj, 6), "iterations:", len(ej))
print("Gauss-Seidel:", np.round(xgs, 6), "iterations:", len(egs))
print("Direct:", np.linalg.solve(A, b))

plt.semilogy(ej, label="Jacobi")
plt.semilogy(egs, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change")
plt.title("Convergence comparison"); plt.grid(True); plt.legend(); plt.show()
