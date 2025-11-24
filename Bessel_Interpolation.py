from typing import List
from Newton_Backward_Interpolation import newton_backward
from Newton_Forward_Interpolation import newton_forward
from askFunction_tableFunc import forward_difference_table


def bessel_interpolation(x_vals: List[float], y_vals: List[float], x: float):
    """
    Simplified Bessel interpolation: averages two series; best for mid-interval.
    Pedagogical/simple version using central differences.
    """
    n = len(x_vals)
    if n < 2:
        raise ValueError("Need at least 2 points")
    h = x_vals[1] - x_vals[0]
    tab = forward_difference_table(y_vals)
    mid = (n-1)//2
    t = (x - (x_vals[mid] + x_vals[mid+1])/2) / h  # t from mid-pair
    # For simplicity use interpolation average of forward and backward approximations
    y1 = newton_forward(x_vals[:mid+2], y_vals[:mid+2], x)
    y2 = newton_backward(x_vals[mid:], y_vals[mid:], x)
    return 0.5*(y1 + y2)

print("Bessel interpolation (simplified).")
n = int(input("Number of data points (>=2): "))
xs = [float(input(f"x[{i}]: ")) for i in range(n)]
ys = [float(input(f"y[{i}]: ")) for i in range(n)]
xq = float(input("Query x: "))
val = bessel_interpolation(xs, ys, xq)
print(f"Interpolated value ~ {val}")
