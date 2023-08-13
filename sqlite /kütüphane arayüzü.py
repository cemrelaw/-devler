from kütüphane import*

print(""" 
KÜTÜPHANE PROGRAMI
      
İŞLEMLER:
      1-) KİTAPLARI GÖRÜNTÜLE
      2-) KİTAP SORGULA
      3-) KİTAP EKLE
      4-) KİTAP SİL
      5-) BASKI YÜKSELT

      ÇIKMAK İÇİN: "q"

""")
      
kütüphane = Kütüphane()

while True:

    işlem = input("yapmak istediğiniz işlemi tuşlayınız:  ")

    match işlem:
        case "q":
            print("PROGRAM SONLANDIRILIYOR...")
            sleep(1)
            print("TEKRAR BEKLERİZ.")
            quit

        case "1":
            print("kitaplar görüntüleniyor...")
            sleep(1)
            kütüphane.kitaplari_goster()

        case "2":
            isim = input("aradığınız kitabın adını giriniz: ")
            print("kitap sorgulanıyor...")
            sleep(1)
            kütüphane.kitap_sorgula(isim)

        case "3":
            print("kütüphaneye eklemek istediğiniz kitabın bilgilerini giriniz.")
            sleep(0.5)

            isim = input("isim: ")
            yazar = input("yazar: ")
            yayinevi = input("yayinevi: ")
            tur = input ("tür: ")
            baski = int(input("baski: "))

            yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)
            print("kitap ekleniyor...")
            sleep(1)
            kütüphane.kitap_ekle(yeni_kitap)
            print("kitap başarıyla eklendi.")

        case "4":
            isim = input("kütüphaneden silmek istediğiniz kitabın adını giriniz: ")
            cevap = input("işleme devam etmek istediğinizden emin misiniz? (e/h)")
            match cevap:
                case "e":
                    print("kitap siliniyor...")
                    sleep(1)
                    kütüphane.kitap_sil(isim)
                    print("kitap silindi.")
                case "h":
                    print("işlem iptal edildi.")
                    break
                case _:
                    print("geçersiz işlem...")
                    break

        case "5":
            isim = input("baskısını yükseltmek istediğiniz kitabın adını giriniz: ")
            print("kitabın baskısı yükseltiliyor...")
            sleep(1)
            kütüphane.baski_yukselt(isim)
            print("seçtiğiniz kitabın baskısı yükseltildi.")
        