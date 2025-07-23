import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("Arthur.jpg")  # Always read images in BGR format

print(img.shape)

t = np.arange(255,-1,-1, dtype=np.uint8)
new_img = t[img]

fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(cv.cvtColor(new_img, cv.COLOR_BGR2RGB))
ax.set_title("Negative Transformed Image")
plt.show()
