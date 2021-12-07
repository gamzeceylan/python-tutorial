# py de public private direkt olarak uygulanmaz sadece mantık üzerinden uygulanır. o da _ ile. private demek

# ------ 1. yol get ve set metotları ile -------

# get ve set propeert yazdığını gösterir
# _ sadece sınıf içinde erişilebilir olduğunu , dışarı kapalı olduğunu söyler
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get__price(self):
        return self._price

    def set__price(self, value):
        if value >= 0:
            self._price = value

        else:
            raise ValueError("Fiyat negatif olamaz")

"""
"""
- değşkenin başına koyulan _ mantığı biz bunu private değişken yaptık demektir. python da
özel bir public private yapısı yok. biz hala p1._price = -400 diyebiliriz ve hata almayız. 
ama _ mantığı bu değişkene böyle erişme demek. o yüzden get ve set metotlar üzerinden erişmeliyiz.

# p1 = Product("Telefon", 3750)

# p1._price=-4000 # yapılabilir ama böyle yapmamalısın

# p1.set__price(-900) # doğrusu böyle yapıp hata almaktır

# print(p1._price) # böyle ulaşabilirsin ama _ olduğu için yapmamayı tercih etmelisin

# print(p1.get__price()) # doğrusu böyle ulaşmaktır

"""

# ------ 2. yol @property ve @degisken.setter ile ----------
# @propert ve @degiske.setter attribute lerini eklersen artık bir fonksiyon değil direkt değişken üzerinden erişirsin
# @property get işlemi için yazılır


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value

        else:
            raise ValueError("Fiyat negatif olamaz")


p1 = Product("Telefon", 4000)

# dikkat et price üzerinden çağırıyorsun _price ya da price() değil
print(p1.getprice)


"""
# p1.price = -200 #hata aldık

# artık fiyata direk erişip güncelleme yapabiliyoruz
p1.price= 3500
print(p1.price)
"""
