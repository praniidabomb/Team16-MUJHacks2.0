import cv2
import time

video = cv2.VideoCapture(0)
# the argument 0,1,2 represents number of camera's
while True:
    check, frame = video.read()

    print(check)
    print(frame)

    # if You want in gray
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)  # Frame Rate Actually

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
