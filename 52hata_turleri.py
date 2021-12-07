"""
x = int(input("x : "))
y = int(input("y : "))

print(x/y)

-yukarıda x veya yerine 20a gibi bir şey girilirse ValueError, y yerine 0 girilirse division by zero hatası alırsın
- iki hata bilgilsini de kullanıcıya farklı mesajlarla göstememiz gerekir
- çünkü kullanıcı bu hatalardan anlamaz. açıklayıcı mesaj yazıyor olman gerekir
- hata turlerini de tanıyor olman
"""


#----- SyntaxError => yazım yanlışı -------
"""
# isim;

# def yazdir((:
      pass

# print("Merhba"a)

"""


#------ NameError => tanımlanmamış bir değişken kulanımı------
"""
# print(isim)

"""


#--------- TypeError => hatalı parametre kullanımı ------
"""
# len(5)

# 4 + "a"

"""

#------- IndexError => yanlış index numarası ------
"""
# liste = ["merhaba"]
  liste[1]

"""

#------ ValueError => hatalı tip kullanımı ---------
"""
# int("10a")

"""

#------ KeyError => key hatası ----------------
"""
# d={}
  d["ad"]

"""

#------ AttributeError => olmayan bir hataya ulamak istendiğinde-----------
"""
# "merhaba".upper()   doğru

# "merhaba".Upper()   yanlış

"""


"""
# python dokumanlarında Python Built-in Exceptions tan hata çeşitlerine bakabilirsin

# hatalar object türünden olduğu içi hataları genelleyip bütün hatalarda tek bir hata mesajını kullanıcıya
 çıkartabiliriz. hepsini tek tek ezberlemene gerek yok. sonra arka planda da alınan hata türlerini kayıt ederiz.
 sonra dokumandan bakıp hataya göre düzeltme yapabiliriz

"""