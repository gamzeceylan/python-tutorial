"""
- her değişken kendi tanımlandığı aralıkta geçerli olur

"""

name = "Gamze"


def test():
    name = "Çınar"
    # çınar üzerinde işlem yapar. ama çınar olmasaydı bir üsttetiki name de işlem yapıcaktı
    print(name)


x = 50

def test2():

    global x #global olan x i alır 50 yi. bunu kullanmak için global anahtar kelimesini kullanabilirsin
    print(f"x : {x}")
    
    x = 100
    print(f"chaned x to {x}")



test2()
