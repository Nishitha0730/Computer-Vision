import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram_equalization(image):
    """
    Perform histogram equalization on a grayscale image.

    Parameters:
        image (numpy.ndarray): Input grayscale image.

    Returns:
        numpy.ndarray: Histogram equalized image.
    """
    # Calculate histogram
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Calculate cumulative distribution function (CDF)
    cdf = hist.cumsum()
    # cdf_normalized = cdf * hist.max() / cdf.max()
    #
    # # Mask all pixels with zero CDF
    # cdf_m = np.ma.masked_equal(cdf, 0)

    # Normalize the CDF
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    cdf_normalized = cdf_normalized.astype('uint8')

    # Map the original pixel values in the image to the new pixel values
    equalized_image = cdf_normalized[image]

    return equalized_image