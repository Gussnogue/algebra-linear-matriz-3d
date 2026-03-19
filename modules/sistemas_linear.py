import numpy as np

def resolver_sistema_2x2():
    A = np.array([[2, 1], [1, -1]])
    b = np.array([5, 1])
    x = np.linalg.solve(A, b)
    return {
        "A": A,
        "b": b,
        "solucao": x,
        "descricao": "2x + y = 5\n x - y = 1"
    }

def resolver_sistema_3x3():
    A = np.array([[1, 1, 1],
                  [2, -1, 1],
                  [1, 2, -1]])
    b = np.array([6, 3, 2])
    x = np.linalg.solve(A, b)
    return {
        "A": A,
        "b": b,
        "solucao": x,
        "descricao": "x + y + z = 6\n2x - y + z = 3\nx + 2y - z = 2"
    }

