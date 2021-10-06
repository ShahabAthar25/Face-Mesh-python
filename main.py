import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

current_time = 0
previous_time = 0

while True:
    success, img = cap.read()

    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time

    cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), )

    cv2.imshow("Face Mesh", img)

    cv2.waitKey(1)