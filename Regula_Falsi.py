from typing import Callable
from askFunction_tableFunc import ask_function


def regula_falsi(f: Callable[[float], float], a: float, b: float, tol=1e-8, maxiter=100):
    fa = f(a); fb = f(b)
    if fa*fb > 0:
        raise ValueError("Function has same sign at a and b.")
    x = a
    for i in range(maxiter):
        x = (a*fb - b*fa) / (fb - fa)
        fx = f(x)
        if abs(fx) < tol:
            return x, i+1
        if fa * fx < 0:
            b = x; fb = fx
        else:
            a = x; fa = fx
    return x, maxiter

print("Regula Falsi (false position). Provide f(x) and endpoints a,b with opposite signs.")
f = ask_function(1)
a = float(input("a: "));
b = float(input("b: "))
root, its = regula_falsi(f, a, b)
print(f"Root ~ {root} after {its} iterations.")
