import cv2
img = cv2.imread('./image.jpg', cv2.IMREAD_GRAYSCALE)
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("YUV Image", yuv_img)

# Let's seperate the channels
# cv2.imshow('Y Channel', yuv_img[:, :, 0])
# cv2.imshow('U Channel', yuv_img[:, :, 1])
# cv2.imshow('V Channel', yuv_img[:, :, 2])

# cv2.waitKey()
