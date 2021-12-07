"""
-str ifadede uzun uzun + yazarak birbirine ekleme çok karmaşıklığa neden olur..
-onun yerine format yapısını kullan
-sırasıyla format() içine yazdığın {} yerine gelir
- index numarası belirtmezsen sırasıyla yazılır ama index de belirtebilirsin.
- format içine yazdıkların 0, 1, 2 siye gider
- ctrl + k + c yorum satırı
- ctrl + k + u yorum satırı kalkar
- f string 

"""

name = "Gamze"
surname = "Ceylan"
age = 21
gender = "K"

# 1. kulllanım
print("Adım : {} Soyadım : {} Yaşım : {}".format(name, surname, age))

# 2. kullanım
print("Adım : {2} Soyadım : {1} Yaşım : {0}".format(name, surname, age))

# 3. kullanım
print("Adım : {a} Soyadım : {s} Yaşım : {y}".format(a=name, s=surname, y=age))

print("Adım : {0} Soyadım : {1} Adım : {0}".format(name, surname))


number = 200/7
# n:1.5   : ilk kısım kaç boşluk bıkakılacağını belirler. ikinci kısım sayının tam kısmı dahil kaç basamak alınacağını
# number = round(200/7,3)   yazsaydın da virgülden sonra 3 basamak alırdı
print("the resutl is {n:1.5}".format(n=number))

# f string. f"" ile oluşturulur. {} içine direkt parametre verebilirsin. 
print(f"Benim adım : {name}, Soyadım : {surname}")
