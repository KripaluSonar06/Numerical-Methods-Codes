from typing import Callable
import numpy as np
from askFunction_tableFunc import ask_function

def rk4_solve(f: Callable[[float,float], float], x0: float, y0: float, h: float, n_steps: int):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n_steps):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        y = y + h*(k1 + 2*k2 + 2*k3 + k4)/6
        x = x + h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

print("RK4 solver for y' = f(x,y)")
f = ask_function(2)
x0 = float(input("x0: ")); y0 = float(input("y0: "))
h = float(input("step h: ")); nsteps = int(input("n steps: "))
xs, ys = rk4_solve(f, x0, y0, h, nsteps)
for xi, yi in zip(xs, ys): print(f"x={xi:.6g}, y={yi:.12g}")
