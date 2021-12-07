def selamla(isim):
    return "Merhaba "+isim


sonuc = selamla("Gamze")
print(sonuc)

##########


def topla(a, b):
    return a+b


sonuc = topla(3, 6)
print(sonuc)


"""
NOT : abs gelen negatif değeri pozitif yapar

"""
sonuc = abs(-6)
print(sonuc)  # çıktı : 6


###########
# gönderilen sayı kadar ekrana txt yazdıran fonksiyon

def yazdir(txt, adet):
    print(txt * 5)  # böyle yazdırabilirsin


# \n alta geçer.
yazdir("Merhaba\n", 5)


###########
# kendisine gönderilern 2 sayı arasındaki asal sayıları bulan fonksiyon

#tam çalışmıyor sorunu anlamadım
def asalSayiBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1 :
            for i in range(2, sayi):
                if(sayi % i == 0):
                    break

                else:
                    print(sayi)
                    

asalSayiBul(5,10)
