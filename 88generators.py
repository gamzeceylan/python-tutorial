# -------  generator -----
# generator, iterable bir nesne oluşturan fonksiyondur

"""
- küçük veriler döndürdüğümüzde böyle bir fonksiyon işimizi görebilir ama 
büyük dosyalar okuyacağımız zaman örn 500 binlik direkt okuduğumuz nesneyi 
yazdırabilmeliyiz. eger böyle bir liste içinde alır sonra okursak bellekte boş
yere yer kaplamış oluruz. işle bunu generator aracılığıyla yapıcaz.
 
- yield anahtar sozcugu bize bir generator objesi oluşturur.
- yield de iterator da olduğu gibi next metoduyla kullanılır. 
NOT : next ile bir önceki veriye erişemezsin. okuduğunu ekrana yazar ve dıradaki 
veriye odaklanırsın. böylelikle bellekte yer kaplamazsın ve uygulaman çok daha 
performanslı çalışır   

def sayi_say(max):
    sayilar = []
    sayi = 1
    while sayi <= max:
        sayilar.append(sayi)
        sayi += 1
    return sayilar


sonuc = sayi_say(10)
print(sonuc)


"""
# generator nesnesi __iter__ ve __next__ özelliklerine sahiptir.
# print(help(sonuc)) ile bu özelliklere bakabilirsin
# class ta elemanlar üzerinde tek tek dolaşabilelim diye iter ve next nesnesini oluşturuyorduk
# ancak bunlar generator un kendisinde olduğu için oluşturmana gerek yok. iter nesnesi kendiliğinden oluşur
# generator nesnesi bir iterator dur


def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi += 1


sonuc = sayi_say(5)  # sonuc bir generator objesidir
"""
-- next ile eknana yazdırma

print(next(sonuc))
print(next(sonuc))
print(next(sonuc))
print(next(sonuc))
print(next(sonuc))

"""
# next bellek üzerinde yer kaplamaz

# next generator un kendisinde olduğu için direkt for la da yazdırabilirsin

"""
- for ile ekrana yazdırma

print(next(sonuc))

for i in sonuc:
               print(i)

"""

"""
- list e çevirip ekrana yazdırma
- ama yine bellekte bir liste tutuyorsun

sonuc=list(sonuc)
print(sonuc) # hepsini yazar

"""

"""
- büyük verilerle çalıştığında verilerin hepsini belleğe atıp sırayla göstermek uygulama performansını düşürür.
bunun yerine veriyi alırsın gösterirsin silersin ve diğerine geçersin. tercih edilen budur

"""


"""
- döngü kullanmadan generator oluşturma
- liste oluştururken [ ] kullanırdın. generator oluştururken de ( ) kullanman gerekiyor. ekstra bir çevirme yapamana gerek yok

generator = (i for i in range(1, 11))

print(next(generator))
print(next(generator))
print(next(generator))

print(type(generator))

"""

generator = (i for i in range(1, 11))

print(next(generator))
print(next(generator))
print(next(generator))

print(type(generator))
