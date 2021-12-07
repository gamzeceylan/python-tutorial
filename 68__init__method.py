"""
- class a özel metotalarımızı tanımlayabiliriz.
- ama class ların bazı özel methodları vardır. 
- def yazıp _ yazarsan bunları görürsün.
- __metod__ class lara özel metotlardır

"""
# -------- __init__ -----------------
"""
- init üretilen her instance için çalışan bir balangıç metodudur
- init mutlaka her sınıfa yazılır
- ve self parametresi alır. self üretilen nesneyi temsil eder.
- init, üretilen nesne kadar çalışır. içerideki değişkenleri de çağırdığında gelir
- init içinde obje attribute leri tanımlanır
"""

"""

class Product:
    def __init__(self):
        self.name = "Samsung  s10"
        self.price = 2000
        print("product nesnesi oluşturuldu")


p1 = Product()
p2 = Product()

# nesneleri çağırmasan, ekrana yazdırmasan bile "product nesnesi oluşturuldu" ekrana yazılır
# çünkü o her nesne üretildiğinde zaten direkt çalıştı.
# ve iki nesnenin ilk değerleri için de veri ataması Samsung s10 ve 2000 olarak yapıldı
print("hello")


"""


class Product:

    # init birden fazla parametre de alabilir
    # eğer init e parametre yazdıysan nesne oluşturduğunda o parametreleri bekler
    # self için parametre göndermiyorsun çünkü zaten self nesnenin kendisi
    # isActive e default değer atadık. onu artık yazmak zorunda değiliz. otomatik false atanır
    def __init__(self, name, price, isActive=False):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product nesnesi oluşturuldu")


p1 = Product("Samsung s10", 5000, True)
p2 = Product("Iphone 12", 12000)

print(p1.name, p1.price, p1.isActive)
print(p2.name, p2.price, p2.isActive)
