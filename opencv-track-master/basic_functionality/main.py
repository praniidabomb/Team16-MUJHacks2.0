import cv2
gray_img = cv2.imread('./image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gray Scale', gray_img)
cv2.waitKey()

# Saving this to into a file

cv2.imwrite('./gray_image.jpg', gray_img)
print("Saved Image")

# To see all the available flags
print([x for x in dir(cv2) if x.startswith('COLOR_')])

