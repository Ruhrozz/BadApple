import subprocess
import cv2
import os

# proc = subprocess.Popen(['start', 'cmd', '&&', 'python', 'main.py'], shell=True)
# proc.wait()

cap = cv2.VideoCapture("badapple.mp4")
ret, frame = cap.read()

os.system("start /wait cmd /c python main.py")
