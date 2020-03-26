
import sqlite3,os

dosya = 'deneme.Seval'
dosya_mevcut = os.path.exists(dosya)

vt = sqlite3.connect(dosya)
im = vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS personel (isim,soyisim)""")
if not dosya_mevcut:
	im.execute("""INSERT INTO personel VALUES ("Bahar","KARAKAYA")""")
	im.execute("""INSERT INTO personel VALUES ("Seval","Gurhan")""")
	vt.commit()
    #Burada veriyi tekrar tekrar yazmasını engelledik.

im.execute("""SELECT * FROM personel""") #Personelden her şeyi seç.

#veriler = im.fetchall() >> verilerin hepsini alır.
#print(veriler)
print(im.fetchone())
print(im.fetchone())
print(im.fetchone())
#print(im.fetchmany(1)) >> verilerin istediğimiz tanesini alır. 
print(im.execute("SELECT name FROM sqlite_master"))
im.execute("SELECT * FROM personel WHERE isim = 'Seval'") 
print(*im.fetchall())
vt.close()
