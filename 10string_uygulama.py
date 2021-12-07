website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama"


# ------------- ' Hello World ' baş ve sondaki boşlukları sil
sonuc = ' Hello World '.strip()  # bas ve sondakileri sildi
sonuc = ' Hello World '.lstrip()  # soldan boşlukları sildi
sonuc = ' Hello World '.rstrip()  # sagdan boşlukları sildi
# soldan bu karakterleri siler. / yazarsın ama ikisini de siler
sonuc = website.lstrip('/:pthw')

print(sonuc)

# ------------------ wwww.sadikturan.com içindeki sadikturan bilgisini haricindekileri sil
sonuc = "wwww.sadikturan.com".strip('w.com')
print(sonuc)

# ------------- kursAdi tüm karakterleri küçük harf yap
sonuc = kursAdi.lower()
print(sonuc)

# ------------------- website içinde kaç a var?
# count() kullanıcıdan mail istediğmizde @ var mı dite kontrol etmek için kullanılabilir
sonuc = website.count("a")
sonuc = website.count("www")  # www  var mı
# www ara ama 9. ve 15. index arasında ara.
sonuc = website.count('www', 9, 15)
print(sonuc)

# --------------------- website içinde www ile başlayıp com ile bitiyor mu?
sonuc1 = website.startswith("www")
sonuc2 = website.endswith("com")
print(sonuc1, sonuc2)

# ------------------------- website içinde .com ifadesi var mı
# find() ve index() arar ve bize hangi indexten başladığını döndürür. ama index bulamazsa hata verir find -1 döndürür.

sonuc = website.index('.com')
sonuc = website.find('.com', 0, 10)  # 0 la 10 arasında var mı

# default olarak aramaya soldan başlar ve ilk gördüğünü döndürür
sonuc = kursAdi.find('Python')
sonuc = kursAdi.rfind('Python')  # şimdi aramaya sağdan başlar
print(sonuc)

# -----------------kursAdi içinde karakterlerin hepsi alfabetik mi? isalpha, isdigit
sonuc1 = kursAdi.isalpha()
sonuc2 = kursAdi.isdigit()  # false gelir
sonuc = '123'.isdigit()  # true gelir
print(sonuc1, sonuc2)

# --------------- contents idafesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekle
# toplam karakter ayırır. contentsi ortaya kolay kalan yerleri * la doldurur.sağda ve solda 21 * olur
sonuc = 'Contents'.center(50, '*')
print(sonuc)

# ---------------- kursAdi boşlukları - ile değiştir.
sonuc = kursAdi.replace(' ', '-')
print(sonuc)

# ---------------- 'Hello World' içinde world ifadesini There olarak değiştir
s = 'Hello World'
sonuc = s.replace('World', 'There')
print(sonuc)

# --------------------------- kursadi karakter dizisini boşluk karakterlerinden ayır
# bosluklardan bol. bolmezsen her harfi dizeye ayrı ayrı aktarırı. böylede kelimeleri diziye alır
kursAdi = kursAdi.replace(':', '')  # : sildi
sonuc = kursAdi.split() #bosluklardan ayırdı bir siziye attı
birlestirme = ''.join(sonuc)
print(birlestirme)
