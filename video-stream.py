# Code taken from the OpenCV tutorial
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 as cv
from ultralytics import YOLO
 
#replace here for model
model = YOLO("yolov8n-oiv7.pt")


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    color = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)
    # Display the resulting frame
    cv.imshow('frame', color)
    if cv.waitKey(1) == ord('q'):
        break

    #model runs here 
    detection = model.predict(source='0', show=True, conf=0.05)












 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()