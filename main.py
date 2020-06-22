import cv2
import os
import sys
from flask import Flask

filepath = sys.argv[1]


video1 = cv2.VideoCapture(filepath)

#frame_height = video1.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
#frame_width  = video1.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)

frame_width  = int(video1.get(3)) # float
frame_height = int(video1.get(4)) # float

s = (frame_width, frame_height)

out1 = cv2.VideoWriter('facial_exp_output1.mkv',
                      cv2.VideoWriter_fourcc('M','J','P','G'), 
                      10, 
                      (frame_width, frame_height))

while(True):
  ret, frame = video1.read()

  if ret == True: 
    
    # Write the frame into the file 'output.avi'
    out1.write(frame)

    # Display the resulting frame    
    cv2.imshow('frame',frame)

    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break  



out1.release()