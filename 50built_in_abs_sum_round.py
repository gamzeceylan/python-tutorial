# ---- sum toplam değeri bulur -----
sayilar = [34, 98, 2, 5]
sonuc = sum(sayilar)
print(sonuc)

# üzerine 10 ekler
sonuc = sum(sayilar, 10)
print(sonuc)

# --- örn---
urunler = [
    {"title": "iphone x", "price": 5000},
    {"title": "iphone xr", "price": 6000},
    {"title": "samsung", "price": 7000}

]

# urunler fiyrının toplamını istiyorsan önce urunlerin fiyarını bir liste olarak getirmen gerek []
# listeyi getirdik şimdi toplam alabiliriz
sonuc = [urun["price"] for urun in urunler]
print(sonuc)

# bu listeyi de sum a yollardan toplar hepsini
toplamFiyat = sum([urun["price"] for urun in urunler])
print(toplamFiyat)

# fiyat ortalamaısnı bulalım
sonuc = toplamFiyat / len(urunler)
print(sonuc)

# listede olan bir urun satışta değilse, fiyatı 0 sa nasıl hesaplanır ?
# satışta olamıdğı için ortalama hesaplarken urun sayısına katmamamız gerekir
urunler = [
    {"title": "iphone x", "price": 5000},
    {"title": "iphone xr", "price": 6000},
    {"title": "samsung", "price": 7000},
    {"title": "nokia", "price": 0}
]
# toplam fiyatta 0 toplanır ama bu önemli değil
toplamFiyat = sum([urun["price"] for urun in urunler])
# diyatı 0 olanları eledik
urunAdedi = len([urun for urun in urunler if urun["price"] > 0])
ortalama = toplamFiyat/urunAdedi
print(ortalama)

# -------- round --------------------
# round yuvarlama yapmak için kullanılır
sonuc = round(10.2)  # 10.2 yi 10 a yuvarlar
print(sonuc)

sonuc = round(10.6)  # 10.2 yi 11 a yuvarlar
print(sonuc)

sonuc = round(10.5)  # ortayı aşağı yuvarlar. 10 a
print(sonuc)

#aşağıyı anlamadım
sonuc = round(1.7113312,2)
print(sonuc)