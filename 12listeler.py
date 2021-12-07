"""
------Listeler üzerinde ekleme, güncelleme, silme işlemleri--------


"""
# ----------eleman yazdırma---------------------

diller = ["Python", "C#", "Java", "Javascript"]
sonuc = type(diller)  # list döner
sonuc = diller[2:]  # 2. indexten başlar sona kadar alır
sonuc = diller[0:2]  # 0. dan başlar ve 2 tane döner 0 ve ve 1
sonuc = diller[:-1]  # en sonuncuya kadar döner ama en sonuncuyu almaz
sonuc = diller[:3]  # 3. dahil almaz 3 e kadar alır
sonuc = diller[-3:-1]
print(sonuc)


# -------------eleman değiştirme-------

diller[0] = "Gamze"
diller[-1] = "Ceylan"  # en sondakini değiştirir
sonuc = diller
print(sonuc)


# ----------eleman sayisi bulma-------------

elemanSayisi = len(diller)
print(elemanSayisi)


# ------------------metot kullanmadan eleman ekleme--------------

# ama bu yöntem orjinal diziyi eklemez sadece birleştirip bize gösterir. diller hala 5 elemanlı
sonuc = diller + ["Angular", "Vue.js"]
print(sonuc)


# -------------değer mevcut mu-----------------

# "Gamze" dahilse evet yazar
if "Gamze" in diller:
    print("evet")


# ------------liste elemanlarını yazdırma----------

# x üzerine elemanları alır
for x in diller:
    print(x)


# ---------------liste içinden eleman silme--------

# index no verip del ile silebiliriz
del diller[0]
print(diller)
