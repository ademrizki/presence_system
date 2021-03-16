import IoU
import Read_PIN
import getRPT
import time
import datetime
import signal
import sys
import MySQLdb
import Modul_FaceRec

now = datetime.datetime.now()
FCR = Modul_FaceRec
db = MySQLdb.connect("localhost","root","","laporan")
curs = db.cursor()
lanjut = True

def getMode():
    print ("\nMasukan input untuk memasuki mode ")
    print ("""Mode :(presensi/daftar/update/laporan)(input lowcase)\n""")
    mode = input('Mode : ')
    if mode == "presensi":
        mode = input("Presensi(masuk/keluar) : ")
        if mode == "masuk" or mode == "keluar":
            return mode
        else :
            return "salah"
    elif mode == "daftar" or mode == "update":
        return mode
    elif mode == "laporan":
        return mode
    else:
        return "salah"

def pilih_hari(no_hari):
    if no_hari == "0":
        return "Minggu"
    elif no_hari == "1":
        return "Senin"
    elif no_hari == "2":
        return "Selasa"
    elif no_hari == "3":
        return "Rabu"
    elif no_hari == "4":
        return "Kamis"
    elif no_hari == "5":
        return "Jumat"
    elif no_hari == "6":
        return "Sabtu"
    else:
        return "NULL"

def signal_handler(signal, frame):
    global lanjut
    print("\nCTRL+C captured, ending read.")
    lanjut = False
    curs.close()
    sys.exit(0)

print ("Welcome")
time.sleep(2)
signal.signal(signal.SIGINT, signal_handler)
while (lanjut):
    mode = getMode()
    if mode == "daftar" or mode == "update":
        IoU.action()
        mode = "salah"
    elif mode == "laporan":
        getRPT.RPT_info()
        mode = "salah"
    elif mode == "masuk":
        try:
            (npmPin, namaPin) = Read_PIN.getPIN_info()
            print ("mendeteksi wajah dalam 3 detik")
            time.sleep(3)
            (npmFace, namaFace) = FCR.getFace_info()
            print ("\nMemproses...")
            no_hari = now.strftime("%w")
            Hari = pilih_hari(no_hari)
            if (namaPin == namaFace and npmPin == npmFace):
                curs.execute("INSERT INTO T_"+npmPin+"(tanggal,hari,jamMasuk) VALUES (CURDATE(), '"+Hari+"', CURTIME())")
                db.commit()
                mode = "salah"
            else:
                print ("Wajah dan Data tidak sesuai, silahkan diulang")
        except TypeError:
            print ("Wajah dan Data tidak sesuai, silahkan diulang")
    elif mode == "keluar":
        try:
            no_hari = now.strftime("%w")
            Hari = pilih_hari(no_hari)
            (npmPin, namaPin) = Read_PIN.getPIN_info()
            curs.execute("SELECT * FROM T_" +npmPin+ " where jamKeluar is NULL and jamMasuk is NOT NULL and keterangan is NULL and hari = '"+Hari+"' order by nomor desc limit 1")
            status = 0
            for row in curs:
                status = 1
            if status == 1:
                print ("mendeteksi wajah dalam 3 detik")
                time.sleep(3)
                (npmFace, namaFace) = FCR.getFace_info()
                print ("\nMemproses..")
                if (namaPin == namaFace and npmPin == npmFace):
                    ket = raw_input("\nMasukan Keterangan dari kegitatan hari ini : ")
                    curs.execute("update T_"+npmPin+" set jamKeluar = CURTIME(), keterangan= '"+str(ket)+"' where jamKeluar is NULL and jamMasuk is NOT NULL and keterangan is NULL and hari= '"+Hari+"' order by nomor desc limit 1")
                    db.commit()
                    print ("\n SELESAI \n")
                else:
                    print ("Wajah dan Data tidak sesuai, silahkan diulang")
            else:
                print ("\nInput data masuk terlebih dahulu untuk keluar")
        except TypeError:
            print ("Wajah dan Data tidak sesuai, silahkan diulang")
    elif mode == "salah":
        print ("\nMode salah, silahkan diulang")
            
            

        
        
        











    

