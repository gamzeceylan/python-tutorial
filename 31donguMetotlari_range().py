"""
-for da dönmek için bir liste gerek
- eger elimizde bir liste yoksa ve for da dönmek isyiorsan listeti sıralı şekilde while ile oluşturmak yerine
range() ile oluşturabiliriz
- range 0 dan başlar verdiğimiz sona kadar sıra oluşturur. sonra da onu listeye çevirebiliriz.
- for döngülerinde kullanırken listeye çevirmene gerek yok. for kendiğinden çevirir
"""

r = range(10)  # 0 dan 10 a kadar oluşturucak. 10 dahil değil
sonuc = list(r)
print(sonuc)


r = range(5, 10)  # 5 ten 10 a kadar oluşturur10 dahil değil
sonuc = list(r)
print(sonuc)

r = range(50, 100, 10)  # 50 den başlar 100 e kadar 10 ar artarak gider
sonuc = list(r)
print(sonuc)

# adım sayısını -1 dersen tersten yazdırır. -10 dersen 10 azalarak yazdırır
# tabi unutma alt sınır dahil üst sınır dahil değil. 100 dahil 50 değil
r = range(100, 50, -10)
sonuc = list(r)
print(sonuc)


# 0-9 arası
for i in range(10):
    print(i, ". merhaba")

# 7-9
for i in range(7, 10):
    print(i, ". merhaba")


# 100- 200 arasındaki çift sayılar ?
for i in range(100, 200):
    if(i % 2 == 0):
        print(i)
