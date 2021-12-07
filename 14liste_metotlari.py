"""
-Python resmi sitesinde ve w3school da güzel döküman var hepsini oradan öğrenebilirsin

"""

sayilar = [1, -4, 5, 6, 8, 42, 4, 75, 5, 5]
harfler = ["a", "b", "r", "f", "k", "g"]

# --------------------------- min()----- max()--------------
# min() en kucuk değeri verir
# max() en buyuk degeri verir.
# harfler için de aynı seyi yaparsan alfabetik sıraya göre karsilastirma göre yapar.
# kelime olursa da kelimeleri alfabetik sıraya sokarak karsilastirir
enKucuk = min(sayilar)
enBuyuk = max(sayilar)
print(f"En kucuk : {enKucuk}, En buyuk : {enBuyuk}")

enKucuk = min(harfler)
enBuyuk = max(harfler)
print(f"En kucuk : {enKucuk}, En buyuk : {enBuyuk}")

# --------------- append() ----------------------
# append() listenin sonuna eleman ekler
sayilar.append(10)
print(sayilar)

# -------------- insert() ---------------------
# insert() belirtilen konuma eleman ekler. konum : index
sayilar.insert(3, 100)
print(sayilar)  # 3. indexe ekler diğerlerini kaydırır

# kendini -1 e ekler. -1 dekini sağa kaydırır. yani sonran bir önce
sayilar.insert(-1, 200)
print(sayilar)

# en sona eklemek istersen liste uzunluğunu alman gerekir. çünkü 10 elemanlı sonuncu index 9, sen 10. indexe koyarsan sona eklenmiş olur
sayilar.insert(len(sayilar), 1559)
print(sayilar)

# ----------------------- pop() ------------------------------
# pop() eleman siler. index verilmezse en sondan siler. index verilirse belirtilen yerden siler
sayilar.pop()
print(sayilar)

sayilar.pop(0)  # ilk elemanı sildik
print(sayilar)

# ----------------------- remove() -----------------------------
# remove() verilen DEĞERİ diler
# eğer deger yoksa hata alırsın o yüzden önce kontrol etmen gerek
sayilar.remove(42)
print(sayilar)

harfler.remove('a')
print(harfler)

# -------------------------- sort() -------------------------------
# sort() buyukten kucuge veya alfabeye göre sıralar

sayilar.sort()
print(sayilar)

harfler.sort()
print(harfler)

# ------------------------ reverse() ---------------------------------
# listeyi direkt ters çevirir. buyukten kucuğe sıra yapmak istiyorsan once sort() sonra reverse()

sayilar.reverse()
print(sayilar)

harfler.reverse()
print(harfler)

# -------------------- count() -------------------------------
# count() tekrarlanan eleman sayısını bulur.
print(sayilar.count(5))
print(harfler.count('a'))

# --------------------- index() ---------------------------------
# aranan elemanın index no sunu döndürür
# bulamazda hata verir
print(sayilar.index(5))  # tekrarlansa da ilk gördüğünün indexini döndürür


#----------------- clear() ---------------------------
#listeyi komple siler.
sayilar.clear()
print(sayilar) #silindiği için boş döner. [] döner














