# kanpırhenşın
"""
-uzun uzun yazmak yerine : 

sayilar1 = []
for i in range(10):
    sayilar1.append(i)

-bunu kısaca şöyşe yazabilirsin : 

sayilar2 = [i for i in range(10)]

-[expression for item in list] 

ile kolayca liste oluşturabilirsin.

-expression : yapmak istediğin işlem. örn : 
sayilar = [i*i for i in range(10)]
yukarıdaki işlem 0,...,9 arası oluşturduğu liste elemanlarını i üzerine alıyor sonra
i nin karesini alıp sayılar dizisine ekliyor


"""
sayilar1 = []
for i in range(10):
    sayilar1.append(i)

print(sayilar1)


sayilar2 = [i for i in range(10)]
print(sayilar2)


# karesini alıp sayilar3 içine ekliyoruz
sayilar3 = [i**2 for i in range(10)]
print(sayilar3)


# liste içindeki elemanlar üzerinde işlem yapıp yeni listeye atmak
liste = [10, 4, 3, 8, 9, 12]

sayilar4 = [i*2 for i in liste]  # 2 katını alıp sayilar4 içine ekledik
print(sayilar4)


# string üzerinde işlem yapmak
# hepsi büyük harfe dönüşüp sonuc içine eklendi
isim = "gamze"
sonuc = [c.upper() for c in isim]
print(sonuc)

# hepsi küçük harf olup yeni listeye eklendi
isimler = ["aHmet", "çıNar", "GamzE", "meliH"]
yeniIsimler = [isim.lower() for isim in isimler]
print(yeniIsimler)
