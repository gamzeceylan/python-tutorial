import os
import datetime

"""
- os modulü işletim sistemiyle alakalı bir bilgi sunar. 
- klasor işlemleri, dosya işlemleri os üzerinden yapılabilir

result=dir(os)
print(result)

"""
# ---------------- klasör oluşturma -----------------
# result = os.name # işletim sistemini söyler nt demek window işletim sistemini kullanıyor demek
# os.mkdir("newdirectory") #bulunduğumuz dizinde dosya oluştrurur


# ----------------- etkin dizin öğrenme ---------------------------
# result=os.getcwd() # şuan bulunulan dosyanın nerede olduğunu yani path ini verir


# ---------------------dizin değiştirme -----------------------------

# chdir() konum değiştirir. mkdir ile dosya oluşturmadan önce istediğin dizine geçebilirsin ve orada dosya oluşturabilirsin

# os.chdir('C:\\') # mesela şuan C deyiz
# os.chdir('..') # olduğumuz konumdan bir üst konuma geçtik
# os.mkdir("yenidosya") #bir üst konuma geçtiğimiz için desktop da dosyayı oluşturur

# os.chdir('../..') # bulunduğumuz konumdan iki üst konuma deçtik

# ------------------------- iç içe klasör oluşturma --------------------------------
# os.makedirs("newdirectory/yeniklasor") #geçerli dizine iç içe oluşturur


# ----------------  klasörleri listeleme --------------------

# result=os.listdir() bulunduğun konumdakileri getirir
# result=os.listdir('c:\\Users\\gamze ceylan\\Desktop')

# ---------------- listelenen klasorleri filtreleme -------------
"""
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)
"""

# ------------- dosya hakkında bilgi sahibi olma-------------------

"""
- stat ile bazı bilgiler gelir. 
- örneğin st_size : dosyanın byte cinsinden büyüklüğünü verir
- st_atime : dosyaya son erişilme zamanı 
- st_ctime : oluşturulma zamanı
- bu tarih bilgileri pek anlaşılır biçimde değildir. datetime modulu ile bunları anlaşılır hale getirebiliriz
"""

dosya = os.stat("21sets.py")  # time ler saniye üzerinden gelir

# saniyeyi tarihe çeviriyoruz - oluşturulma tarihi (create)
result = datetime.datetime.fromtimestamp(dosya.st_ctime)

# saniyeyi tarihe çeviriyoruz - son erişilme tarihi tarihi (access)
result = datetime.datetime.fromtimestamp(dosya.st_atime)

# saniyeyi tarihe çeviriyoruz - değiştirlme tarihi (modified)
result = datetime.datetime.fromtimestamp(dosya.st_mtime)
# result=os.getcwd()

print(result)


# ----------- istediğin programı çalıştırma ----------------
# system üzerinden istediğin programı çalıştırabilirsin

# os.system("spotify.exe") # spotify direkt açılır


# ----------------- klasor adi değiştirme ---------------

# os.rename("newdirectory","yeniklasor") # aynı dizindeyse. farklı dizindeyse yol vericen sanırım

# ------------- klasor silme ---------------------------------
# os.rmdir("yeniklasor") #eğer klasor içi boşsa silinir

# os.removedirs("yeniklasor/mod") #klasor ve alt dizinleri silinir


# -------------------- path -------------------------------
# path dosya yolu işlemleridir.

# dosyanın tam konumunu verir
result = os.path.abspath("yeniklasor")
print(result)

# dirname de konumu verilen dosyanın dizin isimini verir. dizin ismi : dosyanın adının yoldan çıkarılmış halidir.
result = os.path.dirname(
    "C:/Users/gamze ceylan/Desktop/python_lessons/yeniklasor")
print(result)

# dizin öğrenmek istiyorsun ama dosya yolunu bilmiyorsan iki meotdu birlikte kullanman gerekir
# dosyanın tam yolunu buluyo bulduğu yoldan da dizin ismini alıyo
result = os.path.dirname(os.path.abspath("yaniklasor"))

# dosyanın ilgili konumda olup olmadığını kontrol etme
# aynı dizinde aradığımızda direkt adı yazıyoruz ama yol da verebilirdik
# exsists bool döner
result = os.path.exists("yeniklasor")
result = os.path.exists("C:/Users/gamze ceylan/Desktop/python_lessons/yeniklasoooor")

#ulaştığın yer bir klasor mu ?
result = os.path.isdir("C:/Users/gamze ceylan/Desktop/python_lessons/yeniklasor")

#ulaştığın yer bir dosya mı ?
result = os.path.isfile("C:/Users/gamze ceylan/Desktop/python_lessons/yeniklasor")

# path oluşturma
# böyle bir path yok ama verdiğin değerlerle varmış gibi oluşturabilirsin
# path bilgilerini birleştirdiği için join
result = os.path.join("C:\\","deneme", "deneme1")

# path bilgilerini bölme (sadece dosya adını ayırır)
result = os.path.split("C:\\deneme\\aa\\bb")

# uzantıyı bölme. sadece uzantı ayrılır
result = os.path.splitext("C:\\deneme\\aa\\bb.py")
result = os.path.splitext("bb.py")

# örneğin bir resmin adını değiştiriceksen önce uzantısından ayırmamız sonra da ismi değiştirmemiz sonra da uzantıyla birleştirmemiz gerekkir

resimAd=result[0]
resimYol=result[1]

print(resimAd,resimYol)
print(result)
