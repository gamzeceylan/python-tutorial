"""
- len() karakter sayısını döndürür
- dizi[x:y] x. indexten başlar y. indexe kadar alır. y dahil değil. y-x karakter döndürür 
"""

name = 'Gamze'
gender = 'K'
age = '21'
msj = "Benim adim : " + name + " ve Yaşım : " + age

karakterSayisi = len(msj)

print(msj[0])  # B gelir
print(msj[1])  # e gelir
print(msj[2])  # n gelir
# print(len(msj)) #karakter sayisini döndürür

# eğer burda msj[karakterSayisi] yazarsan taşma hatası alırsın
print(msj[karakterSayisi-1])

# 1. indexten başlar 7. indexe kadar alır 7 yi almaz
# ilk 5 i almak istiyorsan msj[:5] yazmalısın. başlangıç belirtmezsen 0. indexten başlar
print(msj[1:7])
print(msj[:5])
print(msj[:-1])  # komple alır
print(msj[10:])  # 10. indexten en sona kadar alır

# geriden doğru -1 di o zaman -10 dan en sona kadar alır (en son dahil değil)
print(msj[-10:-1])

print(msj[:500])  # hata vermez

# print(msj[50]) hata verir

# 0 ı alır. sonraki 2ye atlayıp 3 ü alır. sonraki 2ye atlar 5 i alır
print(msj[0:10:2])

print(msj[:]) #bütün karakterleri alır çünkü başı ve sonu belli değil
print(msj[::1]) #:: adım sayısı. 1 olduğu için hepsini alır.
print(msj[::2]) #2 atlayarak alır
print(msj[::-2]) # en sağdan başlar, sola doğru 2 adım atlayarak alır

print(msj[::-1]) #yazdırmaya en sonran başlar ve 1 adım gittiği için tersten yazdırır