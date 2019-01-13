import cv2
import numpy as np
import math

img = cv2.imread("../image2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

print(rows, " ", cols)

# Vertical Wave
def vertical_wave(img):
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
            offset_y = 0

            if j + offset_x < rows:
                img_output[i, j] = img[i, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0
    cv2.imshow("Input", img)
    cv2.imshow("Vertical Wave", img_output)
    cv2.waitKey()


def horizontal_wave(img):
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = 0
            offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
            if i + offset_y < rows:
                img_output[i, j] = img[(i + offset_y) % rows, j]
            else:
                img_output[i, j] = 0
    cv2.imshow("Input", img)
    cv2.imshow("Horizontal Wave", img_output)
    cv2.waitKey()


def both_verti_hori(img):
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.sin(2 * 3.14 * j / 150))
            if i + offset_y < rows and j + offset_x < cols:
                img_output[i, j] = img[(i + offset_y) % rows, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0
    cv2.imshow("Input", img)
    cv2.imshow("Multidirectional Wave", img_output)
    cv2.waitKey()


def concave_effect(img):
    img_output = np.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(128.0 * math.sin(2 * 3.14 * i / (2 * cols)))
            offset_y = 0
            if j + offset_x < cols:
                img_output[i, j] = img[i, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0
    cv2.imshow("Input", img)
    cv2.imshow("Concave Effect", img_output)
    cv2.waitKey()


concave_effect(img)
