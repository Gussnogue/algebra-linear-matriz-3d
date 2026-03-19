import numpy as np

def calcular():
    A = np.array([[3, 1, 0],
                  [2, 4, 1],
                  [1, 0, 2]])
    rank = np.linalg.matrix_rank(A)
    return {"A": A, "rank": rank}

