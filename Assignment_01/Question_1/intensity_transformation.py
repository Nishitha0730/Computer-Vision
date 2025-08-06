import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'F:\SEM 5\Computer Vision\Project\Assignment_01\a1images\emma.jpg', cv.IMREAD_GRAYSCALE)
# rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb_img, cmap='gray')
# plt.imshow(img,cmap='gray')
# plt.show()


# Define control points
c = np.array([(50,75),(150,200),(255,255)])

# Create Transformation curve
t1 = np.linspace(0, c[0,1], c[0,0]+1-0)    #start, stop, num_of_points  <-- output
t2 = np.linspace(c[0,1]+1, c[1,1], c[1,0]-c[0,0])
t3 = np.linspace(c[1,1]+1, c[2,1], c[2,0]-c[1,0])


# Combine Segments
t = np.concatenate((t1,t2,t3), axis=0).astype('uint8')

# Plot the transformation curve
plt.figure(figsize=(8, 5))
plt.plot(t, 'b-', linewidth=2, label='Transformation Curve')
plt.scatter(c[:,0], c[:,1], color='red', s=50, label='Control Points')  # Mark control points
plt.xlabel('Input Pixel Intensity')
plt.ylabel('Output Pixel Intensity')
plt.title('Intensity Transformation Curve')
plt.grid(True)
plt.legend()
plt.show()


# Apply Transformation
img_transformed = cv.LUT(img, t)

plt.imshow(img_transformed,cmap='gray')
plt.show()