import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, img = capture.read()
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
        break

capture.release()
cv2.destroyAllWindows()