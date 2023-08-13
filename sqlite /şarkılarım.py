import sqlite3

class Şarkı():

    def __init__ (self, isim, sanatci, album, sure):

        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.sure = sure

    def __str__ (self):
        return "isim: {} \nsanatci:{} \nalbum:{} \nsure: {}".format(self.isim, self.sanatci, self.album, self.sure)
    
class Kitaplık():
    
    def __init__ (self):
        self.baglanti_kur()

    def baglanti_kur(self):
        self.baglanti = sqlite3.connect("sarki kitapligim.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "create table if not exists kitapliks (isim text, sanatci text, album text, sure int)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def şarkı_ekle(self, isim, sanatci, album, sure):

        şarkı = Şarkı (isim, sanatci, album, sure)
        sorgu = "insert into kitapliks values (?, ?, ?, ?)"
        self.cursor.execute(sorgu(şarkı.isim, şarkı.sanatci ,şarkı.album, şarkı.sure))
        self.baglanti.commit() 

    def şarkı_sil(self, isim):

        sorgu = "delete from kitapliks where isim = ?"
        self.cursor.execute(sorgu(isim, ))
        self.baglanti.commit()

    def şarkı_görüntüle(self, isim):

        sorgu = "select * from kitapliks where isim = ?"
        self.cursor.execute(sorgu(isim, ))
        liste = self.cursor.fetchall()
        for i in liste:
            şarkı = Şarkı(i[0],i[1],i[2],i[3])
            print(i)

    def şarkı_süresi(self, sure):

        top_sure = 0
        sorgu = "select * from kitapliks"
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()
        for i in liste:
            top_sure += liste[i][3]
        return top_sure