# import datetime

"""
result= dir(datetime)
result=help(datetime)
print(result)

-zaman ile ilgili bir işlme yapıcaksan time, tarih ile ilgili bir işlem yapıcaksan date,
tarih ve zamanla alakalı bir işlem yapıcaksan datetime classına ulaşabilirsin
-time ve date içinde olan işlemler datetime içinde de vardır. bir nevi iki sınıfın birleşimi gibi

NOT : now() ve today() aynı bilgileri verir


"""

from datetime import datetime

result = datetime.now()  # şuanki tarih saat gelir
# böyle hour, year, month, minute bilgisini vs alabilirsin
result = datetime.now().year


# ya da böyle kullan
simdi = datetime.now()
simdi = datetime.today()

result = simdi.year
result = simdi.month
result = simdi.second
print(simdi)


# -------- ctime() -----------------
# ctime() içine bir object ister. datetime.now() gibi. daha ayrıntılı tarih gösterir. ayın adı vs
# str döner
simdi = datetime.today()
result = datetime.ctime(simdi)
print(result)

# --------- strftime() -----------
# now() ya da today() ile alınan saat ve tarih bilgisinden istediğimizi ekrana yazdırabiliriz.
# .year .month tan daha esnek bir kullanımdır
# w3school ya da python dan datetie modlunun kulanımını okursan hangi harfin neye karşılık geldiğini görebilirsin

simdi = datetime.now()
result = datetime.strftime(simdi, '%Y')  # sadece yıl
result = datetime.strftime(simdi, "%B")  # sadece ay
result = datetime.strftime(simdi, "%Y %B %A")

print(result)


# --------- strptime() --------
# string ifadeyi çözümler
"""
# asagidaki gibi bir string ifade gelirse hangisi ne program bilemez böyle tek tek ayırmamız gerekir

t = "21 Nisan 2019"
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)

"""
t = "21 April 2019 hour 10:12:30"

# kendi otomatil datetime türüne çevirir. %d gibi karşıklarını yazmamız gerekiyor. onun haricindekileri
# olduğu gibi eklemeliyiz hour : gibi
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

# artık result bir datetime modulu istediğin işlemi yapabilirsin
result = result.day
print(result)

# ------------ datetime() --------------------------

# verdiğimiz veriyi tarihe datetime modülüne çevirir

birthday = datetime(1983, 5, 9, 12, 30, 10)
simdi = datetime.today()

#---------------- timestamp ---------------------
# timestamp() metodu ilgili tarih objesini bize saniye cinsinden getirir.
result=datetime.timestamp(birthday)

#------------- fromtimestamp ------------------------
# saniyeyi tekrar datetime bilgiseine çevirir.
result=datetime.fromtimestamp(result)
print(result)

"""
NOT : fromtimestamp(0) 1970-01-01 03:00:00 döndürür. bu bilgisayarlar için milat bilgisidir
-yani timestamp ile saniyeye dönüştürdüğünde bu milat tarihi üzerinden o ana kadar olan zaman saniye olarak hesaplanır
"""
result=datetime.fromtimestamp(0)
print(result)

# aşağıda timedelta objesi gelir 13831 days, 4:21:40.518048 gibi bir şey döner
result = simdi-birthday

# aradaki farki days seconds olarak hesaplayabilirsin
result = result.days
#result = result.second
print(result)

# -------------- timedelta ------------------------
# ileriki bir tarihi bulmak istiyorsan timedelta yı import etmelisin.
# datetime içinde timedelta vardır.

from datetime import timedelta

simdi = datetime.today()
result= simdi + timedelta(days=100) # şuanın üzerine 10 gün ekledi
print(result)


result= simdi + timedelta(days=100,minutes=10) 
result= simdi - timedelta(days=10) # 10 gün azaltmak