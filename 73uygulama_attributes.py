class Pet:
    cinsler = ["kedi", "köpek", "kuş"]

    def __init__(self, isim, cins):
        # bunu bu şekilde burda da tanımlayabilirdin ??
        # cinsler = ["kedi", "köpek", "kuş"]

        # cinslere self yazarsan artık her nesneye özel olur.
        # her hayvnın kendi özel listesi olur. ve tabiki o zaman artık class içinde self diyip ulaşıcaksın
        #self.cinsler = ["kedi", "köpek", "kuş"]

        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayval değildir")

        self.isim = isim
        self.cins = cins

    def get_cins(self, cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayval değildir")
        Pet.cinsler.append(cins)


boncuk = Pet("Boncuk", "kedi")
pasa = Pet("Paşa", "köpek")
mavis = Pet("Maviş", "kuş")

# kral=Pet("Kral","aslan") hata alırız

print(Pet.cinsler)  # cinsler listesine ulaştık

# nesne üzerinden de ulaşabiliriz?? hani sınıf adıyla ulaşabilirdik?
print(boncuk.cinsler)
print(pasa)

# hem nesne hem de class uzerinden ekleme yapabliriz
Pet.cinsler.append("balık")
boncuk.cinsler.append("timsah")

print(Pet.cinsler)


