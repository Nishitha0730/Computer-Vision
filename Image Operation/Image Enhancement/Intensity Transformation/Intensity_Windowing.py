# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# img = cv.imread("Arthur.jpg")
#
#
# fig , ax = plt.subplots(figsize=(12, 8))
# ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
# ax.set_title("Original Image")
# plt.show()


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv.imread("Arthur.jpg")   # shape - 675,1200,3

# Define control points (input, output)
c = np.array([(50,10), (200, 220)])

# Create piecewise linear transformation
t1 = np.linspace(0, c[0,1], c[0,0] + 1 - 0).astype('uint8')
t2 = np.linspace(c[0,1] + 1, c[1,1], c[1,0] - c[0,0]).astype('uint8')
t3 = np.linspace(c[1,1] + 1, 255, 255 - c[1,0]).astype('uint8')

transform = np.concatenate((t1, t2, t3)).astype('uint8')

# Apply transformation to each channel (BGR)
b, g, r = cv.split(img)
b_transformed = cv.LUT(b, transform)
g_transformed = cv.LUT(g, transform)
r_transformed = cv.LUT(r, transform)
image_transformed = cv.merge((b_transformed, g_transformed, r_transformed))

# Display results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
ax1.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax1.set_title("Original Image")
ax2.imshow(cv.cvtColor(image_transformed, cv.COLOR_BGR2RGB))
ax2.set_title("Transformed Image")
plt.show()

# Plot the transformation curve
plt.figure(figsize=(8, 6))
plt.plot(transform)
plt.title("Piecewise Linear Transformation Curve")
plt.xlabel("Input Pixel Value")
plt.ylabel("Output Pixel Value")
plt.grid(True)
plt.show()