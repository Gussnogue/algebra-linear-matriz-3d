import numpy as np

def calcular():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    return {
        "a": a,
        "b": b,
        "dot": np.dot(a, b),
        "norma_a": np.linalg.norm(a),
        "norma_b": np.linalg.norm(b),
        "outer": np.outer(a, b)
    }

