# ----------------- enumerate() -------------------------
# aşağıdaki gibi indexi biz vererek yazdırıcaz. bunun yerine enumerate kullanabiliriz
markalar = ["opel", "bmw", "meercedes"]
index = 0
for marka in markalar:
    print(f"{index + 1} {markalar[index]}")
    index += 1


obj1 = enumerate(markalar)
# enumerate türünden. yazdırmak için list e dönüştürmelisin
listMarkalar = list(obj1)
# [(0, 'opel'), (1, 'bmw'), (2, 'meercedes')] otomatik bu yazılır. enumerate index ekler
print(listMarkalar)


# yukarıdaki for daha kolay şekilde :
for marka in listMarkalar:
    print(marka)
"""
ekrana :
(0, 'opel')
(1, 'bmw')
(2, 'meercedes')

"""

###
for index, value in listMarkalar:
    print(index, value)

"""
ekrana :
0 opel
1 bmw
2 meercedes

"""

# ama for zaten kendi list e dönüştürüyordu
for index, value in enumerate(markalar):
    print(index, value)

# istersen başlama sırasını da verebilirsin
for index, value in enumerate(markalar, 10):
    print(f"{index}-{value}")


# ----------------- zip() -------------------------
# iki liste karşılıklı index no larına göre birleşir. fazlalıklar gözardı edilir.
# listeler birebir eşleştirilir

liste1 = [1, 2, 3, 4, 5, 6]
liste2 = ['a', 'b', 'c', 'd']
sonuc = list(zip(liste1, liste2))
print(sonuc)
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] ekrana yazar

for item in zip(liste1, liste2):
    print(item)

# elemanları tek tek dolaşabiliriz.
for a, b in zip(liste1, liste2):
    print(a, b)


#####
liste3 = [100, 200, 300, 400, 500]
for a, b, c in zip(liste1, liste2, liste3):
    print(a, b, c)
