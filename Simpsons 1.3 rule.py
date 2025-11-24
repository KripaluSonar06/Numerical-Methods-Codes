from typing import Callable
from askFunction_tableFunc import ask_function


def simpson_one_third(f: Callable[[float], float], a: float, b: float, n: int):
    # n must be even
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i%2==1 else 2
        s += coef * f(a + i*h)
    return s * h / 3

print("Simpson's 1/3 rule.")
f = ask_function(1)
a = float(input("a: "));
b = float(input("b: "))
n = int(input("n (even): "))
val = simpson_one_third(f, a, b, n)
print(f"Approx integral = {val}")