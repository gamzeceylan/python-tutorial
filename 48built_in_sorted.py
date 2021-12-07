# --------------- sorted() -------------
# sort() listeyi sıralama işlemlerinde kullanılırdı ama sadece list ler sıralanırdı. dic sıralarken sort kullanılamazdı.
# sorted() dic sıralarken de kullanılabilir

"""
-sayilar sıralanmış oldu sort() ile

sayilar = [1, 4, 9, 2, 5, 65, 21]
sayilar.sort()
print(sayilar)

"""

# - 1
sayilar = [1, 4, 9, 2, 5, 65, 21]
sonuc = sorted(sayilar)  # sorted içine yazılır dikkat et.
print(sonuc)

# - 2
# reverse nasıl sıralamk isteidiğinle alakalı.
# reverse = True büyüktne küçüğe doğru  sıralar.
# reverse = False küçükten büyüğe sıralar. defult olan budur
sonuc = sorted(sayilar, reverse=True)
print(sonuc)

# - 3
# tuple listesi üzerinde bir değişiklik yapamıyorduk ama sorted metodu ile tuple üzerinde sırama yapabiliriz
# tuple sorted içine atıldıktan sonra liste tiğine döner
rakamlar = (1, 6, 3, 7, 9, 2, 5, 2)
sonuc = sorted(rakamlar)
print(sonuc)
print(type(sonuc))

# - 4
users = [
    {"username": "sadikturan", "tweets": [
        "tweet 1", "tweet 2"], "email":"sdk@gmail.com"},
    {"username": "gmzceylan", "tweets": []},
    {"username": "zynpsanver", "tweets": [
        "tweet 1"], "name":"", "phone":"1213324"}
]

# yukarıdaki her dic i KEY e göre sıralayabiliriz. KEY sıralama kriterini belirtiyor
sonuc = sorted(users, key=len)  # en az key olandan en çok key olana
print(sonuc)

# en çok key olandan en az key olana
sonuc = sorted(users, key=len, reverse=True)
print(sonuc)

# istediğimiz veriye göre de sıralayabiliriz.
# username ye göre alfabetik sıraladı
sonuc = sorted(users, key=lambda user: user["username"])
print(sonuc)

# ya da tweet sayılarına göre sılayabiliriz
sonuc = sorted(users, key=lambda user: len(user["tweets"]))
print(sonuc)

# - 5
kurslar = [
    {"title": "python kursu", "students": 2500},
    {"title": "web geliştirme kursu", "students": 35000},
    {"title": "javascript kursu", "students": 5000}
]

# hangi kursa en az öğrencisi olandan en fazla öğrencisi olana
sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])
print(sonuc)

# en popüler kurslar
sonuc = sorted(kurslar, key=lambda kurs: kurs["students"], reverse=True)
print(sonuc)

# en kuraların öğrenci sayıları
sonuc = map(lambda kurs: kurs["title"], sorted(
    kurslar, key=lambda kurs: kurs["students"], reverse=True))
print(list(sonuc))
