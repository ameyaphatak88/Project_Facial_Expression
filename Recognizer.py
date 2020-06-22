import cv2
from model import FacialExpressionModel
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")

def draw_rectangle(face):
    cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0), 2)
    return fr


def predict(fr):
    gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray_fr, 1.3, 5)

    for(x, y, w, h) in faces:
        fc = gray_fr[y:y+h, x:x+w]
        roi = cv2.resize(fc, (48, 48))

        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

        return (faces, pred)

