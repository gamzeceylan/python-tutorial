"""
- Eğer fonksiyonun istediği parametreyi göndermezsek fonksiyon hata verir
- ama göndermek de istemiyorsak o parametreye default değer atamalıyız.
- oraya dışarıdan değer göndermediğimiz sürece default değerde çalışır

NOT : default parametre her zaman en sonra tanımlanır. def usAlma(taban=2,us) bu hata verir
çünkü 3 alsa dışardan tabana mı gidicek usse mi kafa kafası karıştı adamın
yani default parametre aldığında ondan sonraki değişkenler de default parametre almalı
"""


def selamlama(isim, mesaj="iyi Günler"):
    print(f"{mesaj} {isim}")


selamlama("Ali", "Selam")
selamlama("Mert")


def usAlma(taban, us=2):
    return taban**us


print(usAlma(5))
print(usAlma(2, 3))


# bir fonksiyona fonksiyon da gönderebilirizi.

def toplam(a, b):
    return a+b


def islem(a, b):
    return toplam(a, b)


sonuc = islem(7, 10)
print(sonuc)

####

"""
def islem(a, b, fn):
    return fn(a, b)
"""

# default değer de yollayabiliriz
def islem(a, b, fn=toplam):
    return fn(a, b)


sonuc = islem(5, 10, toplam)
# toplam fonksiyonunu gönderirken fonksiyonun referansını gönderdiğimiz için () bunu yazmamalıyız

print(sonuc)
