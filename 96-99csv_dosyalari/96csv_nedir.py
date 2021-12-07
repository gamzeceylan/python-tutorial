"""
- CSV : comma separated values. virgülle ayrılmış değerlerç
- txt gibi karışık bilgi değil başlığı olan, virgülle ayrılmı ve düzenli oluşmuşmuş
veri içerirler.
- python da cvs dosyaları ile çalışmak için csv kütüphanesi vardır
- csv metotları normal dosya metotları ile aynıdır. 
- veriler bir obje içine alınır. o yüzden listelerde çalışıyor gibi çalışırsın

- örnek olarak veri setlerini bulabileceğimiz kaggle sayfası vardır. içinde büyük veri
setleri vardır
- bir veri indirdiğinde csv uzantılı iner.
- excel ile açarsan tablo şeklinde, txt ile açarsan virgülle ayrılmış verileri görürsün

"""
# dosya sonuna kada okuma
with open("products.csv") as file:
    print(file.read())  # dosya metni döner


# bilgilerin anlamlı hale gelmesi için satır satır okuman gerekir.

import csv  # csv modulunu eklioyoruz

with open("products.csv") as file:
    csv_reader = csv.reader(file)
    print(csv_reader)  # object nesnesi döner

    # for ile her bilgi üzerinde gezebiliriz
    # her satır bir liste halinde gelir
    """
               for p in csv_reader:
                               print(p)
               """

    # istediğimiz indexi alabiliriz
    """
               for p in csv_reader:
                              print(p[0],p[1])
               """

    # eğer başlık bilgilerini istemiyorsak önce next ile ilerletiriz.
    """
               next(csv_reader)
               for p in csv_reader:
                              print(f"ürün adı : {p[0]}, ürün fiyatı : {p[1]}")
               """

    # satışta olanları getirme
    next(csv_reader)
    print(list(csv_reader)) #liste şeklinde döner. gördüğün gibi listeler ile çalışıyoruz
    for p in csv_reader:
        if p[2] == "True":
            print(f"ürün adı : {p[0]}, ürün fiyatı : {p[1]}")


# listeyle çalıştığımız için hangi elemanın hangi indexte olduğunu bilmen gerekiyor
