"""
- örneğin len() liste için özel bir metottur. aynısı class lar için de vardır

liste = [1, 4, 5, 76]
print(len(liste))

s = "hello world"
print(len(s))

"""
"""
- list sınıfının kendisinde len metodu vardır.
- eğer senin tanımladığın bir tipte (Film) de olsun istiyorsan class içinde metodu tanımlamalısın.
- __method__ bu alt çizgiler sınıfa özel bir metod olduğu ve dışarıdan çağrılmaması gerektiğini söyler.
Dışarıdan çağırabilirsin ama mantık olarak çağırmamalısın

"""
# metotları özelleştirmen lazım


class Film:

    def __init__(self, baslik, yonetmen, sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure

    # str yi çağırdığımızda
    def __str__(self):
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi"

    # objeyi direkt çağırdığımızda print(f1) gibi
    def __repr__(self):
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi"

    # len(f) te çalışır
    def __len__(self):
        return self.sure

    # del f dediğinde çalışır. bu meotdu yazmasan da obje silinir. bu ekstra çalışır
    def __del__(self):
        print("Film objesi silindi")




# f=Film()

liste = [1, 4, 5, 76]
"""
print(type(f)) 
print(type(liste))

print(str(f)) # f in adresi döner. çünkü kendi tanımladığımız bir tip ve ne yapıcağını metoda söylemedik
# <__main__.Film object at 0x000001CAEDACCFD0> döner

print(str(liste)) # list sınıfında bu metot ezildiği için direkt liste döner
# [1, 4, 5, 76] döner

"""

# __str__ metodunu Film e yazdıktan sonra

f1 = Film("Ekşi Elmalar", "Yılmaz Erdoğan", 98)
print(str(f1))  # Ekşi Elmalar, Yılmaz Erdoğan tarafından yönetildi

print(f1)  # repr çalışır

# filmin süresi döner. metodu class ta özelleştirmeden önce f, len e sahip değildi
print(len(f1))


# del f1
