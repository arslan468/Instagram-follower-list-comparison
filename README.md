# 🕵️‍♂️ Instagram Takipçi Analiz Aracı (Insta-Stalker)

Merhaba bu proje Instagram'daki takipçi hareketliliğimi tespit etmek amacıyla yazılmıştır. 

## 🚀 Ne İşe Yarıyor?
Instagram'dan hesaplar merkezi üzerinden dışarı aktardığınız iki farklı zaman dilimine ait "Takipçiler" listesini (HTML formatında) okur ve şunları anında listeler:
- ❌ **Takipten Çıkanlar:** Eskiden olup, şimdi olmayan takipçiler. 
(Program kullanıcı adına göre listeleme yaptığı için kullanıcı adını değiştiren kullanıclar da burada gözükecektir)
- ✅ **Yeni Gelenler:** Yeni Takipçiler.

## 🔒 Gizlilik ve Veri Güvenliği (ÖNEMLİ!)
> **Not:** Bu depodaki HTML dosyalarında bulunan isimler **tamamen sahte (fake) isimlerdir.** Kendi kişisel verilerimin ve beni takip eden insanların gizliliğini korumak adına, projeyi GitHub'a yüklemeden önce `Faker` kütüphanesini kullanarak tüm kullanıcı adlarını rastgele isimlerle değiştirdim. 

Fakat aklınızda soru işareti kalmasın: **Programın algoritması ve çalışma mantığı %100 doğru ve sorunsuz çalışmaktadır.** Kendi gerçek verilerinizle (HTML çıktılarıyla) denediğinizde çalıştığını göreceksiniz. 🛠️

## 🛠️ Nasıl Çalıştırılır?

### 1. Kendi sistemine projeyi klonla:
   git clone [https://github.com/arslan468/Instagram-follower-list-comparison.git]

### 2. Gerekli kütüphane
  pip install beautifulsoup4 lxml

### 3. Kendi takipçi listelerinizi ekleyip dosya yolunu düzenledikten sonra çalıştığını görüceksiniz
