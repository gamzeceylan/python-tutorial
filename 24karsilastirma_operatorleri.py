"""
-karşılaştırma operatorleri varsa true ya da false döner. CEVAP BOOLEAN DIR

- (=) atama işlemi yapar
- (==) denk mi olarak döner 
- (!=) eşit değil mi diye sorar
- (>)
- (<)
- (>=)
- (<=)
- True int karşılığı 1 dir. int(True) = 1
"""
a, b, c = 5, 10, 5
username = "gmzcyln"
sonuc = (a == b)
sonuc = (a == c)
sonuc = (username == 'gmzcyln')
sonuc = (a > b)
sonuc = (True == 1)  # true döner. True sayısal değeri 1 dir
sonuc = (False == 0)  # false sayısal degeri 0 dır
print(sonuc)  # false döner
print(int(True))

ortalama = (50 + 40 + 60)/3
print(f"Ortalama : {ortalama}, Geçme Durumunuz : {ortalama>=50}")
# ortalama>=50 burası true ya da false yazdırır


_email = "ggamzeeceylan@gmail.com"
_sifre = "1234"

email = input("Email giriniz : ")
sifre= input("Sifre giriniz : ")

isEmail = (email.lower().split() == _email)
#artık ne kontrolü yapmak istiyorsan eklersin. büyük-küçük harf duyarlılığını kaldırırsın ya da boşlukları kendin islersin vs

print(f"Mail doğruluğu : {isEmail}")
