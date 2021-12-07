# ---------- Çarpım tablosu -------------------
import random
for i in range(1, 10):
    print("***************")
    for j in range(1, 10):
        print("{}x{}={}".format(i, j, i*j))


# girilen sayının asal olup olmadığını kontorl et

sayi = int(input("Bir sayi giriniz : "))
asalmi = True

if(sayi == 1):
    asalmi = False

for i in range(2, sayi):
    if(sayi % i == 0):
        asalmi = False
        break

if(asalmi == True):
    print("sayi asaldır.")
else:
    print("Sayi asal değildir")


# ---------------- sayi tahmin oyunu --------------------

randomSayi = random.randint(1, 100)
print(randomSayi)

can= int(input("Kaç hak kullanmak istersiniz ? "))
sayac = 0
puan = 100
while can > 0:
    can-= 1
    sayac += 1
    tahminSayi = int(input("tahmin : "))

    if tahminSayi == randomSayi:
        print("Doğru cevap ! {}. defada bildiniz Puanınız : {}".format(sayac, 100-(sayac-1)*20))
        break

    elif tahminSayi > randomSayi:
        print("aşağı")

    else:
        print("yukarı")

    if can == 0:
        print("hakkınız bitti. tutulan sayı {}".format(randomSayi))
