from bs4 import BeautifulSoup

def takipcileri_cek(adres): 
    try: 
        with open(adres, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f,'lxml')
        takipciler = set()
        linkler = soup.find_all('a', target= "_blank")

        for link in linkler: 
            kullanici_adi = link.text.strip()
            if kullanici_adi: 
                takipciler.add(kullanici_adi)
        return takipciler
    
    except FileNotFoundError:
        print("Hata !Dosya Yolunda dsoya yok")

        return set()
    
eski = 'eski_takipciler.html'
yeni = 'yeni_takipciler.html'

eski_takipciler = takipcileri_cek(eski)
yeni_takipciler = takipcileri_cek(yeni)

print(f"Eski takipçi sayısı: {len(eski_takipciler)}")
print(f"Yeni takipçi sayısı: {len(yeni_takipciler)}")
print("-" * 30)

takipten_cikanlar = eski_takipciler - yeni_takipciler
print(f"❌Takipten Çıkanlar ({len(takipten_cikanlar)} kişi): ")
for kisi in takipten_cikanlar:
    print(f"❗️    - {kisi}")

print("-" * 30)

yeni_gelenler = yeni_takipciler - eski_takipciler

print(f"✅Yeni gelenler ({len(yeni_gelenler)} kişi): ")
for kisi in yeni_gelenler:
    print(f"💐      {kisi}")

