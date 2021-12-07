"""
- string ler karakter dizileri olarak adlandırılır.
- python da char veri tipi yok. tek karakter de tanımlasan o karakter dizisidir. yani str türü
- karakter dizileri 0 dan başlayarak sağa doğru ve -1 den başlarayarak sola doğru gider
- istediğimiz kadar karakter alabiliriz ama bunun için string slicing bilmemiz gerekiyor

"""
name = 'Gamze'
gender = 'K'  # bu da karakter dizisi
age = '21'  # bu da karakter dizidir.
msj = "Benim adim : " + name + " ve Yaşım : " + age
print(msj)
print(msj[-6])  # m verir

surname = "Ceylan"
print(surname[-1])  # n verir
print(surname[0])  # c verir
