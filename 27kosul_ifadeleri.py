# ------------- if else blokları ------------------------
"""
- if içi true ie çalışır.
-blok oluşturmak için : ve tab kullanılır.
- indentation girinti hatasıdır. block oluştururken hata yaptın anamına gelir 
"""
import datetime  # bulunduğumuz tarihi almak için modül
if(5 < 10):
    print("Merhaba")

#####################

username = "gamzeceylan"
sifre = "12345"
if(username == "gamzeceylan" and sifre == "12345"):
    print("Giriş başarılı")

else:
    print("Username ya da parola yanlış")

####################

if(username == "gamzeceylan"):
    if(sifre == "12345"):
        print("Giriş başarılı")
    else:
        print("Yanlış parola")
else:
    print("Yanlış kullanıcı adı")

####################

x = 20
y = 10

if(x > y):
    print("x y den büyüktür")
elif (x == y):
    print("x ve y eşittir")
else:
    print("x y den küçüktür")

######################

# if else bloklarına bir şey girilmezse hata verir. hata almamak için pass anahtar sözcüğünü kullanmalısın
if(x > y):
    pass

else:
    pass


########################### uygulama ##############

# trafiğe çıkış tarihi alınan bir aracın servis zamanını hesaplayın


tarih = input("aranıcının hangi tarihte trafiğe çıktı? (1111/1/11) : ")
# string ler bir diziydi. ve / ile ayırıp gün ay yıl ı diziye attık
tarih = tarih.split('/')

print(tarih[0], tarih[1], tarih[2])

simdi = datetime.datetime.now()  # bulunduğumuz tarih gelir. ve object türnden
# print(simdi)

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
#aldığımız tarihi object yaptık

fark = simdi-trafigeCikis
gun=fark.days #tarih object inden gün bilgisini aldık

if(gun <= 365):
    print("1. servis bakım.")

elif( gun>365 and gun <= 365*2):
    print("2. servis bakım.")

elif(gun>= 365*2 and gun <=365*3):
    print("3. servis bakım.")

else:
    print("Hatalı Giriş")
