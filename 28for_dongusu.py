# ----------------- for donguleri --------------------

sayilar = [1, 2, 3, 5, 7, 87, 53, 3]

# x her elemanı üzerine kopyalar
for i in sayilar:
    print(i)


# döngü sayilar uzunluğu kadar dönüceğinden ekrana 8 kere merhaba yazar.
for i in sayilar:
    print(f"{i}. Merhaba")


isimler = ["Gamze", "Zeynep", "Melih"]
for i in isimler:
    print(i)


# isim bir karakter dizisidir. i her elemeanı tek tek üzerine alır
isim = "Gamze Ceylan"
for i in isim:
    print(i)


# _tuple bir liste ama içindeki her değer bir tuple ye karşılık gelir.
_tuple = [(1, 2), (3, 4), (5, 6), (7, 8)]

# print(type(_tuple))  llist döner
# print(type(_tuple[0]))   tuple doner
for a, b in _tuple:
    print(a, b)


_dict = {"k1": 1, "k2": 2, "k3": 3}
# x key alır
for x in _dict:
    print(x)

# value leri yazar
for x in _dict:
    print(_dict[x])

# value yazar.
for x in _dict.values():
    print(x)

# hem key hem value yazar
for key, value in _dict.items():
    print(key, value)


##################### uygulama ######################

urunler = [
    {"name": "iphone XR", "price": "7000"},
    {"name": "iphone 11", "price": "7500"},
    {"name": "iphone 5", "price": "6000"},
    {"name": "samsung XR", "price": "5000"}
]
# ürünlerin fiyatarının toplamı?


toplam = 0
for i in urunler:
    toplam += int(i['price'])  # böyle direkt alabiliyormuşuz

print(toplam)

kelime = input("Kelime :")
for urun in urunler:
    if(urun['name'].find(kelime.lower()) > -1):
        print(f"urun adi : {urun['name']}, urun fiyatı {urun['price']}")
