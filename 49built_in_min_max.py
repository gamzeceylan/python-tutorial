# min de sayılsal olarak en küçük ya da alfatik olarak ilk geleni bulabilirsin
# max ta da tam tersi
# min max fonktiyonlarından farkı dic yapısında vs labdra kullanabiliyor olman, filtreleme yapabiliryorsun


sayilar = [1, 5, 2, 9, 2, 54, 75, 3, 232]
sonuc = min(sayilar)  # 1
sonuc = max(sayilar)  # 232

harfler = ["a", "b", "h", "g", "r"]
sonuc = min(harfler)  # a
sonuc = max(harfler)  # r

isimler = ["gamze", "elifs", "sena", "ece"]
sonuc = min(isimler)
sonuc = max(isimler)

print(sonuc)

# aşağıdaki ile tek tek isim uzunlukları döner
sonuc = [len(isim) for isim in isimler]
print(sonuc)

# isim uzunluğu en kısa olan döner
sonuc = min([len(isim) for isim in isimler])
print(sonuc)

# max uzunluğa sahip isim
sonuc = max(isimler, key=lambda n: len(n))
print(sonuc)


# min uzunluğa sahip isim
sonuc = min(isimler, key=lambda n: len(n))
print(sonuc)


# --- ornek

urunler = [
    {"title": "iphone x", "price": 5000},
    {"title": "iphone xr", "price": 6000},
    {"title": "samsung", "price": 7000}

]
 
sonuc=min(urunler, key=lambda urun:urun["price"])
print(sonuc)

sonuc=min(urunler, key=lambda urun:urun["price"])["title"]
print(sonuc)

sonuc=max(urunler, key=lambda urun:urun["price"])["title"]
print(sonuc)

#------------ min max kullanmazsak --------
max=0
for urun in urunler:
    if urun["price"]>max:
        max=urun["price"]

print(max)