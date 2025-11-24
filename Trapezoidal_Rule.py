from typing import Callable
from askFunction_tableFunc import ask_function


def trapezoidal_rule(f: Callable[[float], float], a: float, b: float, n: int):
    if n <= 0: raise ValueError("n must be positive integer")
    h = (b-a)/n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return s*h

print("Trapezoidal rule for integral.")
f = ask_function(1)
a = float(input("a: "));
b = float(input("b: "))
n = int(input("Number of subintervals n (positive): "))
val = trapezoidal_rule(f, a, b, n)
print(f"Approx integral = {val}")
