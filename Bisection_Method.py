from typing import Callable
from askFunction_tableFunc import ask_function


def bisection(f: Callable[[float], float], a: float, b: float, tol=1e-8, maxiter=100):
    fa = f(a); fb = f(b)
    if fa*fb > 0:
        raise ValueError("Function has same sign at a and b.")
    for i in range(maxiter):
        m = 0.5*(a+b)
        fm = f(m)
        if abs(fm) < tol or (b-a)/2 < tol:
            return m, i+1
        if fa*fm < 0:
            b = m; fb = fm
        else:
            a = m; fa = fm
    return 0.5*(a+b), maxiter

print("Bisection method. Provide f(x) and brackets a,b with opposite signs.")
f = ask_function(1)
a = float(input("a: "));
b = float(input("b: "))
root, its = bisection(f, a, b)
print(f"Root ~ {root} after {its} iterations.")
