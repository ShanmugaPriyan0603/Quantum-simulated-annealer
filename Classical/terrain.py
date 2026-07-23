# terrain.py

import numpy as np

from Classical.config import GRID_SIZE

# Search space
X_MIN = -5.12
X_MAX = 5.12


def generate_terrain():
    """
    Generate a sampled Rastrigin function.
    """

    x = np.linspace(X_MIN, X_MAX, GRID_SIZE)
    y = np.linspace(X_MIN, X_MAX, GRID_SIZE)

    X, Y = np.meshgrid(x, y)

    Z = (
        20
        + X**2
        + Y**2
        - 10*np.cos(2*np.pi*X)
        - 10*np.cos(2*np.pi*Y)
    )

    return Z