import cv2
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
    # Normalize the image to [0, 1]
    normalized_image = image / 255.0

    # Apply gamma correction
    corrected_image = np.power(normalized_image, gamma)

    # Scale back to [0, 255]
    corrected_image = np.uint8(corrected_image * 255)

    return corrected_image