# all ve any True üreten bir liste bekler

# ------------ all ------------
# all kendisine gelen tüm elemanlara tek tek bakar hepsinin True olduğu durumda True döndürür.
# herhangi birinin False olduğu durumda False döndürür.

# 1 değerinin ve herhangi bir dolu değerin karşılığı True dir
# 0 ve '' boş değerin karşılığı false dir.(not : ' ' true)
sonuc = all([True, True, ' ', False])
print(sonuc)  # false yazar.


# ---------------- any ------------------
# any de herhangi biri true ise true döndürür
sonuc = any([True, True, False, False])
print(sonuc)  # true yazar.


# - 1

sayilar = [0, 1, 3, 4, 6, 78, 10]
# sayilar dizisinde değerleri true false olarak yazdırdık
sonuc = [bool(sayi) for sayi in sayilar]
print(sonuc)

# içlerinde False (0) olduğu için all False döner
sonuc = all([bool(sayi) for sayi in sayilar])
print(sonuc)

# içlerinde ture olduğu için any True döner
sonuc = any([bool(sayi) for sayi in sayilar])
print(sonuc)

# filtreleme
sonuc = all([bool(sayi) for sayi in sayilar if sayi % 2 == 1])  # ture
print(sonuc)

# çift sayı true, tek sayı false getirsin
# aşağıda bir filtreleme yapmadık any all kullanmadık ama değerlerin bool karşılıklaırnı yazdırdık
sonuc = [sayi % 2 == 0 for sayi in sayilar]
print(sonuc)

# peki herhangi biri çift sayı mı?
sonuc = any([sayi % 2 == 0 for sayi in sayilar])
print(sonuc)

# tek sayı var mı ?
sonuc = all([sayi % 2 == 0 for sayi in sayilar])
print(sonuc)  # false çünkü tek sayılar false döner


# - 2

kisiler = ["ali", "ahmet", "çınar"]

# tüm kisiler a ile mi baslıyor ?
sonuc = [kisi[0] == "a" for kisi in kisiler]
print(sonuc)
# yukarıdakini filtreleyip tüm sınıf için sorgu yapabiliriz.
sonuc = all([kisi[0] == "a" for kisi in kisiler])  # hepsi a ile mi baslıyor
# herhangi biri a ile baslıyor mu
sonuc = any([kisi[0] == "a" for kisi in kisiler])
print(sonuc)


# comphersion işleminde en başla karşılaştırma operatoru kullanırsan listedeki değerler true false olarak döner
# çünkü nerde karışlastırma operatorleri varsa orası bool türü döner
# en sonra if kisi[0]=='a' diye de filtreleme yapabilirdin ama o zaman liste true flase dönmezdi sadece seçilenler gelirdi