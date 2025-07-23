import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("Arthur.jpg")  # Always read images in BGR format


fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax.set_title("Original Image")
plt.show()
