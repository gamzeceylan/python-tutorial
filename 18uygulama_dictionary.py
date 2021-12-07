# 1- 3 ürün bilgisini (id, ad, fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız
# 2- urun is bilgisini kullanıcıdan alıp ilgili urun bilgisini gösterin

# ----------------------- 1. uygulama --------------------------------
urunler = {}  # boş bir dictionary tanımlayalım

id = input("ID no giriniz : ")
ad = input("Urunun adını giriniz : ")
fiyat = input("Urunun fiyatını giriniz : ")

# id değeri mevcut olmadığı için otomatik ekler. urunler[id]="urun" demekle aynı şey
urunler[id] = {
    "ad": ad,
    "fiyat": fiyat
}

id = input("ID no giriniz : ")
ad = input("Urunun adını giriniz : ")
fiyat = input("Urunun fiyatını giriniz : ")

# id değeri mevcut olmadığı için otomatik ekler. urunler[id]="urun" demekle aynı şey
urunler[id] = {
    "ad": ad,
    "fiyat": fiyat
}
id = input("ID no giriniz : ")
ad = input("Urunun adını giriniz : ")
fiyat = input("Urunun fiyatını giriniz : ")

# id değeri mevcut olmadığı için otomatik ekler. urunler[id]="urun" demekle aynı şey
urunler[id] = {
    "ad": ad,
    "fiyat": fiyat
}

# ------------------------- 2.uygulama ------------------------------------

x = input("aramak istediğiniz id")

print(urunler[x])
print(f"{urunler[x]['ad']}, {urunler[x]['fiyat']}")

"""
NOT : iç içe "" kullanmazsın. "urunler[x]["fiyat"]" bu hatalıdır. 'fiyat' yazmalısın
"""
