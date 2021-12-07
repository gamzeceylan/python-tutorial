msg = "Python kursumuza hoş geldiniz. Ben Sadık Turan"

sonuc = msg.upper()
sonuc = msg.lower()
sonuc = msg.title()
sonuc = msg.capitalize()
print(sonuc)

sonuc = "abc".islower()  # true ya da false döner
sonuc = "abc".isnumeric()
# stript başındaki ve sonundaki boşluk karakterini keser
sonuc = "     abc      ".strip()
print(sonuc)

sonuc = msg.split()  # string ifadeyi boşluklardan böler ve diziye atar
print(sonuc)
print(sonuc[1])  # 'kursumuza' ulaşırsın

sonuc = msg.split('.')  # noktalardan ayırır.
print(sonuc)

sonuc = msg.split()  # bosluklardan bolduk
birlestirme = '--'.join(sonuc)  # birleştirir ve araya -- atar
print(birlestirme)


# içerideki değerin kaçıncı indexten başladığını döndürür
indexNo = msg.index('hoş')
print(indexNo)

baslama = msg.startswith("A")  # A ile mi başlıyor?
bitme = msg.endswith("n")  # n ile mi bitiyor
print(baslama)  # False döner
print(bitme)


# Sadık ı bulup Gamze ile ile değiştirir. eğer bir şey bulamazsa hata vermez false de dönmez
sonuc = msg.replace('Sadık', 'Gamze')
print(sonuc)

sonuc = msg.replace(' ', '-')  # boşlukları - ile değiştirdik
print(sonuc)

# coklu kullanım
sonuc = msg.lower().replace(' ', '-').replace('ş', 's').replace('.', ' ')
print(sonuc)
