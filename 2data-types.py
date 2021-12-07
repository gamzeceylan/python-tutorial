# int
# float
# string
# bool

"""
 x = input("x sayısını giriniz ") ile kullanıcıdan değer alabiliriz ama input string değer alır. int donuştürmen gerek

"""

x = input("x sayisinini giriniz : ")
y = input("y sayisini giriniz : ")

toplam = x + y
print("Toplam : " + toplam)

# str to int
toplam = int(x) + int(y)  # donusturme yaptik
print(toplam)

a = int("20")  # bu da bir donusturmedir
print(a)
print(type(a))


z = int(input("z : "))  # direkt input u sa donusturebiliriz
print(type(z))

# int to float
k = 4
result = float(k)
print(result)  # float a dönüştürdüğümüz için 4.0 yazar. int türünde 4 tü
print(type(result))


# float to int
m = 12.4
result = int(m)
print(result)
print(type(result))  # m int dönüşünce sadece 12 kısmı alınır


# bool to str
tip = False
result = str(tip)
print(type(result))


# bool to int : true int karşılığı 1, false int karşılığı 0 dır
tip2 = False
result = int(tip2)
print(result)

tip2 = True
result = int(tip2)
print(result)
""" 
 True == 1 bize true döner
 
"""
