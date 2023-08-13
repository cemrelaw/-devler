import sqlite3
from time import sleep

class Kitap():

    def __init__(self, isim, yazar, yayinevi, tur, baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
    
    def __str__(self):

        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)

class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "create table if not exists kitaplar (isim text, yazar text, yayinevi text, tur text, baski int)"
            
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
            
        self.baglanti.close()

    def kitaplari_goster(self):
        
        sorgu = "select * from kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("kütüphanede kitap bulunmuyor.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
        
    def kitap_sorgula(self, isim):

        sorgu = "select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("aradığınız kitap kütüphanede bulunmuyor...")
        
        else: 
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
            
    def kitap_ekle(self,kitap):
        
        sorgu = "insert into kitaplar values(?,?,?,?,?)"
        self.cursor.execute(sorgu, (kitap.isim, kitap.yazar, kitap.yayinevi, kitap.tur, kitap.baski))
        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "delete from kitaplar where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()

    def baski_yukselt(self, isim):

        sorgu = "select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("böyle bir kitap bulunmuyor.")

        else:
            baski = kitaplar[0][4]
            baski +=1

            sorgu2 = "update kitaplar set baski = ?, where isim = ?"
            self.cursor.execute(sorgu2, (baski, isim))
            self.baglanti.commit()
            