# 1- Samsung S5, Samsung S6, Samsung S7, Samsung S8 listesi oluştur.
telefonlar = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]

# 2- Liste kaç elemanlı?
elemanSayisi = len(telefonlar)
print(elemanSayisi)

# 3- Listenin ilk ve son elemanı nedir ?
ilkEleman = telefonlar[0]
sonEleman = telefonlar[-1]
print(f"İlk eleman {ilkEleman}, Son eleman {sonEleman}")


# 4- Samsung S5 i Samsung S9 ile değiştir
telefonlar[0] = "Samsung S9"


# 5- Samsung S6 listenin bir elemanı mıdır?
if "Samsung S6" in telefonlar:
    print("elemanıdır")

"""
NOT : (:) yazmak ve ardından bir tab ile yazmak blok oluşturur.
diğer dillerde {} karşılığıdır

"""

# 6- Listenin -3 indeksindeki değer ?
eleman = telefonlar[-3]
print(eleman)


# 7- Listenin ilk 2 elemanını al
sonuc = telefonlar[0:2]
print(sonuc)

# 8- Listenin son 2 elemanı yerine Samsung S9 ve Samsung S10 değerleri ekle
telefonlar[-2:] = ["Samsung S19", "Samsung S10"]
print(telefonlar)

# 9- liste üzerine Iphone X ve Iphone XR ekle
# orjinal liste üzerindeişlem yapmaz
sonuc = telefonlar + ["Iphone X", "Iphone XR"]
print(sonuc)

# 10 Listenin son elemanı silin
del telefonlar[-1]

# 11- Liste elemanlarını tersten yazdır.
print(telefonlar[::-1])


# 13- liste elemanlarını ekrana yazdır.
for x in telefonlar:
    print(x)


# 12- Aşağıdaki veirleri bir liste içinde sakla

# kullaniciA : Yiğit Bilgi 2010, (70, 60, 70)
# kullaniciB : Sena Turan 1999, (80,80,70)
# kullaniciC : Ahmet Turan 1998, (80,70,90)

kullaniciA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
kullaniciB = ["Sena", "Turan", 1999, [80, 80, 70]]
kullaniciC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

ogrenciler = [kullaniciA, kullaniciB, kullaniciC]

print(ogrenciler)

# ogrenciler listesini böyle de yazdırabiliriz (alt alta yazar)
for ogrenci in ogrenciler:
    print(ogrenci)

# ekrana yazdırma
for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyad = ogrenci[1]
    yas = 2021-ogrenci[2]
    ortalama = (ogrenci[3][0] + ogrenci[3][1] + ogrenci[3][2]) / 3
    print(f"{ad} {soyad}, Yaşı : {yas}, Ortalama : {ortalama:1.4}")
    #tam kısımla birlikte toplam 4 basamak gelir
