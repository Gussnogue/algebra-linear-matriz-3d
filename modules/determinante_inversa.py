import numpy as np

def calcular():
    A = np.array([[3, 1, 0],
                  [2, 4, 1],
                  [1, 0, 2]])
    det = np.linalg.det(A)
    inv = None
    if det != 0:
        inv = np.linalg.inv(A)
    return {
        "A": A,
        "det": det,
        "inv": inv
    }

