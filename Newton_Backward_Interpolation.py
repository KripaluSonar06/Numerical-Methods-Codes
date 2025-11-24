from typing import List
from askFunction_tableFunc import forward_difference_table

def newton_backward(x_vals: List[float], y_vals: List[float], x: float):
    #Newton backward interpolation (for values near the end).

    n = len(x_vals)
    h = x_vals[1] - x_vals[0]
    t = (x - x_vals[-1]) / h
    tab = forward_difference_table(y_vals)
    result = tab[0, n-1]
    t_term = 1.0
    for i in range(1, n):
        # backward differences are tab[i, n-i-1]
        t_term *= (t + (i - 1)) / i
        result += t_term * tab[i, n-i-1]
    return result

print("Newton backward interpolation (equally spaced x).")
n = int(input("Number data points: "))
xs = [float(input(f"x[{i}]: ")) for i in range(n)]
ys = [float(input(f"y[{i}]: ")) for i in range(n)]
xq = float(input("Query x: "))
val = newton_backward(xs, ys, xq)
print(f"Interpolated value ~ {val}")
