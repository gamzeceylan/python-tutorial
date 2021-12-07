"""
module1 (db)    : urunler listei olucak urunadi, urunid, urun fiyat bilgisi olucak
module2 (methods)   : urunEkle(), urunGuncelle(), urunleriGetir()
module3 (app)  : yeni ürün ekleme =>  urunEkle("iphone 11 pro" 7000)
                 ürün güncelle => urunGuncelle(1, "iphone 12 pro", 8000)
                 ürünleri listele => urunleriGetir()


"""
#import methods
from methods import *


urunleriGetir()

urunEkle("kalem",50)
urunleriGetir()

urunGuncelle(2,"elma",5)
urunleriGetir()