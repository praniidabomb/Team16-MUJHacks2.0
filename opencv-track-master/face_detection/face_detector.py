import cv2

face_cascade = cv2.CascadeClassifier("haar_cascade_frontal_face.xml")

img = cv2.imread("face.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(
#     gray_img, scaleFactor=1.05, minNeighbors=5)

# for x, y, w, h in faces:
#     img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

# resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

# """ cv2.imshow("With Face Rectangle", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() """

# print(type(faces))
# print(faces)

# cv2.imshow("Gray", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
