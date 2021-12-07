"""
-break döngüyü kırar
-continue bir defalık sonraki kod satırları çalıştırmaz sonra devam eder
- ctrl + c uygulamayı durdurur
"""

isim = "Gamze Ceylan"

# c yi yazar ve durur
for harf in isim:
    print(harf)
    if(harf == "C"):
        break

# m yi yazmaz
for harf in isim:

    if(harf == "m"):
        continue
    print(harf)


# 3 ü ve sonrakileri ekrana yazmaz
i = 0
while (i < 5):
    if(i == 3):
        break
    print(i)
    i += 1


# 3 te sonsuz döngüye girer. continue göründe altı çalıştırmaz hep if e girer
# i = 0
# while (i < 5):
#     if(i == 3):
#         continue
#     print(i)
#     i+=1

i = 0
while (i < 5):
    i += 1 # sonsuz dönmemesi için buraya yazmalısın
    if(i == 3):
        continue
    print(i)
