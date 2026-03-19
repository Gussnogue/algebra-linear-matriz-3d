import numpy as np

def calcular_autovalores():
    A = np.array([[4, -2, 1],
                  [-2, 3, 0],
                  [1, 0, 2]])
    autovalores, autovetores = np.linalg.eig(A)
    return {
        "A": A,
        "autovalores": autovalores,
        "autovetores": autovetores
    }

