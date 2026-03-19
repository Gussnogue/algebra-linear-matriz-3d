import numpy as np

def decompor_qr():
    A = np.array([[2, 1, 3],
                  [0, 5, 1],
                  [1, 2, 4]])
    Q, R = np.linalg.qr(A)
    return {
        "A": A,
        "Q": Q,
        "R": R
    }

def decompor_svd():
    A = np.array([[2, 1, 3],
                  [0, 5, 1],
                  [1, 2, 4]])
    U, S, Vt = np.linalg.svd(A)
    return {
        "A": A,
        "U": U,
        "S": S,
        "Vt": Vt
    }

