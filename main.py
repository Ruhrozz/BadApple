import cv2
import numpy as np
import time
import os


os.system("cls")
print("Available:")

for n, item in enumerate(os.listdir(path='videos')):
    print(f" {n}.", item.split(".")[0])

idx = int(input("Which one? \n"))
name = os.listdir(path='videos')[idx]

chars = list(" .:;)}SM#$%@")
FPS = 30

cap = cv2.VideoCapture(f"videos/{name}")

while True:
    start_frame = time.time()
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    size = gray
    image = cv2.resize(gray, (149, 40), interpolation=cv2.INTER_AREA)
    image = (image // np.ceil(255 / len(chars)).astype(int))
    index_frame = np.take(chars, image)
    char_frame = '\n'.join([''.join(i) for i in index_frame])

    print(char_frame, end='')

    while time.time() - start_frame < 1/FPS:
        pass





