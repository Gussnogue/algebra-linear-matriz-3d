import numpy as np

def vandermonde():
    x = np.array([1, 2, 3, 5])
    V = np.vander(x, increasing=True)
    return {"x": x, "V": V}

def identidade():
    I = np.eye(4)
    return {"I": I}

def diagonal():
    d = np.diag([2, 4, 6])
    return {"d": d}

