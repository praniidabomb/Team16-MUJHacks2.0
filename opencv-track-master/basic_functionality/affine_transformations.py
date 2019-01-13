import cv2
import numpy as np

img = cv2.imread('../image.jpg')
rows, cols = img.shape[:2]

"""
We are defining control points.
We just need three points to get the affine transformation matrix
We want the three points in src_points to be mapped to the corresponding points
in dst_points. 
"""

src_points = np.float32([[0, 0], [cols-1, 0], [0, rows-1]])
dst_points = np.float32(
    [[0, 0], [int(0.6*(cols-1)), 0], [int(0.4*(cols-1)), rows-1]])

affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))

cv2.imshow('Input', img)
cv2.imshow('Output', img_output)
cv2.waitKey()
