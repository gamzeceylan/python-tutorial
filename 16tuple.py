"""
-tuple bir colleciton dur.
- type = tuple
- içine booli str, int yani object türünde karışık tanımlama yapabilirsin
-listleer gibi sıralanabilir. listelerden farkı oluşturduğun değerleri bir daha değiştiremiyorsun.
-güvenli bir kod yazmak için kullanılır ve daha az yer kalplar çünkü değiştirilemez
- elemanlara indexlerle ulaşırsın
- . ya bastıktan sonra kullanabileceğin metotlar karşına gelir
- örn bir veritabanındaki listeleri göstermek isiyorsun o zaman tuple kullanabilirsin
- vt de ki bilgileri tuple içine alır ve gösterirsin
-amacın değişiklik yapmak değil sadece listelemek ise list de kulanabilirsin ama tuple uygulamayı
daha performanslı hale getirir
-üzerine eleman eklemek, eleman silmek gibi işlemleri yapaazsın
- tanımlama yaparken () kullansan da olur kullanmasan da ama daha anlaşılabilir olması için () kullanabilirsin
"""
_list = [1, 2, 3]
_tuple = (1, 2, 3, True)

_tuple2 = ('Gamze', 21, True)

print(type(_tuple))

print(_tuple[0])

# _tuple[0]=5 hata verir. kabul etmez
print(_tuple[0])

print(_tuple.count(1))
# true da 1 sayılır.

print(_tuple + _tuple2)

# varolan listeyi tuple ya çevirebiliriz
_t = tuple([3, 4, 5])

_l = [3, 4, 5, 67]

print(tuple(_l))
