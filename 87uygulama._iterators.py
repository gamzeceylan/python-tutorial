class Counter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # nesneti çağırdığımızde iterable bir nesne olarak geri göndericek
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x

        else:
            raise StopIteration


"""
-Counter ı iterable yapmadan hata alırsın. __iter__ ile iterable yap

for i in Counter(10,20):  # bunu kullanabilen için Counter nesnesi iterable olmalı. 
               print(next(i))

#iter metoduyla iterable yapabilmek içide sıfnın __iter__metodunu çalıştırmalısın
"""

# arka planda __iter__ çalışacak ve iterable bir nesne dönecek
iterator = iter(Counter(10, 20))

# next fonksiyonunun çalışması için de  __next__ özelliği kazandırmalısın
print(next(iterator))

# while ile next diyerek yazdırabilirsin

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break
