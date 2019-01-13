"""
Blurring
It refers to avereging the pixel values within a neighborhood.
This is also called a low pass filter.
Low Pass Filter : Filter that allows low frequencies and blocks higher frequencies

Frequency : Rate of change of pixel values
so sharp edges would be of high frequency, because the pixel values change
rapidly in that region.


"""

import cv2
import numpy as np

img = cv2.imread('./image.jpg')
rows, cols = img.shape[:2]

kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3x3 = np.ones((3, 3)) / 9
kernel_5x5 = np.ones((5, 5)) / 25.0

cv2.imshow('Original', img)

output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)

output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('3x3 filter', output)

output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('5x5 filter', output)

# Shortcut to apply blurs
output = cv2.blur(img, (3, 3))
cv2.imshow('Automatic Filter', output)
cv2.waitKey(0)

"""
Edge detection
Sobel Filter Sx for horizontal edges, Sy for vertical edges
"""

img = cv2.imread('./image2.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('Original', img)
cv2.imshow('Sobel Horizontal', sobel_horizontal)
cv2.imshow('Sobel Vertical', sobel_vertical)


cv2.waitKey(0)


# Laplacian Filter -  Good but leads to a lot of noise
# it uses double derivative in both directions

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)

# Canny Kernels
canny = cv2.Canny(img, 50, 240)

# Motion Blur
img = cv2.imread('./tree.jpg')

size = 15

# generating kernel
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the input image
output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow('Motion Blur', output)
cv2.waitKey(0)

# Vigentte filter
img = cv2.imread('./image2.png')
rows, cols = img.shape[:2]

# generating vigentter mask using Gaussian Kernels
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)

kernel = kernel_x * kernel_y.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

# Applying the mask to each channel in the input image
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Original', img)
cv2.imshow('Vignette', output)
cv2.waitKey()

# Increasing the contrast of an image
img = cv2.imread('./image2.png', 0)
histeq = cv2.equalizeHist(img)

cv2.imshow('Input', img)
cv2.imshow('Histogram equalized', histeq)
cv2.waitKey()

# Histogram Equivalency for color images
import cv2
import numpy as np

img = cv2.imread('./image2.png')

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
cv2.imshow('Histogram Equlaized', img_output)
cv2.waitKey(0)




