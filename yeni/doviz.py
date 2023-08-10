import requests
from bs4 import BeautifulSoup

url1 = "https://kur.doviz.com"
page = requests.get(url1)
soup = BeautifulSoup(page.content, "html.parser")

doviz = input("hesaplamak istediğiniz döviz kurunu giriniz:")    
miktar = int(input("kur hesaplamak istediğiniz miktarı giriniz: "))
doviz = doviz.upper()

def kur_hesapla(): 
    deger = soup.find_all("span", {"data-socket-key": doviz})
    deger = deger[0].text.replace(",", ".")
    sonuc = miktar * float(deger)
    print(f"{doviz}: {deger} \n{miktar} {doviz}: {sonuc} TRY")

kur_hesapla()