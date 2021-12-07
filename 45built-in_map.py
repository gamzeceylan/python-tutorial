# ------------------- map() --------------------
# elimizde bir liste var ve liste üzerindeki elemanlarda her birinde aynı işlemi yapmak istiyoruz
# ya da dic listeside özel bir key i almak isiyorsan
# örn bütün sayıları 6 ile çarpalım, 2 ile modunu alalım, karelerini alalım vs. yani bir kriter olamalı
# iterable obj = liste
# bir kriter var ve o kriteri her liste elemanı üzerinde uygulayacaksan. zaten map içine oku bir func ve iterable alır
# map, map türündendir listeye çevrilmesi gerekir
# !!! map içine fonksiyonu değil, fonksiyonun referansını verirsin

sayilar = [1, 3, 5, 7, 23, 6]
kareleri = []

# -- alternatif yol
# birden fazla liste üzerinde işlem yapmak sitediğinde her biri için bunu yazmak zorunda kalırsın. gereksiz
for i in sayilar:
    kareleri.append(i**2)


# -- guzel yol

def kareAl(sayi):
    return sayi**2


# - 1
sonuc = list(map(kareAl, sayilar))
print(sonuc)

# - 2
# map içi bir func istediği için içine lambmda da yazabilirsin
sonuc = list(map((lambda a: a**2), sayilar))
print(sonuc)

# - 3
rakamlar = ["1", "3", "5", "6", "7"]
isimler = ["gamze", "beyza", "melih", "fatih"]

sonuc = list(map(int, rakamlar))  # sadece int yazdık dikkat et
sonuc = list(map(abs, sayilar))  # abs() yazmadık.
sonuc = list(map(float, sayilar))
sonuc = list(map(str.capitalize, isimler))
print(sonuc)

# - 4
kullanicilar = [
    {"ad": "ali", "soyad": "yılmaz"},
    {"ad": "mehmet", "soyad": "ceylan"}

]

#kullaniciların sadece isim bilgisi
sonuc = list(map((lambda isim: isim["ad"]), kullanicilar))
print(sonuc)