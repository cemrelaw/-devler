def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")

    isim = liste[0]
    vize_1 = int(liste[1])
    vize_2 = int(liste[2])
    final = int(liste[3])

    global harf_notu
    global not_ortalaması 
    not_ortalaması = vize_1 * 0.3 + vize_2 * 0.3 + final * 0.4

    if not_ortalaması >= 90:
        harf_notu = "AA"
    elif not_ortalaması >= 85 :
        harf_notu = "BA"
    elif not_ortalaması >= 80:
        harf_notu = "BB"
    elif not_ortalaması >= 75:
        harf_notu = "CB"
    elif not_ortalaması >= 70:
        harf_notu = "CC"
    elif not_ortalaması >= 65:
        harf_notu = "DC"
    elif not_ortalaması >= 60:
        harf_notu = "DD"
    elif not_ortalaması >= 55:
        harf_notu = "FD"
    else:
        harf_notu = "FF"

    return isim + "  ----->  not ortalaması: " + str(not_ortalaması) + "  ----->  harf notu: " + harf_notu 


sınıf_ortalaması = 0
sayaç = 0
with open("dosya.txt", "r", encoding= "utf-8") as file:
    aktarma = []

    for i in file:
        aktarma.append(not_hesapla(i))
        sınıf_ortalaması += not_ortalaması
        sayaç += 1

    sınıf_ortalaması /= sayaç

    with open("notlar.txt", "w", encoding= "utf-8") as file2:
        for i in aktarma:
            file2.write(i + "\n")

        file2.write("\nSINIF ORTALAMASI: " + str(sınıf_ortalaması))

with open("dosya.txt", "r", encoding= "utf-8") as file:
    kalanlar = []
    geçenler = []

    for i in file:
        not_hesapla(i)
        if harf_notu == "FF":
            kalanlar.append(not_hesapla(i))
        else:
            geçenler.append(not_hesapla(i))   

    with open("kalanlar.txt", "w", encoding= "utf-8") as file3:
        for i in kalanlar:
            file3.write(i + "\n")
    
    with open("geçenler.txt", "w", encoding= "utf-8") as file4:
        for i in geçenler:
            file4.write(i + "\n")
