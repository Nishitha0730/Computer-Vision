import cv2
import numpy as np
from PIL import Image

def contrast_stretching(image):
    img_array = np.array(image)
    I_min = np.min(img_array)
    I_max = np.max(img_array)

    stretched = ((img_array - I_min) / (I_max - I_min)) * 255
    stretched = stretched.astype(np.uint8)

    return Image.fromarray(stretched)