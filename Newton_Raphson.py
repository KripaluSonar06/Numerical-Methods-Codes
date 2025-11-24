from typing import Callable
from askFunction_tableFunc import ask_function


def newton_raphson(func: Callable[[float], float], dfunc: Callable[[float], float], x0: float, tol=1e-8, maxiter=50):
    x = x0
    for i in range(maxiter):
        fx = func(x)
        dfx = dfunc(x)
        if abs(dfx) < 1e-12:
            raise ZeroDivisionError("Derivative near zero; NR may fail.")
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, maxiter

print("Newton-Raphson root finder. Provide f(x) and f'(x).")
f = ask_function(1)
df = ask_function(1)
x0 = float(input("Initial guess x0: "))
root, iters = newton_raphson(f, df, x0)
print(f"Root ~ {root} after {iters} iterations.")
