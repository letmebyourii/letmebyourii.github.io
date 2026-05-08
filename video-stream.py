# Code taken from the OpenCV tutorial
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

import math
import numpy as np
import cv2 as cv
from ultralytics import YOLO
 
#replace here for model
model = YOLO("yolov8n-oiv7.pt")

find_object = 'Woman'  #placeholder


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


    width, height, _ = frame.shape
    detections = model.predict(source='0', show=True, conf=0.05, stream=True, verbose=False)

    for i in detections:
        all_detections = [i.names[int(j.cls)] for j in i.boxes]
        if find_object not in all_detections:
            print("Object not found.")
        for j in i.boxes: #xyxy = (x1, y1) top left corner, (x2,  y2) bottom right corner
            x1 = j.xyxy.flatten()[0].item()
            y1 = j.xyxy.flatten()[1].item()
            x2 = j.xyxy.flatten()[2].item()
            y2 = j.xyxy.flatten()[3].item()

            dist_topleft = math.dist((x1,y1),(0,0))
            dist_bottomright = math.dist((x2,y2),(width, height))

            mindist = width*height*0.15
            # print(mindist, flush=True)
            # print(dist_topleft*dist_bottomright, flush=True)
            if find_object==i.names[int(j.cls)] and dist_topleft*dist_bottomright < mindist:
                print('Object found.', flush=True)
                





 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()