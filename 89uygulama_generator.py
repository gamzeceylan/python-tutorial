# (1-sonsuz) aralığında her sayısının karesini getiren fonksiyon yazın
# fibonacci serisini hem normal fonk hem de generator fonk ile oluştur
# performans testleri yapın

# -------- 1 --------------
# normal fonksiyon ile yaparsan hata alırsın. generator ile yapmalısın
# yield la sanırım return kullanamıyoruz ve yield yanında yazan değişken bize dönüyor

def kareAl():
    sayi = 1
    while True:
        yield sayi
        sayi += 1


sonuc = kareAl()
# next ile çağırdığında sırasıyla çağırır
print(next(sonuc))
print(next(sonuc))
print(next(sonuc))

"""
- for sonsuza kadar yazar

for i in sonuc:
    print(i)

"""

# ------------ 2 ---------------
"""
- normal fonksiyonla yaptığın zaman sayiları bir liste içinde tuttuktan sonra listeyi yazdırdığın
için verdiğin değer büyüdükçe işlemci zorlanıcak ve ram bir süre sonra dolucak hata vericek.
- hatta bazı programla çalışmayı durdurur

def fib_list(max):
    sayilar = []

    a, b = 0, 1
    while len(sayilar) < max:
        sayilar.append(b)
        a, b = b, a+b

    return sayilar

print(fib_list(10000))

"""

"""
-ama bunu generator ile yaptığında ramde hiçbir zorlanma olmaz ve istediğin kadar yazdırabilirsin. çünkü zaten üretilen sayı göstetiliyor

def fib_gen(max):
    a, b = 1, 0
    count = 0
    while count < max:
        a, b = b, a+b
        yield b  # yield : generator olarak return ettiğin
        count += 1


for i in fib_gen(100):  #istediğin kadar çalıştır
    print(i)


"""


