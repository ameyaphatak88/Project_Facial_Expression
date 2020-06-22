import cv2
import os
import sys
from flask import Flask
import Recognizer

def get_output_filename(ipfilename):
  fname = str(ipfilename)
  onlyfname,extn = os.path.splitext(fname)
  newfname = onlyfname + "_out" + extn
  return newfname


def read_and_write(filepath):
  assert os.path.isfile(filepath), 'Invalid filepath as argument'

  video1 = cv2.VideoCapture(filepath)

  frame_width  = int(video1.get(3)) # float
  frame_height = int(video1.get(4)) # float

  s = (frame_width, frame_height)

  outfile = get_output_filename(filepath)
  out1 = cv2.VideoWriter(outfile,
                        cv2.VideoWriter_fourcc('M','J','P','G'), 
                        100, 
                        (frame_width, frame_height))

  while(True):
    ret, frame = video1.read()
    if ret == True: 
      
      # Write the frame into the file 'output.avi'
      out1.write(frame)

      # todo
      #emotion = Recognizer.predict(frame)
      #print(emotion)
      frame = Recognizer.predict_and_rectangle(frame)

      # Display the resulting frame    
      cv2.imshow('frame',frame)

      # Press Q on keyboard to stop recording
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Break the loop
    else:
      break  

  out1.release()



if __name__ == "__main__":
  assert (len(sys.argv) == 2), 'Required number of arguments not passed'
  filepath = sys.argv[1]
  read_and_write(filepath)
