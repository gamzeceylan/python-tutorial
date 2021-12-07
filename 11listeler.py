"""
-Diğer programlama dillerindeki dizi karşılığı python da listedir
-string karakter dizisi gibi bir dizi tanımlayabiliriz
-msg[0][0] ilk [] msg nin 0. elemanı. ikinci [] msg nin 0. elemanının 0. elemanı
-dizi oluşturuken içine int, string, bool türü yazabilirsinçç hepsi aynı türden olmak zorunda değil
"""

msg = "Python Kursumuza Hoşgeldiniz. Ben Sadık Turan".split()

print(msg)
# ['Python', 'Kursumuza', 'Hoşgeldiniz.', 'Ben', 'Sadık', 'Turan'] yazar

print(msg[0])
# ekrana Python yazar

print(msg[0][0])
# ekrana P yazar. Python nun 0. indexi P dir

# print(msg[0][9]) taşma hatası


sayilar = [1, 4, 5, 9]
sonuc = sayilar
sonuc = sayilar[2]  # 5 yazar
# sonuc=sayilar[9] tasma hatası
print(sonuc)

# farklı türler aynı listede olabilir.
listeAli = ['ali', 20]
listeAhmet = ['ahmet', 22]

# liste içinde liste tanımlayabiliriz.
liste = [['ali', 20], ['ahmet', 22], ['gamze', 21]]
sonuc = liste[0]  # ['ali', 20] yazar
sonuc = liste[1][0]  # ahmet yazar
sonuc = liste[2][0][1]  # a yazar.
print(sonuc)


# ya da yukarıda tanımladığımız listeAli ve listeAhmet i liste içine alabiliz
ogrenciler = [listeAli, listeAhmet]
sonuc = ogrenciler  # [['ali', 20], ['ahmet', 22]] yazar
sonuc = ogrenciler[0]  # ['ali', 20] yazar
sonuc= ogrenciler[0][1] #yas bilgisini yazar
print(sonuc)
