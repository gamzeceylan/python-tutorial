"""
- amacımız key- value seklinde bilgileri saklamk
- dictionary, unorded yani sıralanamaz. sort() metodunu kullanamayız
- ama değiştirilebilir, veri eklenebilir ancak SIRALANAMAZ!!!!!!!!!!
- her bir verinin key i ve value si vardır. list lerden farkı budur.
- key, index numarasıdır.
- json veri yapısı, veri taşırken kulllaılır. dictionary yapısı json veri yapısıyla aynıdır 
"""
plakalar = {
    41: "Kocaeli",
    54: "Sakarya",
    34: "İstanbul",
    69: "Bayburt"

}

print(plakalar[69])  # [] içine key değeri alır ve value döndürür

# ---------------- Eleman ekleme -------------------------
# 17 ye karşılık değer olmadığı için 17: "Çanakkale" olarak direkt ekler
plakalar[17] = "Çanakkale"

# --------------- Eleman Değiştirme ------------------------
# aşağıdaki gibi yazdığımızda key değerini buluyorsa direkt değştirir. (bulamazsa eklioyrdu)
plakalar[41] = "aaa"

print(plakalar)

# ---------------- Dictionary içinde Dictionary------------
# iç içe tanımlama yapabiliriz
# örn 100 bir öğrenciyi tutuyor
ogrenciler = {

    100: {
        "ad": "Çınar",
        "soyad": "Turan",
        "yas": 4,
        "notlar": [70, 80, 90]
    },

    105: {
        "ad": "Gamze",
        "soyad": "Ceylan",
        "yas": 21,
        "notlar": [70, 80, 90]
    },

    110: {
        "ad": "Zeynep",
        "soyad": "Arslan",
        "yas": 20,
        "notlar": [70, 80, 90]
    }
}

print(ogrenciler[100])
print(ogrenciler[105])
print(ogrenciler[100]["ad"])  # ikinci [] ile ikinci dic e ulaşabiliriz
print(ogrenciler[100]["notlar"][0]) #böyle de not a inebiliriz

ortalama=(ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] +ogrenciler[100]["notlar"][2])/3
print(f"{ogrenciler[100]['ad']} ogrencinin ortalamasi : {ortalama}")