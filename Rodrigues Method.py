import math
import numpy as np

def legendre_rodrigues(n: int):
    """
    Return coefficients of Legendre polynomial P_n(x) using Rodrigues:
      P_n(x) = (1/(2^n n!)) d^n/dx^n [(x^2 - 1)^n]
    Coefficients returned as numpy.poly1d
    """
    # Build polynomial (x^2 - 1)^n
    base = np.poly1d([1, 0, -1])  # x^2 - 1
    poly = base ** n
    # differentiate n times
    for _ in range(n):
        poly = np.polyder(poly)
    poly = poly * (1.0 / (2 ** n * math.factorial(n)))
    return np.poly1d(poly)


n = int(input("Enter degree n (>=0): "))
Pn = legendre_rodrigues(n)
print(f"P_{n}(x) =")
print(Pn)