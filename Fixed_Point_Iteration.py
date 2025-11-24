from typing import Callable
from askFunction_tableFunc import ask_function


def fixed_point(g: Callable[[float], float], x0: float, tol=1e-8, maxiter=100):
    x = x0
    for i in range(maxiter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, maxiter

print("Fixed point iteration solves x = g(x). Provide g(x).")
g = ask_function(1)
x0 = float(input("Initial guess x0: "))
root, iters = fixed_point(g, x0)
print(f"Fixed point ~ {root} after {iters} iterations.")
