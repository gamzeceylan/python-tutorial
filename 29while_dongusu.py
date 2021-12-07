# ------------------ while döngüsü ------------------
"""
- for bir liste üzerinde işlem yaparken while bir koşul oluşturur
- while true olduğu sürece çalışır

"""

i = 0
while i < 10:
    print(f"{i}. Merhaba")
    i += 1
# 0-9 arası 10 tane yazar


# aşağısı 1-20 arası tek sayıları yazdırır
i = 0
while i <= 20:
    if(i % 2 == 1):
        print("Tek sayı :", i)

    else:
        print("Çift sayı : ", i)

    i += 1

# tanımladığın bir değer boşsa '' false döner, içinde karakter varsa true döner
username = ''
print(bool(username))  # false döner

username = 'a'
print(bool(username))  # true döner


# aşağıdaki kod kullanıcı adı girilene kadar kullanıcı adını sorar
username = ''
while not username:
    username = input("Kullanici adiniz : ")

print("girdiniz kullanıcı adı :", username)

# --------------- örnek ------------------
# 3 sayilar listesini ekrana yazdır ############3


sayilar = [4, 6, 8, 3, 5, 63, 98, 3]

# 1. yol
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2. yol (ama tersten yazdırır)
while sayilar:
    print(sayilar.pop())

# 3. yol düzden yazdırır.
while sayilar:  # içi boşalana kadar true döner
    print(sayilar.pop(0))  # sürekli en baştakini siler

# kullanıcıdan alıdğın 5 sayıyı kullanıcıya göster
yeniSayilar = []
i = 0
while i < 5:
    sayi = int(input("Sayi giriniz : "))
    # yeniSayilar[i] = sayi hiç olur mu böyle?
    yeniSayilar.append(sayi)
    i += 1

print(yeniSayilar)


###### kullanıcıdan alacağın sınırsız ürünü liste içinde sakla ######
urunler = {}
urunSayisi = int(input("Kaç ürün gireceksiniz ? "))
i = 0
while i < urunSayisi:
    print(i, ". Urun Bilgisi")
    ID = i+1
    urunAd = input("Adi : ")
    fiyat = float(input("Fiyati : "))
    urunler.update({
        ID: {
                   "urunAdi": urunAd,
                   "fiyat": fiyat
                   }
    })
    i += 1

i = 0
while i < len(urunler):
    print(
        f"{i+1}. ürün : Adi {urunler[i+1]['urunAdi']}, Fiyat : {urunler[i+1]['fiyat']}")
    i += 1


# hocanın yaptığı : daha mantıklı. çünkü liste içine index ile ulaşabiliyorsun


tumUrunler = []  # liste içine dic oluşturcaz
i = 0
while i < urunSayisi:
    print(i, ". Urun Bilgisi")
    urunAd = input("Adi : ")
    fiyat = float(input("Fiyati : "))

    tumUrunler.append({  # [ {}, {}, {}] olarak saklanıcak
        "urunAdi": urunAd,
        "fiyat": fiyat
    })
    i += 1

for urun in tumUrunler:
    print(f"ürün adi : {urun['urunAdi']}, fiyati : {urun['fiyat']}")
