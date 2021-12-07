"""
- | import moduleAdi | ile modulu dosyana dahil et

- ilgili module de hangi metodları kullanabileceğini bilmiyorsan :

value = dir(math)
print(value) 

ile ekrana fonk isimlerini yazdır.

- yada fonksiyonları nasıl kullanacağını bilmiyorsan

value = help(math)
print(value)

- ya da tek bir modulun nasıl kullanılacağını öğrenmek istioyrsan 

value = help(math.factorial)   # . dediğinde içindeki fonk gelir
print(value)

-------- yukarıdakilere tabiki dokumandan da bakabilirsin -----------
"""

# 1. yol
"""
import math

value = math.sqrt(5)
value = math.factorial(3)
value = math.floor(5.9)
value = math.ceil(5.9)
print(value)

import math as m #takma isim verip de kullanabilirsin
deger=m.factorial(5)
print(deger)

"""

# 2. yol
"""
-from * ile imort ettiğinde artık modul ismini yazmadan ulaşabilirsin. çünkü tüm kütüp import etmiş olursun 

from math import *

value = factorial(5)
print(value)

"""

# 3. yol
"""
- sadece kullanmak istediğin fonksiyonları import edebilirsin
- import etmediklerini kullanamazsın

from math import factorial,sqrt

value=factorial(6)
value=sqrt(9)
print(value)

"""

# hangi fonksiyon kullanılır ?
"""
- python modulundeki bir fonksiyon ile aynı adda bir fonksiiyon tanımladığımızda en son yazılan kullanılır
- en son yazılan bir üsttekini ezer

"""

"""
-aşağıda en son yazıldığı için ptyhon fonksiyonu kullanılır

def sqrt(x):
    print("x : " + str(x))


from math import sqrt

value = sqrt(6)
print(value)

"""

"""
- aşağıda en son yazıldığı için bizim fonksiyonumuz kullanılır

from math import sqrt

def sqrt(x):
    print("x : " + str(x))


value = sqrt(6)
print(value)

"""