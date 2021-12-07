class NewDict(dict): #dict sınıfında türettik
    def __repr__(self):
        print('repr metondundan mesaj var.')
        return super().__repr__() #dict in kedni __repr__ çalışır

    # missing metodu olmayan bir key istendiğinde çalışır.
    def __missing__(self,key):
        print("olmayan key bilgisi istiyorsunuz.")

    # key çeğrıldığında çalışır
    def __getitem__(self,key):
        print("bir elemanı çağırıyorsunuz.")
        return super().__getitem__(key)

    def __setitem__(self,key,value):
        print("listeye eleman ekliyorsunuz.")
        super().__setitem__(key,value)

    def __contains__(self,item):
        print("listede eleman arıyorsunuz") 
        return super().__contains__(item)
        # print("listede eleman arayamazsınız")
        # return False

data = NewDict({"first":"Sadık","last":"Turan"})


print(data["first"])
data["age"] #burda __missing__ çalışır. çünkü age key i yok
data["first"]="Çınar"

print(data)

print("first" in data)