"""
- module yi eklemek için dosyalar aynı dizinde olmalı
- import module demek aslında module.py içinde yazdığımız her şey buraya da gelsin demek

"""

import module58  # module yi import et
import module58 as m  # module ye isim verip bu isim üzerinden de kullanabilirirz

# module dosyamız çok büyük olabilir ve herpsini kullanmak istemiyor olabiliriz. sadece ogrenci ve sayilar a ulaşabilirizS
from module58 import ogrenci, sayilar

# from ile tüm module yi import etmek istersen de * kullan.
from module58 *

# artık module58. ile module içindeki tüm özelliklere ulaşabilir ve burada kullanabilirsin
sonuc = module58.sayi
sonuc = module58.sayilar
sonuc = module58.sayilar[1]
sonuc = module58.topla(4, 5)

print(sonuc)

#
sonuc = m.topla(9, 8)
print(sonuc)


#
sonuc = ogrenci
print(sonuc)
