import db


def urunEkle(urunAdi, fiyat):
    db.urunler.append({
        "id": len(db.urunler)+1,
        "urunAdi": urunAdi,
        "fiyat": fiyat
    })


def urunGuncelle(id, urunAdi, fiyat):
 
        for i in db.urunler:
            if i["id"] == id:
                i["urunAdi"] = urunAdi
                i["fiyat"] = fiyat
                break




def urunleriGetir():
    for urun in db.urunler:
        print(urun["id"], urun["urunAdi"], urun["fiyat"])
