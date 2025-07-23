import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def gamma_correction(image, gamma):
    """
    Apply gamma correction to an image.

    Parameters:
    - image: Input image (numpy array).
    - gamma: Gamma value for correction.

    Returns:
    - Corrected image.
    """
    t = np.array([(i / 255.0) ** (gamma) * 255 for i in np.arange(0, 256)]).astype(np.uint8)
    g = cv.LUT(image, t)

    return g