# ---------- Identity operator : is -------------------
"""
- (==) deger karşılaştırması yapar.
- is adres karşılaştırması yapar

"""
x = y = [1, 2, 3] #x ye y aynı adesi tutarlar ve aynı yeri gösterirler
z= [1,2,3]

sonuc = (x == y) # değer karşılaştırması yapar true döner
sonuc = (x == z) # deger karşılaştırması yapar true döner
sonuc = (x is z) # adres karşılaştırması yapar false döner
sonuc= (x is y) # adres karşılaştırması yapar true döner

spnuc= (x is not z) # is not da sotabilirisin. true döner

print(sonuc)


# -------------- Membership operator : in ----------------------
"""
- elemanın olup olmadığını sorar.

"""
x= ['apple', 'banana']
print('banana' in x) #true döner

name= 'Çınar'
print(name in x) #false döner

print('banana' not in x) #false döner