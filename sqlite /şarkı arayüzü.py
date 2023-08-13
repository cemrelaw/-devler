from şarkılarım import*
from time import sleep

kitaplık = Kitaplık()

print ("""
KİTAPLIĞIM
       """)
sleep(1)

print("""

İŞLEMLER: 
      1-) ŞARKI EKLE
      2-) ŞARKI SİL
      3-) ŞARKILARIM
      4-) TOPLAM ÇALMA SÜRESİ

      çıkmak için "q"

""")

while True:

    işlem = input("yapmak istediğin işlemi seç: ")

    match işlem:
        case "q":
            print("sonra görüşürüz...")
            sleep(1)
            break
        case "1":
            print("kitaplığına hangi şarkıyı eklemek istersin?")
            isim = input("şarkının adı: ")
            sanatci = input("sanatçı: ")
            album = input("albüm: ")
            sure = input("sure: ")
            print("şarkı kitaplığına ekleniyor...")
            sleep(1)
            kitaplık.şarkı_ekle(isim, sanatci, album, sure)
            print("şarkı başarıyla kitaplığına eklendi.")
        
        case "2":
            print("hangi şarkıyı kitaplığından kaldırmak istersin?")
            isim = input("şarkının adı: ")
            print("şarkı kitaplığından kaldırılıyor...")
            sleep(1)
            kitaplık.şarkı_sil(isim)
            print("şarkı kitaplığından başarıyla kaldırıldı.")

        case "3":
            print("hangi şarkıyı dinlemek istersin?")
            isim = input("şarkının adı: ")
            print("şarkı açılıyor...")
            sleep(1)
            kitaplık.şarkı_görüntüle(isim)

        case "4":
            print("kitaplığının toplam çalma süresi hesaplanıyor...")
            sleep(1)
            kitaplık.şarkı_süresi()

        case _:
            print("geçersiz tuşlama")



        