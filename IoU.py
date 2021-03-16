import MySQLdb
import cv2
import time
import os
import signal
import getpass
import sys

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
db = MySQLdb.connect("localhost","root","","presensi")
db1 = MySQLdb.connect("localhost","root","","laporan")
lanjut = True

def signal_handler(signal, frame):
    global lanjut
    print ("\nCTRL + C captured, ending read.")
    lanjut = False
    cam.release()
    cv2.destroyAllWindows()
    curs.close()
    sys.exit(0)

def face_insertOrUpdate(id,nama,kelas):
    curs = db.cursor()
    curs1 = db1.cursor()
    curs.execute("SELECT * FROM facebase WHERE npm=" +str(id))
    statData = 0
    for row in curs:
        statData = 1
    if (statData == 1 ):
        curs.execute("UPDATE facebase SET nama=%s, kelas=%s WHERE npm=%s", (nama,kelas,str(id)))
        db.commit()
    else:
        curs.execute("INSERT INTO facebase(npm, nama, kelas)values(%s,%s,%s)", (id,nama,kelas))
        curs1.execute("CREATE TABLE IF NOT EXISTS T_"+str(id)+"(nomor INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(30) default '"+str(nama)+"',kelas VARCHAR(8) default '"+str(kelas)+"', tanggal date NOT NULL, hari VARCHAR(10), jamMasuk time NOT NULL, jamKeluar time, keterangan VARCHAR(255))")
        db.commit()
        db1.commit()

def PIN_insertOrUpdate(nama,id,kelas):
    global lanjut
    while lanjut:
        signal.signal(signal.SIGINT, signal_handler)
        passKey = getpass.getpass("Masukan PIN (6 digit angka) : ")
        if passKey and len(passKey) == 6:
            curs = db.cursor()
            curs2 = db.cursor()
            curs3 = db1.cursor()
            curs.execute("SELECT * FROM passkey WHERE pkey="+str(passKey))
            curs2.execute("SELECT * FROM passkey WHERE npm="+id)
            curs3.execute("SELECT * FROM T_"+id)
            statusData = 0
            for row in curs2:
                statusData = 1
            if (statusData == 1 ):
                curs3.execute("UPDATE T_"+id+" SET nama=%s, kelas=%s", (nama,kelas))
                curs3.execute("ALTER TABLE T_"+id+" ALTER nama SET DEFAULT '"+nama+"'")
                curs3.execute("ALTER TABLE T_"+id+" ALTER kelas SET DEFAULT '"+kelas+"'")
                curs2.execute("UPDATE passkey SET nama=%s, kelas=%s, pkey=%s WHERE npm=%s", (nama, kelas, passKey, id))
                db.commit()
                db1.commit()
            else:
                curs.execute("INSERT INTO passkey (pkey,npm,nama,kelas) VALUES(%s,%s,%s,%s)",(str(passKey), id, nama,kelas))
                db.commit()
            break
        else:
            print ("\nMasukan format PIN dengan benar!\n")
            continue
        
            
def action():
    id = str(input("Masukan NPM : "))
    nama = str(input("Masukan Nama : "))
    kelas= input("Masukan Kelas : ")
    face_insertOrUpdate(id,nama,kelas)
    PIN_insertOrUpdate(nama,id,kelas)
    sampleNum = 0;
    cam = cv2.VideoCapture(0)
    print ("\nBersiap menjalankan kamera, silahkan menghadap kamera")
    time.sleep(5)
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            sampleNum = sampleNum+1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(100)
        if sampleNum>20:
            os.system(" del trainner\\trainner.yaml /s /q")
            os.system("trainner.py")
            try:
                os.mkdir('absensi\\'+nama)
            except WindowsError:
                print ("Folder Presensi Pengguna sudah di buat")
                break
            break
    
    cam.release()
    cv2.destroyAllWindows()
