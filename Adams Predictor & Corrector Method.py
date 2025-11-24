from typing import Callable
import numpy as np
from askFunction_tableFunc import ask_function


def adams_bashforth_moulton(f: Callable[[float,float], float], x0: float, y0: float, h: float, n_steps: int):
    """
    Simple PECE predictor-corrector:
    Use RK4 to get first 3 values, then use 3-step Adams-Bashforth predictor and
    3-step Adams-Moulton corrector (order 3/4 style).
    Returns arrays xs, ys
    """
    # helper RK4
    def rk4_step(f, x, y, h):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

    xs = [x0]
    ys = [y0]
    # startup with RK4 until we have 3 previous points
    while len(xs) < 3 and len(xs) < n_steps+1:
        x = xs[-1]
        y = ys[-1]
        ynew = rk4_step(f, x, y, h)
        xs.append(x + h)
        ys.append(ynew)

    # continue with predictor-corrector
    for i in range(len(xs), n_steps+1):
        # indices for last three steps
        x_im2 = xs[-3]
        x_im1 = xs[-2]
        x_i   = xs[-1]
        f_im2 = f(x_im2, ys[-3])
        f_im1 = f(x_im1, ys[-2])
        f_i   = f(x_i, ys[-1])
        # Predictor: 3-step Adams-Bashforth
        y_pred = ys[-1] + h*( (23/12)*f_i - (16/12)*f_im1 + (5/12)*f_im2 )
        x_next = x_i + h
        # Corrector: Adams-Moulton 3-step implicit (we use one-step iteration)
        f_pred = f(x_next, y_pred)
        y_corr = ys[-1] + h*( (5/12)*f_pred + (8/12)*f_i - (1/12)*f_im1 )
        # Optionally iterate correction (single correction step is typical)
        xs.append(x_next)
        ys.append(y_corr)
    return np.array(xs), np.array(ys)

print("Solving y' = f(x,y) with Adams-Bashforth predictor & Adams-Moulton corrector (PECE).")
f = ask_function(2)
x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
h = float(input("Enter step size h: "))
nsteps = int(input("Enter number of steps: "))
xs, ys = adams_bashforth_moulton(f, x0, y0, h, nsteps)
for xi, yi in zip(xs, ys):
    print(f"x={xi:.6g}, y={yi:.12g}")