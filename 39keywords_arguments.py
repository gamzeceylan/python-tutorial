# parametreleri belirtip degerleri ona göre gönderebiliriz
# sıraları karıştırabilirsin o yüzden belirtip gönderbilirsin
def full_name(firsname, lastname):
    return f" your name is {firsname} {lastname}"


sonuc = full_name(lastname="Ceylan", firsname="Gamze")
print(sonuc)


# *args : istenilen sayıda parametre gönderilir
"""
-aşağıdaki yol bir çözüm olabilir anck her zaman değil...

liste = [10, 20, 30, 40]

def toplam(sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc += i
    return sonuc

# fonksiyona liste gönderebilirizi
print(toplam(liste))

"""


def toplam(*args):
   # print(type(args)) arg tuple tipinde bir liste.
  #  print(args)  verdiğimiz sayıları listeler
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc


# istediğin kadar parametre gönder. gönderdiğin parametreler listesi tuple
print(toplam(10, 13, 3, 56, 34, 78, 2))

"""
-aslında args özel bir isim değil sadece takma isimdir yerine m de yazabilirsin.
- *  değişken sayıda parametre göndericeğini söylersin ve tuple döner
- *args yazmadan yerine *h yazsan da aynı şey döner ve yine istediğin sayıda parametre yollayabilirsin

"""
