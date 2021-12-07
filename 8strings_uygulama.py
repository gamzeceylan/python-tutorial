"""
-string ifadelerce * operatörü yanyaa tekrarkalamayı sağlar

"""

website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama"

# 1- kursAdi karakter dizisindeki karakter sayisi
sonuc = len(kursAdi)
print("kursAdi karakter sayisi : ", sonuc)

# 2- website içinde www karakterlerini aratın
print(website[7:10])

# 3- website içinden com karakterlerini aratın
print(website[-3:])

# 4- kursadi içinden ilk 15 ve son 15 karakterlerini alın
print(kursAdi[0:15])
print(kursAdi[-15:])

# 5- kursAdi ni tersten yazdırın
# :: yazdığında tümünü almış olursun. -1 yazarsan ters çevrilir
print(kursAdi[::-1])

# 7- 'Hello world' içindeki w yi W ile dğeiştir
s = 'Hello world'
# s[6]='W' hata verir str dizilerinde tek karakter ataması yapamazsın
s = s[0:6] + 'W' + s[-4:]
print(s)

# 8- abc ifadesini yan yana 3 defa yazdır.
print('abc '*3)

name, surname, age, job = 'Gamze', 'Ceylan', 21, 'Öğrenci'
# 9- yukaridaki değişkenleri Benim adım ...., yaşım ..., mesleğim... diye yazdır
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")
print("Benim adım {} {} yaşım {} mesleğim {}".format(name, surname, age, job))
