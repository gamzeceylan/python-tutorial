opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

# -------------------- get() ----------------------
# get() metodu da verdiğin key değerini getirir. aslında opelObj["marka"] ile aynı işi yapar
sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")


# -------------- dictionary ekrana yazdırma ---------------
"""
for x in opelObj:
    print(x)

-x üzerine key değerlerini alır. böyle yazarsan ekrana marka model yil yazar.
"""
# 1.yol :
# asağıdaki gibi value bilgilerine ulaşırsın
for x in opelObj:
    print(opelObj[x])

# 2. yol : values() metodu
for x in opelObj.values():
    print(x)

# 3. yol : items()
# items() ile key ve value değerlerine birlikte ulaşabiliriz. x key değerini y value değerini kopyalar
for x, y in opelObj.items():
    print(x, y)


# ---------------- deger arama ------------------------
# key bilgisini arayabiliriz.
sonuc = 'marka' in opelObj  # true ya da false döner


# ------------- eleman sayısı ------------------------
sonuc = len(opelObj)

# ----------------- eleman ekleme -------------------------
# özel bir eleman ekleme metodu yok
opelObj["renk"] = "kırmızı"

# --------------- eleman silme --------------------------
# pop() içine verilen key değerini siler
opelObj.pop("renk")

# popitem() son değeri siler.
opelObj.popitem()

# del ile de verilen key deperi silinebilir
del opelObj['marka']

# clear() listenin elemanlarının tamamını siler. ama liste hala varolur. sadece içi boşalır ve {} döner
opelObj.clear()

# del listeyi komple bellekten kaldırır
# del ise bellekten komple siler ve opelObj yi aradığımızda defined hatası alırız yani tanımlanmamış değer
del opelObj


# del yaptık hata almamak için tekrar tanımlıyorum
opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

# -------------- objeyi kopyalamak ------------------
"""
# bir dictionary aşağıdaki şekilde kopyalanamaz. çünkü referans tiplidir. adres tutarlar ve adresler 
koyplanır ve gösterdikleri yer aynı olur
# birinde yaptığın bir değişiklikten diğeri de etkilenir. c# ta class lardaki gibi. belleğin heap bölgesinde açılırlar
# copy() metodu kullanmalısın 

obj=opelObj
print(obj)

"""
# şimdi obj üzerindeki değişiklik opelObj yi etkilemez
obj = opelObj.copy()
obj["marka"] = "Clio"

print(sonuc)
print(opelObj)

# --------------- update() --------------------
# update() ile verilen bilgi değiştirilir, ekstra bir değer eklemek istiyorsan da kabul eder

opelObj.update({
    "marka": "BMW",  # marka değeri değiştirilir
    "renk": "kırmızı"  # renk değeri eklenir
})

print(opelObj)