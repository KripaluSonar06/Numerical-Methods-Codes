import numpy as np

def legendre_recurrence(n: int):
    """
    Compute P_0 ... P_n using recurrence:
      (n+1)P_{n+1}(x) = (2n+1) x P_n(x) - n P_{n-1}(x)
    Return numpy.poly1d for P_n.
    """
    P0 = np.poly1d([1.0])
    if n == 0:
        return P0
    P1 = np.poly1d([1.0, 0.0])  # x
    if n == 1:
        return P1
    Pm1 = P0
    Pn = P1
    for k in range(1, n):
        Pnext = ((2*k+1) * np.poly1d([1.0, 0.0]) * Pn - k * Pm1) / (k+1)
        Pm1, Pn = Pn, Pnext
    return Pn


n = int(input("Enter degree n (>=0): "))
Pn = legendre_recurrence(n)
print(f"P_{n}(x) =")
print(Pn)