# lis comprehension koşullu ifadeler (MANTIĞINI ÇOK ANLAMADIM)

"""
-koşullu ifadeleri de comprehension ile tanımlayabiliriz

for item in liste:
    if(kosul):
        expression

uzun yazmak yerine : 

[expression for item in liste if kosul]

yazabiliriz.

-[expression for i in list if kosul] : eer sadece if kullanıcaksan kosul sonda olmalı
-[expression if kosul else for i in list] : eger if else kullanıcaksan if else basla for sonda olmalı

"""
# uzun yazım--------------------------------------------------
import datetime
sayilar1 = [1, 45, 32, 76, 3, 2, 123, 90]
sonuc1 = []
for i in sayilar1:
    if i > 30:
        sonuc1.append(i)

print(sonuc1)

# kısa yazım--------------------------------------------------
sayilar2 = [1, 45, 32, 76, 3, 2, 123, 90]
sonuc2 = [i for i in sayilar2 if i > 30]

print(sonuc2)

# farki lı bir kullanım---------------------------------------
sonuc3 = [sayi if (sayi % 2 == 0) else "Tek sayi" for sayi in sayilar1]
print(sonuc3)

# yukarıda dikkar et "Tek sayi" yazaken print kullanmadık. çünkü orayı liste içine ekliyoruz. print ekrana yazdırma


# örnek-------------------------------------------------------
# uzun
fiyatlar = [1000, 3000, 5000, 0, 4000]
vergiler = []
for fiyat in fiyatlar:
    if(fiyat > 0):
        vergiler.append(fiyat*1.88)

print(vergiler)

# kısa
vergiler2 = [fiyat*1.88 for fiyat in fiyatlar if(fiyat > 0)]
print(vergiler2)

vergiler3 = [fiyat*1.88 if fiyat >
             0 else "vergi hesaplanamadi" for fiyat in fiyatlar]
print(vergiler3)

"""
yukarıdakinin uzun hali

for fiyat in fiyatlar:
    if fiyat > 0:
        expression
    else:
        "vergi hesaplanamadi"

"""

# örnek-------------------------------------------------------
# uzun
sonuc4 = []
for x in range(3):
    for y in range(3):
        sonuc4.append((x, y))

print(sonuc4)
# NOT : [( ), ( ), ( )] bu tuple dır

# kısa
sonuc5 = [(x, y) for x in range(3) for y in range(3)]
print(sonuc5)

# örnek-------------------------------------------------------

# isimler listesini küçü harfe çevirip tersten yazdır
isimler = ["Ahmet", "ali", "ÇıNar", "DeniZ"]

sonuc = [i.lower()[::-1] for i in isimler]
print(sonuc)

# string içindeki rakamlardan liste oluştur
string = "Hello 12345 World"

rakamlar = [i for i in string if i.isdigit()]
print(rakamlar)

# yillar dizisinden yaş içeren bir liste oluştur
yillar = [1983, 1999, 2008, 1956, 1986]

simdi = datetime.datetime.now().year

yaslar = [simdi-yil for yil in yillar]
print(yaslar)
