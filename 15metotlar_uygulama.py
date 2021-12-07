isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']
years = [1998, 2000, 1998, 1987]

# 1- Cenk ismini sona ekle
isimler.append('Cenk')
print(isimler)

# 2- Sena basa ekle
isimler.insert(0, 'Sena')  # -1 sen sonra bir önceye ekler
print(isimler)

# 2- Gamze sona ekle
isimler.insert(len(isimler), 'Gamze')
print(isimler)

# en sondaki elemanı sil
isimler.pop()

# 3- Yigit indexi
temp = isimler.index('Yiğit')
print(temp)

# 4- Yiğit i sil
isimler.remove('Yiğit')
print(isimler)

# 5- Beril listenin elemanı mı? ***************************
# 1.yol
if 'Beril' in isimler:
    print("Elemanıdır")

# 2.yol
sonuc = "Beril" in isimler  # bool döner
print(sonuc)


# 6- Listeyi ters yazdır
# print(isimler.reverse()) hata aldım aşağdaki gibi yapmalısın
isimler.reverse()
print(isimler)

# 7- listeyi alfabetik sırala
isimler.sort()
print(isimler)

# 8- years listesini rakamsal buyukluğe göre sıralama
years.sort()
print(years)

# 9- str= "Iphone X, Iphone XR" karakter dizisini listeye çevir
strng = "Iphone X, Iphone XR"
yeni = strng.split(',')
print(yeni)
"""
- NOT : strng.split(',') bu diziyi böler ama orjinal halini değiştirmez. bunu yeni bir değişkene ataman lazım.
strng.split(',') yazıp bırakırsan ve strng[0] yazarsan sana I verir çünkü orjinal hali değişmez.
yeni[0] Iphone X verir

"""

# 10- yaslar en buyuk ve en kucuk elemanı ?
print(min(years))
print(max(years))

# 11- yaslar da kaç tane 1998 var ?
print(years.count(1998))

# 13- kullanıcıdan alacağın 3 tane marka bilgisini bir listede sakla

markalar = []

"""
- Aşağıdaki işlemi 3 kere tekrarlamamız gerekiyor onun yerine for a al
marka = input("Bir marka giriniz : ")
markalar.append(marka)
"""

marka1 = input("Bir marka giriniz : ")
markalar.append(marka1)

marka2 = input("Bir marka giriniz : ")
markalar.append(marka2)

marka3 = input("Bir marka giriniz : ")
markalar.append(marka3)

print(markalar)