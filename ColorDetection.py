import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # read the video
    ret, frame = cap.read()

# videoga u badal hsv colors.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# lower limit of red color as a hsv
    lower_red = np.array([0,100,100])

# upper limit o the red color as hsv
    upper_red = np.array([10,255,255])

# lower limit of blue color as a hsv
    # lower_orange = np.array([11,100,100])

# upper limit o the blue color as hsv
    # upper_orange = np.array([25,255,255])


# soo muuji kaliya colroska red ah, inta kale black kadhig..
    mask = cv2.inRange(hsv,  lower_red, upper_red)

    result = cv2.bitwise_and(frame, frame, mask = mask)



# soo bandhing, normal image io
    cv2.imshow("Blue Detection", result)
    cv2.imshow("Normal", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

