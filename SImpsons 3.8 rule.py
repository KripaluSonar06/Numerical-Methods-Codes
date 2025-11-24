from typing import Callable
from askFunction_tableFunc import ask_function


def simpson_three_eighths(f: Callable[[float], float], a: float, b: float, n: int):
    # n must be multiple of 3
    if n % 3 != 0:
        raise ValueError("n must be divisible by 3 for Simpson's 3/8 rule")
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        coef = 3 if i%3!=0 else 2
        s += coef * f(a + i*h)
    return 3*h*s/8

print("Simpson's 3/8 rule.")
f = ask_function(1)
a = float(input("a: "));
b = float(input("b: "))
n = int(input("n (multiple of 3): "))
val = simpson_three_eighths(f, a, b, n)
print(f"Approx integral = {val}")
