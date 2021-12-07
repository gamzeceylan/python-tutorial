"""
- class üzerinden çağırıyorsan method
- class üzerinden çağırmıyorsan fonksiyon.
- fonk ve method aynı işi yapar

- fonk def anahtar sozcuğu ile tanımlanır
- fonksiyon adları küçük harfle başlar genelde. çünkü
class adları buyuk yazılır karışmasın
"""
# ---------------- fonksiyon tanımlama ----------------------


def selamlama():
    print("Merhaba")


selamlama()

for i in range(5):
    selamlama()

# ---------------------- deger döndürme ---------------------
"""
-print python a özgüdür. örn sen html sayfasına bu fonksiyonu yollayacaksan
return ile ekna yazdırmak istediğin şeyi döndürürsün

"""


def toplamStr():
    return f"toplam{10+20}"


toplamStr()
print(toplamStr())


############


def toplam():
    return 10+20


sonuc = toplam() + 50  # toplam dan bir osnuc döner
print(toplam(), sonuc)


############

def yasHesapla():
    import datetime
    return datetime.datetime.now().year


sonuc = yasHesapla()
print(sonuc)


############


def selamla():
    import datetime
    saat = datetime.datetime.now().hour

    if saat < 12:
        return "Günaydın"

    else:
        return "iyi geceler"


selamla()

sonuc=selamla() + " Gamze" #string ifadeleri toplayabiliriz
print(sonuc)
