pi = 3.14
# veri kaybı olmaması için float yazdık. int yazsaydık ondalık kısmı atardı
r = float(input("Yaricapi Giriniz : "))
area = pi*(r**2)
circumference = 2*pi*r
# print içine + yazarsan toplama yapmaya çalışır. , ile yazman gerek
# str bir işlem ile str bir işlem birleştirilebilir. ,yerine + yazarsan hata alırsın
print("Alan : ", area)
print("Cevre :  ", circumference)

# 2. yazım
result = "Alan : " + str(area) + " " + "Cevre : " + str(circumference) #str ye donusturup + yazabilirsin
print(result)

road = input("Gidilen yolu km cinsinden giriniz : ")
mil = float(road) / 1.609344
mesafemil= round(mil,3)
print("Gidilen yol mil cinsinden : ", mesafemil)

"""
 round() yuvarlama fonksiyonudur. round(a, 3) örneğin içine vfloat a değerini göderirsen
virgülden sonra sadece 3 basamak yazdırır.
"""
