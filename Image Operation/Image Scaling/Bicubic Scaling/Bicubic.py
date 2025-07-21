import numpy as np
from PIL import Image

def cubic_kernel(t):
    """Catmull-Rom cubic kernel"""
    a = -0.5
    abs_t = np.abs(t)
    abs_t2 = abs_t**2
    abs_t3 = abs_t**3

    if abs_t <= 1:
        return (a + 2) * abs_t3 - (a + 3) * abs_t2 + 1
    elif 1 < abs_t < 2:
        return a * abs_t3 - 5 * a * abs_t2 + 8 * a * abs_t - 4 * a
    else:
        return 0
