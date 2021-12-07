# -------------- filter() ---------------

# map() tüm elemanlar üzerinde işlem yapıyordu.
# filter seçtiği elemanlar üzerinde işlem yapıcak
# yine bunu da list e çevirmen gerek

yaslar = [4, 15, 67, 19, 22, 13]

# -- uzun yol


def yetiskinmi(x):
    if x < 18:
        return False
    else:
        return True


sonuc = [x for x in yaslar if x > 18]
print(sonuc)


# --- filter ile
sonuc = list(filter(yetiskinmi, yaslar))
print(sonuc)


# --- lambda and filter
# lambda ya yandan parametre geliyo
sonuc = list(filter(lambda x: x > 18, yaslar))
print(sonuc)

# - 1
sayilar = [0, 1, 35, 6, 79, 17]
sonuc = list(filter(lambda x: x % 2 == 0, sayilar))
print(sonuc)

# - 2
isimler = ["ali", "gamze", "furkan", "ahmet", "ayşe"]
sonuc = list(filter(lambda x: x[0] == "a", isimler))
print(sonuc)

# - 3
# bir değişiklik yapmak istiyorsan : map
sonuc = list(map(lambda x: x.upper(), isimler))
print(sonuc)

# - 4
# a ile başlayanları bulup hepsini buyuk harf yap.
# zaten filter sana seçtiğin elemanları döndürücek onları da tek tek map ile değiştiriceksin.
# yukarıdaki filter ile birleştirdik
# map in 2. parametresi filtrelenmiş veirler olabilir
sonuc = list(map(lambda x: x.upper(), filter(lambda x: x[0] == "a", isimler)))
print(sonuc)

# yukarıdakinin biraz daha sade hali
filtredResult = filter(lambda x: x[0] == "a", isimler)
sonuc = list(map(lambda x: x.upper(), filtredResult))
print(sonuc)


# - 5
users = [
    {"username": "sadikturan", "tweets": ["tweet 1", "tweet 2"]},
    {"username": "gmzceylan", "tweets": []},
    {"username": "zynpsanver", "tweets": ["tweet 1"]}
]

# tweet atnaları döndürdük
sonuc = list(filter(lambda x: len(x["tweets"]) > 0, users))
print(sonuc)

# tweet atanların usernae sini döndür
filtrelenmisVeri = list(filter(lambda x: len(x["tweets"]) > 0, users))
sonuc = list(map(lambda x: x["username"], filtrelenmisVeri))
print(sonuc)

# aynı seyleri list comprehension ile de yapabiliriz
sonuc = [user["username"].upper() for user in users if len(user["tweets"]) > 0]
print(sonuc)
