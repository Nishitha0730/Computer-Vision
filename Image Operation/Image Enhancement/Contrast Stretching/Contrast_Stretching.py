import cv2
import numpy as np


def contrast_stretching(image):
    I_min = np.min(image)
    I_max = np.max(image)

    stretched = ((image - I_min) / (I_max - I_min)) * 255
    stretched = stretched.astype(np.uint8)

    return stretched