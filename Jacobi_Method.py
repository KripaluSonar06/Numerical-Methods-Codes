import numpy as np

def jacobi(A: np.ndarray, b: np.ndarray, x0: np.ndarray = None, tol=1e-8, maxiter=100): #Ax=b
    n = A.shape[0]
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()
    D = np.diag(A)
    R = A - np.diagflat(D)
    for k in range(maxiter):
        x_new = (b - R.dot(x)) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k+1
        x = x_new
    return x, maxiter

print("Jacobi iterative method for Ax = b")
n = int(input("Dimension n: "))
print("Enter matrix A row by row (space-separated):")
A = np.zeros((n, n))
for i in range(n):
    row = list(map(float, input(f"Row {i}: ").split()))
    if len(row) != n: raise ValueError("Row length mismatch")
    A[i, :] = row
b = np.array(list(map(float, input("Enter b vector (space-separated): ").split())))
x0_input = input("Initial guess x0? (leave blank for zeros) ")
x0 = None
if x0_input.strip():
    x0 = np.array(list(map(float, x0_input.split())))
    sol, iters = jacobi(A, b, x0)
    print(f"Solution approx after {iters} iterations:\n{sol}")
else:
    print("Invalid choice.")