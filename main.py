import os
import time

import cv2
import numpy as np


def main():
    print("Available:")
    for n, item in enumerate(os.listdir(path="videos")):
        print(f" {n}.", item.split(".")[0])
    idx = int(input("Which one? \n"))

    name = os.listdir(path="videos")[idx]

    CHARS = list(" .:;)}SM#$%@")
    FPS = 30

    cap = cv2.VideoCapture(f"videos/{name}")

    while True:
        cmd_shape = list(os.get_terminal_size())
        cmd_shape[0] -= 1  # adding "\n"

        start_frame = time.time()
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        image = cv2.resize(gray, cmd_shape, interpolation=cv2.INTER_AREA)
        image = image // np.ceil(255 / len(CHARS)).astype(int)

        index_frame = np.take(CHARS, image)
        char_frame = "\n".join(["".join(i) for i in index_frame])

        print(char_frame, end="")

        while time.time() - start_frame < 1 / FPS:
            pass


if __name__ == "__main__":
    main()
