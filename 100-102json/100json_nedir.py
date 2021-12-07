"""
- jason 
- db den veri istiyoruz db de servis aracılığıyla verileri bize getiriyor. service nin ne olduğu 
önemli değil.- sonra bu verilerri sevice den alıyoruz json veri türünde kullanııya gösteriyoruz.
mobil de veya web de. json veri türüne alternatif xml de vardır. yani json ve xml uygulamalar arasında
veri alışverişini sağlar.
- uygulama dili ce farketmez önemli olan json şeklinde verileri almak ve işlemek
- json veriyi {} arasına oluşturuyoruz. temelde dic yapısındadır

"""


"""
-Normal dosya okuma da dosya str olarak okunur. eğer json kütüphanesini import edersen
artık dosya dict yapısında döner

with open("person.json") as file:
               data=file.read()


print(data)
print(type(data)) # data tipi str dir
# print(data["firstName"]) # string üzerinden bu şekilde indexleyemezsin. dic olsaydı yapabilirdin

# str olan dosyaı dic e çevirip kullanman lazım. yukarıdaki gibi indexleyebilmen için

"""
# ------- deserialize ------------
# json veri türünü uygulamaya getirdiğinde yani python tarafına getirdiğinde dict veri yapısına getirmek
# okuduğun verileri bir obje karşılığa çevirmek


import json
with open("person.json", encoding="utf-8") as file:
    data = json.load(file)


print(data)  # dict yapısında gelir
print(type(data))  # data tipi dict dir
print(data["firstName"])  # dict olduğu için artık indexleyebilirsin
print(data["hobbies"][0])

# json bir başka uygulama tarafından, service üzerinden gelebilir. şuan kendi oluşturduğumuz dosyayı okuyoruz


# ----  biz json oluşturmak istersek -----
# kullanıcıdan aldığın bilgileri json türüne çevirmek istersen
# aslında uygulama tarafından bakınca string bir bilgidir
#--- json- string---
data = """
{
               "firstName":"Sadık",
               "lastName":"Turan",
               "hobbies":["spor","sinema"],
               "age":37,
               "children":[
                              {
                                             "firstName":"Çınar",
                                             "age":3
                              }
               ]
}

"""

print(type(data)) # data str dir 

# eğer json formatına diekt çevirmek istiyorsan içericeki bilginin json formatına uyması gerekir
# çevrilemezse hata verir
# loads metodu kullanılır. 
# loadc dict türüne çevirir
jsonData = json.loads(data)

# load ı json dosyayı uygulamaya dict olarak çekiyorsak ve okumak isiyorsak
# uygulama tarafında bilgi json str şeklinde varsa okumak için loads kullanılır

print(jsonData["firstName"])
print(jsonData["hobbies"][0])
