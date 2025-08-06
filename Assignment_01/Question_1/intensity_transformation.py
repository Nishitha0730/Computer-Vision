import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'F:\SEM 5\Computer Vision\Project\Assignment_01\a1images\emma.jpg', cv.IMREAD_GRAYSCALE)
# rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb_img, cmap='gray')
plt.imshow(img,cmap='gray')
plt.show()
