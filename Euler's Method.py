from typing import Callable
import numpy as np
from askFunction_tableFunc import ask_function


def euler_method(f: Callable[[float,float], float], x0: float, y0: float, h: float, n_steps: int):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n_steps):
        y = y + h * f(x, y)
        x = x + h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

print("Euler's method for y' = f(x,y)")
f = ask_function(2)
x0 = float(input("x0: "));
y0 = float(input("y0: "))
h = float(input("step h: "));
nsteps = int(input("n steps: "))
xs, ys = euler_method(f, x0, y0, h, nsteps)
for xi, yi in zip(xs, ys): print(f"x={xi:.6g}, y={yi:.12g}")
