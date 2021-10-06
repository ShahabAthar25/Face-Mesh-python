import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

current_time = 0
previous_time = 0

face_mesh_model = mp.solutions.face_mesh
face_mesh = face_mesh_model.FaceMesh()
draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    if results.multi_face_landmarks:
        for face_landmark in results.multi_face_landmarks:
            draw.draw_landmarks(img, face_landmark)

    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time

    cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), )

    cv2.imshow("Face Mesh", img)

    cv2.waitKey(1)