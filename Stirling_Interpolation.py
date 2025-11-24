from typing import List
from askFunction_tableFunc import forward_difference_table


def stirling_interpolation(x_vals: List[float], y_vals: List[float], x: float):
    """
    Simplified Stirling interpolation for equally spaced data and x near centre.
    We build central difference table and use Stirling formula (approx).
    This is a pedagogical, not fully optimized implementation.
    """
    n = len(x_vals)
    if n % 2 == 0:
        raise ValueError("Stirling best with odd number of points (central point).")
    h = x_vals[1] - x_vals[0]
    mid = n//2
    # forward diff
    tab = forward_difference_table(y_vals)
    # compute t
    t = (x - x_vals[mid]) / h
    # Stirling mixes central differences: use simple series
    # y0 + t*Δy0 + t^2/2! * Δ^2 y0 + ...
    # We'll construct alternating central differences roughly
    result = y_vals[mid]
    # Build central difference sequence (approx)
    # Δy at center ~ (tab[1,mid] + tab[1,mid-1]) / 2
    # For simplicity, use central symmetric approach
    factorial = 1.0
    t_power = 1.0
    # We'll use up to available order
    for k in range(1, n):
        factorial *= k
        t_power *= t if k == 1 else (t - (k-1)) if (k%2==1) else (t + (k-1))
        # pick a central difference approx index
        idx = mid - (k//2)
        if idx < 0 or idx >= n:
            break
        central_diff = tab[k, idx] if (k < n and idx + k < n) else 0.0
        result += (t_power / factorial) * central_diff
    return result

print("Stirling interpolation (requires odd number of equally spaced points).")
n = int(input("Number of data points (odd): "))
xs = [float(input(f"x[{i}]: ")) for i in range(n)]
ys = [float(input(f"y[{i}]: ")) for i in range(n)]
xq = float(input("Query x: "))
val = stirling_interpolation(xs, ys, xq)
print(f"Interpolated value ~ {val}")