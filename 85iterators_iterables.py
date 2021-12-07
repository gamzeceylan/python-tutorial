# --------------- iterable obje ----------------
# nesne olarak kullanılabilen bir nesneye iterable obje denir.
# temel olarak nesnedeli dizinin gezinilebileceği ve ilerenebileceği anlamına gelir.
# list, dict, set(kümeler), range gibi koleksiyonlar iterable dır.

# --------------- iterable ? (yinelenebilir) -----------------------
# biz aslında farkında olmadan for ile listeler üzerinde dolaşırken bu özelliği kullanıyoruz.

liste = [34, 6, 3, 90, 43]

# a=10 for i in a: diyip bir işlem yapamazdık. çünkü a bir iterable değildir
# print(dir(liste)) ile list içindeki __iter__ fonk görebilirsin.
# ama print(dir(a)) ile baktığında __iter__ i göremezsin
for i in liste:
    print(i)


# --------------- iterator ? (yineleyici) -------------------
# iterable obje nin üzerinde tek tek gezebilmek için objeyi iterator objesine çevirmemiz gerekir.
# for bu işi bizim için yapıyor. iteroter obje üzerinden de elemanlarda dolaşılıyor

"""
# print(nex(liste)) ile elemanlar üzerinde gezmek istediğinde iterator hatasını alırsın. next, for gibi
nesneyi iterable obje ye çevirmez. kendin iter metoru aracılığıyla önce liste yi iterable yapmalısın
sonra next i kullanmalısın
# next metodu da elemanları tek tek yazar. her next de bir adım gider

"""

print("karışmasın diye".center(50, "*"))

# print(next(liste)) # TypeError: 'list' object is not an iterator hatası

iterable = iter(liste)

# <list_iterator object at 0x0000028685863FD0> döner. iterable çevrildi
print(iterable)

"""
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
# print(next(iterable)) next nerde durucağını bilemez o yüzden try cath ile kocls
# ntrol etmeisin. StopIteration hatası

"""

print("karışmasın diye".center(50, "*"))

while True:
    try:
        print(next(iterable))

    except StopIteration:
        break


# iterator ve iterable ı neden bilmeliyiz ? kendi tanımladığımız tiplerde de bu kavramları uygulamamız gerekir

"""
NOT : iter() fonksioynunu kullanıp nesneyi iterable nesne yapmak için nesnenin iterator özelliğinin olması gerekir.
eğer nesnenin iterator özelliği yoksa iter() kullanamazsın. iter() den nce iterator özelliği kazandırmalısın.
iterator özelliği kazandıran da __iter__() metodudur

- next metodunu çağırdığın zamanda arka tarafta sınıfın __next__ metodu çalışır

"""