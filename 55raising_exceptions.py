# Raising Exceptions : Hata Nesnesi Fırlatma

# uygulamanın gidişatın agöre normalde hata sayılmayan ama bizim içi hata olabilecek durumlarsa kendimiz hata fırlatabiliriz
# örneğin x 5 ten küçük olsun istiyoruz, küçü grilirse hata sayılsın
# bu durumda raise anahtar sözcüğü ile istediğimiz hatayı fırlatabiliriz
# ilgili hatayı fırlattıktan sonra hatanın yanında parametre olarak mesajı yollayabiliriz

"""

x = 10
if x > 5:
    raise ValueError("x 5 ten büyül olamaz")

# raise ValueError da yazabilirsin mesaj yazmak zorunda değilsin

"""


def colorize(text, color):
    colors = ["blue", "black", "pink", "purple"]
    if type(color) is not str:
        raise TypeError("color str tipinde olmalıdır")

    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır")

    if color not in colors:
        raise ValueError("geçersiz renk girişi")

    print(f"{text} {color} olarak yazdırıldı")


"""
NOT : Hata fırlatıldıtan sonra aşağıda kalan hiç bir ifade özel bir blog içinde değilse finally gibi çalıştırılmaz.
mesela def teki print açıkta ama hata fırlayınca kod oraya gelmez

"""

"""
colorize("merhaba", "blue")

"""

# yapılıcak hatayı da yakalayabiliriz (anlamadım)
"""
try:
    colorize("merhaba", "blu")
except Exception as ex:
    print(ex)
"""

# hataların tipine göre alabiliriz (anlamadım)
"""
try:
    colorize("merhaba", 1)
except (TypeError,ValueError) as ex:
    print(ex)
"""
