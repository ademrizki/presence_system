import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8,
                                               grid_x=8, grid_y=8);
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImageAndLabels(path):
    ImagePath=[os.path.join(path, f) for f in os.listdir(path)]
    faceSamples=[]
    Ids=[]
    for imagePath in ImagePath:
        pilImage = Image.open(imagePath).convert('L')
        ImageNp = np.array(pilImage,'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(ImageNp)
        for (x,y,w,h) in faces:
            faceSamples.append(ImageNp[x:x+w, y:y+h])
            Ids.append(Id)
    return faceSamples,Ids

faces, Ids = getImageAndLabels('dataSet')
recognizer.train(faces, np.array(Ids))
recognizer.save('trainner/trainner.yaml')
