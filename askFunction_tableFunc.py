import math
from typing import List
import numpy as np


def ask_function(units: int = 1, vars_name: str = 'x'):
    """
    Ask user for a python expression to build a callable function.
    Example inputs:
      for single-variable: "math.sin(x) + x**2"  -> returns lambda x: ...
      for two-variable: "x+y" -> will return lambda x,y: ...
    """
    if units == 1:
        s = input(f"Enter function of x (use 'math' or 'np' for math functions). Example: math.sin(x)+x**2\nf(x) = ")
        return eval("lambda x: " + s, {"math": math, "np": np})
    elif units == 2:
        s = input(f"Enter function of x and y. Example: x + y**2\nf(x,y) = ")
        return eval("lambda x,y: " + s, {"math": math, "np": np})
    else:
        raise ValueError("Only units 1 or 2 supported in helper.")

def forward_difference_table(y: List[float]) -> np.ndarray:
    """
    Return forward difference table: rows -> order, columns -> starting index
    """
    n = len(y)
    tab = np.zeros((n, n))
    tab[0, :] = y
    for i in range(1, n):
        for j in range(n - i):
            tab[i, j] = tab[i-1, j+1] - tab[i-1, j]
    return tab
