"""
lst = [1, 2, 3]

result = type(lst)  # lst, bir list class ından türetilmiş olan instance.
print(result)


- bir liste tanımladağımızda list class ının bir kopyasını oluştururz
- yani list class ı daha önce oluşturulmuş, bazı metotlar içine aktarılmış
- biz de list class ından bir instance üreterek o sınıfın özelliklerine erişebiliyoruz
- . diyip metotlara ulaşabiliriz.
- class tan türettiklerimiz bir object veya instance dir

- class adları büyü harfle baslar
- method : class fonksiyonları
- arrtibute : class değişkeni
"""


class Ogrenci:
    # method
    # attribute
    pass


ogr1 = Ogrenci()  # ornekledik
ogr2 = Ogrenci()


print(type(ogr1))  # ogr tipi Ogrenci dir
print(ogr1)  # ogr ram üzerinde tutulan bir adreste object e karşılık geldiğini görürüz
print(ogr1, ogr2)  # ogr1 ve ogr2 belleğin farklı yerlerie tutulan iki nesnedir


class Urun:
    pass


p1 = Urun()  # nesne urettik. # samsung s10
p2 = Urun()  # Iphone 12
p3 = Urun()  # Iphone 12 pro
p4 = Urun()  # huawei p20 lite

urunler = [p1, p2, p3, p4] # hepsini liste içine alabiliriz

for p in urunler:
    print(p)
