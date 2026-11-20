import numpy as np
from scipy.optimize import root

# Circle x^2+y^2=4 and parabola y=x^2-1
def equations(z):
    x, y = z
    return [x**2 + y**2 - 4, y - (x**2 - 1)]

for guess in ([1., 1.], [-1., 1.], [0., -1.]):
    result = root(equations, guess)
    print("Initial guess:", guess)
    print("Solution:", np.round(result.x, 6))
    print("Residuals:", np.round(equations(result.x), 10))
    print("Converged:", result.success, result.message)
