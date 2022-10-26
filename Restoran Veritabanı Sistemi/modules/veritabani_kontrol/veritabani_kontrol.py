import sqlite3

acilis = sqlite3.connect("db.sqlite")
AcilisImlec = acilis.cursor()
AcilisImlec.execute("CREATE TABLE IF NOT EXISTS db (RandevuKodu, MasaNo, BaslangicSaat, BitisSaat, KisiSayisi)")
acilis.close()

def VeriGir(RandevuKodu, MasaNo, BaslangicSaat, BitisSaat, KisiSayisi):
    veritabani = sqlite3.connect("db.sqlite")
    imlec = veritabani.cursor()
    imlec.execute("INSERT INTO db VALUES ('{d1}', '{d2}', '{d3}', '{d4}', '{d5}')".format(d1 = RandevuKodu, d2 = MasaNo, d3 = BaslangicSaat, d4 = BitisSaat, d5 = KisiSayisi))
    veritabani.commit()
    imlec.execute("SELECT * FROM db")
    RandevuSira = len(imlec.fetchall())
    veritabani.close()
    liste = [RandevuSira, RandevuKodu]
    return liste

def VeriSil(RandevuKodu):
    veritabani = sqlite3.connect("db.sqlite")
    imlec = veritabani.cursor()
    imlec.execute("DELETE FROM db WHERE RandevuKodu='" + RandevuKodu + "'")
    veritabani.commit()
    veritabani.close()

def VeriCek(RandevuSira):
    veritabani = sqlite3.connect("db.sqlite")
    imlec = veritabani.cursor()
    imlec.execute("SELECT * FROM db")
    liste = imlec.fetchmany(RandevuSira)
    bilgiler = liste[RandevuSira - 1]
    veritabani.close()
    return bilgiler

def ButunRandevular():
    veritabani = sqlite3.connect("db.sqlite")
    imlec = veritabani.cursor()
    imlec.execute("SELECT * FROM db")
    bilgiler = imlec.fetchall()
    veritabani.close()
    return bilgiler

def VeriDegistir(RandevuKodu, MasaNo, BaslangicSaat, BitisSaat, KisiSayisi):
    veritabani = sqlite3.connect("db.sqlite")
    imlec = veritabani.cursor()
    imlec.execute("UPDATE db SET RandevuKodu='{d1}', MasaNo='{d2}', BaslangicSaat='{d3}', BitisSaat='{d4}', KisiSayisi='{d5}' WHERE RandevuKodu='{d1}'".format(d1 = RandevuKodu, d2 = MasaNo, d3 = BaslangicSaat, d4 = BitisSaat, d5 = KisiSayisi))
    veritabani.commit()
    veritabani.close()
    liste = [RandevuKodu, MasaNo, BaslangicSaat, BitisSaat, KisiSayisi]
    return liste

def Yenile():
    veritabani = sqlite3.connect("db.sqlite")
    imlec = veritabani.cursor()
    imlec.execute("DROP TABLE db")
    imlec.execute("CREATE TABLE db (RandevuKodu, MasaNo, BaslangicSaat, BitisSaat, KisiSayisi)")
    veritabani.close()