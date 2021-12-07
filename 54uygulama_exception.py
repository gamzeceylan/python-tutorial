# 1: Liste elemanları içindeki sayısal değerleri bulunuz

liste = ["1", "2", "5a", "10b", "abc", "10", "50"]
"""
-Benim yaptığım

for i in liste:
    try:
        sonuc = int(i)

    except Exception as e:
        sonuc = "hata Cevrilemedi"

    print(sonuc)

"""

"""
-Hocanın yaptığı

for i in liste:
    try:
        sonuc = int(i)
        print(i)

    except ValueError: #çeviremezse döngü durmaz, hatayı atlar devam eder
        continue


"""

# 2: kullanıcı "q" (quit() : uygulamayı sonlandırmak) değerini girmedikçe aldığımız her
# inputun sayı olduğuna emin ol aksi halde hata mesajı çıkart

"""
while True:
    deger = input("sayi : ")
    if deger == "q":
        break
    else:
        try:
            sayi = float(deger)
            print(sayi)
            break

        except:
            print("Hatalı giriş")
            continue

"""
# 3: Dictionary ve key bilgilerini parametre olarak alan get(d, key) fonk. yazdır
# d= {"urunAdi": "samsung s10"}
# d["price"] =>KeyError

# get(d, "price") => none
# get(d, "urunAdi") => samsung s10

d = {"urunAdi": "samsung s10"}

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d,"urunAdi"))
print(get(d,"fiyat"))
