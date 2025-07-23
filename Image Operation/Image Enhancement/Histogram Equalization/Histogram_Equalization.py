import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np



def histogram_equalization(image):
    # Convert PIL Image to NumPy array
    img_array = np.array(image)

    # Compute histogram
    hist, bins = np.histogram(img_array.flatten(), 256, [0, 256])

    # Rest of your equalization code...
    cdf = hist.cumsum()
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    cdf_normalized = cdf_normalized.astype('uint8')
    equalized_image = cdf_normalized[img_array]

    # Convert back to PIL Image if needed
    return Image.fromarray(equalized_image)