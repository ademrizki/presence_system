import MySQLdb
import getpass
import signal
import sys

lanjut = True
db = MySQLdb.connect("localhost","root","","presensi")
cur = db.cursor()

def signal_handler(signal, frame):
    global lanjut
    print ("\nCTRL+C captured, ending read")
    sys.exit(0)
    lanjut = False


def getPIN_info():
    global lanjut
    while lanjut:
        signal.signal(signal.SIGINT, signal_handler)
        try:
            passKey = str(getpass.getpass("Masukan PIN (6 digit) : "))
            if (passKey and len(passKey) == 6):
                sql = "select * from passkey where pkey=%s" %passKey
                cur.execute(sql)
                result = cur.fetchall()
                db.commit()
                for row in result:
                    npm = row[3]
                    nama = row[2]
                    kelas = row[4]    
                print ("\nNama : %s \nNPM : %s \nKelas : %s " %(nama, npm, kelas))
                return npm, nama
            else:
                print ("\n\n\nMasukan salah, harap diulang")
        except UnboundLocalError:
            print ("\nMaaf, Data belum terdaftar")

                
            
            
            
            
        
