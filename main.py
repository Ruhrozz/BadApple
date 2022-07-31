import cv2
import numpy as np
import time

chars = list(" .:;)}SM#$%@")

FPS = 30
cap = cv2.VideoCapture("badapple.mp4")
# cap = cv2.VideoCapture("shrek.mp4")

while True:
    start_frame = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(gray, (174, 52), interpolation=cv2.INTER_AREA)
    image = (image // np.ceil(255 / len(chars)).astype(int))
    index_frame = np.take(chars, image)
    char_frame = '\n'.join([''.join(i) for i in index_frame])

    # os.system("cls")
    print(char_frame)

    while time.time() - start_frame < 1/FPS:
        pass





