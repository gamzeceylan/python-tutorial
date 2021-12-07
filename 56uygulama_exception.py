# 1- faktoriyel fonksiyonu oluşturup fonksiyona gelen deger için hata mesajları verin

def faktoriyel(x):

    sonuc = 1
    x = int(x)

    if x < 0:
        raise ValueError("0 dan büyük olmalıdır")

    elif x == 0:
        return 1

    for i in range(1, x+1):
        sonuc = i*sonuc

    return sonuc


for i in [5, 7, 'a', 2, -4, '10a']:
    try:
        x = faktoriyel(i)

    except ValueError as ex:
        print(ex)
        continue

    else:
        print(x)

"""
NOT : Uygulama expect yani hata bloğuna girdikten sonra o bloğu çalıştırıp durur.
bunun olamaması, hesaplamanın devam etmesi için continue yazmalısın

"""

# 2- girilen parola içinde türkçe karakter hatası veriniz


def paraloKontrol(parola):
    # turkce_Karakterler = ["ç", "ğ", "ö", "ş", "ü"]
    turkce_Karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_Karakterler:
            raise TypeError("paralo turkçe karakter iceremez")

    print("geçerli parola")


parola = input("parola giriniz : ")

try:
    paraloKontrol(parola)

except TypeError as ex:
    print(ex)
