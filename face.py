# face.py
import cv2
import time

class FD:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def detect_for_1_second(self):
        cap = cv2.VideoCapture(0)
        start_time = time.time()
        face_found = False

        while time.time() - start_time < 1:
            ret, frame = cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            if len(faces) > 0:
                face_found = True
                break  # No need to check more frames

        cap.release()
        return face_found
