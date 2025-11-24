from typing import List
from askFunction_tableFunc import forward_difference_table

def newton_forward(x_vals: List[float], y_vals: List[float], x: float):
    """
    Newton forward interpolation for equally spaced x.
    Assumes x_vals equally spaced.
    """
    n = len(x_vals)
    h = x_vals[1] - x_vals[0]
    t = (x - x_vals[0]) / h
    tab = forward_difference_table(y_vals)
    result = tab[0,0]
    t_term = 1.0
    for i in range(1, n):
        t_term *= (t - (i - 1)) / i
        result += t_term * tab[i, 0]
    return result

print("Newton forward interpolation (equally spaced x).")
n = int(input("Number data points: "))
xs = [float(input(f"x[{i}]: ")) for i in range(n)]
ys = [float(input(f"y[{i}]: ")) for i in range(n)]
xq = float(input("Query x: "))
val = newton_forward(xs, ys, xq)
print(f"Interpolated value ~ {val}")