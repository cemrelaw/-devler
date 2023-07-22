import time

class kumanda():

    def __init__(self, ac_kapa = "kapalı", ses_ayarı = 0, kanal_listesi = {0: "MENU", 1: "TRT"}, mevcut_kanal = 0):
        self.ac_kapa = ac_kapa
        self.ses_ayarı = ses_ayarı
        self.kanal_listesi = kanal_listesi
        self.mevcut_kanal = mevcut_kanal
    
    def tv_ac(self):

        if self.ac_kapa == "kapalı":
            print("TV açılıyor...")
            time.sleep(0.5)
            self.ac_kapa = "açık"
            print("Hoşgeldiniz.")

        else:
            print("TV kapatılıyor...")
            time.sleep(0.5)
            print("Hoşçakal.")
            time.sleep(1)
            self.ac_kapa = "kapalı"
            quit

    def ses_ac(self):
        
        print (f"ses seviyesi : {self.ses_ayarı}")

        if self.ses_ayarı < 30:
            
            print("ses açılıyor...")
            self.ses_ayarı += 1
            time.sleep(0.3)
            print(f"yeni ses seviyesi: {self.ses_ayarı}")
        else:
            print(f"ses maksimum seviyede. \nses seviyesi: {self.ses_ayarı}")

    def ses_kıs(self):
        
        print(f"ses seviyesi: {self.ses_ayarı}")

        if self.ses_ayarı > 0:
            print("ses kısılıyor...")
            self.ses_ayarı -= 1
            time.sleep(0.3)
            print(f"yeni ses seviyesi: {self.ses_ayarı}")
        else:
            print(f"ses minimum seviyede. \nses seviyesi: {self.ses_ayarı}")
    
 
    
    def kanal_ekle(self):
        
        print("mevcut kanal listesi: ", self.kanal_listesi)
        time.sleep(0.5)
        no = int(input("eklemek istediğiniz kanalın numarasını giriniz: "))
        ad = input("eklemek istediğiniz kanalın adını giriniz: ")
        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.update({no: ad})
        print(f"{no} numaralı {ad} kanalı listenize eklendi.")
        time.sleep(0.3)
        print("mevcut kanal listesi: ", self.kanal_listesi)

    def kanallar(self):
        print("kanal listesi: ")
        for x,y in self.kanal_listesi.items():
            print(x,y)
    

    def kanal_değiştir(self):

        print(f"mevcut kanal:{self.mevcut_kanal} \nkanal listesi: {self.kanal_listesi}")
        kanal_no = int(input("açmak istediğiniz kanal numarasını giriniz: "))

        if kanal_no in self.kanal_listesi:
            print("kanal değiştiriliyor...")
            time.sleep(0.3)
            kanal = self.kanal_listesi[kanal_no]
            self.mevcut_kanal = kanal
            print(f"mevcut kanal: {self.mevcut_kanal}")
        else:
            print("geçersiz kanal numarası")

kumanda = kumanda()
print("\n\n\tAKILLI KUMANDA ")

while True:

    print("\n\tYAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ... ")
    time.sleep(0.3)
    mod = int(input("\n1: On/Off \n2: V+ \n3: V- \n4: Kanal Ekle \n5: Kanal Listesi  \n6: Kanal Değiştir  \n0: Çıkış \n"))

    match mod:
        case 1:
            kumanda.tv_ac()
        case 2:
            kumanda.ses_ac()
        case 3:
            kumanda.ses_kıs()
        case 4:
            kumanda.kanal_ekle()
        case 5:
            kumanda.kanallar()
        case 6: 
            kumanda.kanal_değiştir()
        case 0: 
            break
    
    time.sleep(0.5)
