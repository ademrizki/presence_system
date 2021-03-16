import cv2
import numpy as np
import MySQLdb
import datetime
import time
import os

recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read("trainner/trainner.yaml");
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
now = datetime.datetime.now()

def getProfile(id):
    db = MySQLdb.connect("localhost","root","","presensi")
    curs = db.cursor()
    cmd = "SELECT * FROM facebase WHERE npm="+str(id)
    curs.execute(cmd)
    profile = None
    rows = curs.fetchall()
    for row in rows:
        profile=row
    curs.close()
    return profile

def getFace_info():
    count = 0
    ulang = True
    try:
        cam = cv2.VideoCapture(0)
        while ulang:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            count = count + 1
            if count == 360:
                ulang = False
            else:
                for(x,y,w,h) in faces:
                    id, conf = recognizer.predict(gray[y:y+h,x:x+w])
                    profile = getProfile(id)
                    print (str(id) + str(conf))
                    if(conf<43):
                        if(profile!=None):
                            cv2.imwrite("absensi/"+profile[2]+"/"+now.strftime("%Y-%m-%d %H-%M")+"[1]"+".jpg", img)
                            cv2.imwrite("absensi/"+profile[2]+"/"+now.strftime("%Y-%m-%d %H-%M")+"[2]"+".jpg", img)
                            time.sleep(2)
                            return profile[1],profile[2]
                            break
                    cv2.imshow('img',img)
                    if cv2.waitKey(10) & 0xFF==ord('q'):
                        break
        cam.release()
        cv2.destroyAllWindows()
    except:
        pass
