a = 5
b = 10

c, d, e = 40, 45, 50  # böyle de atama yapılabilir

c, d = d, c  # c=d, d=c ataması

a += 5  # a = a+5
a -= 5  # a = a-5
a %= 5  # a = a%5

values = 1, 2, 3  # böyle tanımlarsan tuple tipi olur
print(type(values))

a, b, c = values
print(a, b, c)  # sırasıyla değer aktarılır. eğer biri eksik olursa hata alırsın

# a, b = values         hata
# a, b, c, d= values    hata

degerler = 1, 3, 4, 5, 6, 7, 8, 3, 2, 4
a, b, *c = degerler  # * operatörü kalan tüm değerleri buraya al demek
print(a, b, c)

a, *b, c = degerler #en sonu c ye an başı a ya ve kalan tüm değerleri b üzerine alır
print(a, b, c)
sonuc= b[0] + b[1] + b[5] #b artık list. elemanlarına index ile ulaşabiliriz
print(sonuc)
print(type(b))