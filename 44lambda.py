"""
- bazı hazır built-in fonksiyonlar vardır ve pratik işlem yaparken işimizi kolaylaştırır.
- uzun uzun fonksiyon yazıp işlem yaptırmak yerine hazır fonksiyonlarla yaptırabiliriz.

"""

# ---------------- lambda -----------------------------

# def le tanımlamak yerine lambda ile tanımlayabilirsin
# kare alma işlemini böyle fonk ile yapmak yerine direkt lambda anahtar sözcüğü ile yapabilirsin
# çoklu fonk kullanmak istediğinde aşağıdaki uzun yazım karışıklık yaratır
# lambda ile tek satırda fonk tanımlayabilir, işlem yapabilir ve sonucu geri döndürebilirsin


def multiply(a):
    return a**2


# lambda a: a**2 bu direkt a nın karesini
# (lambda a: a**2)(4)  bu direkt geriye 16 döner

# --- 1. kullanım
sonuc = (lambda a: a**2)(4)
print(sonuc)


# --- 2. kullanım
# kareAl tanımlayıp heryerde def gibi kullanabilirsin
kareAl = (lambda a: a**2)
sonuc2 = kareAl(5)
sonuc3 = kareAl(6)
print(sonuc2)


#---- Ornek
toplama = (lambda a, b, c: a+b+c)
sonuc4 = toplama(1, 2, 8)
print(sonuc4)


#--- Ornek
tersCevir = (lambda s: s[::-1])

sonuc = tersCevir("sadik")
print(sonuc)

sonuc = tersCevir(["sadik", "gamze"])
print(sonuc)

#---- Ornek


def myFunc(n):
    return lambda a: a*n


carp = myFunc(2)  # artık carp lambda ya esit
sonuc = carp(5)
sonuc = carp(10)
print(sonuc)
