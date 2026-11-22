import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    def stats(func):
        # [axis=0 (colunas), axis=1 (linhas), matriz achatada]
        return [
            func(matrix, axis=0).tolist(),
            func(matrix, axis=1).tolist(),
            func(matrix).tolist(),
        ]

    calculations = {
        'mean': stats(np.mean),
        'variance': stats(np.var),
        'standard deviation': stats(np.std),
        'max': stats(np.max),
        'min': stats(np.min),
        'sum': stats(np.sum),
    }

    return calculations
