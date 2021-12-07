"""
- Pip ile harici paket kurulumu
- python kullanımı kolay olduğu için bir çok yazılımcı destek verir.
- python paket yönetim havuzu var. kullanıcılar python ile bir modul geliştiriyorlar. birden 
fazla modul olduğunda ise paket olarak adlandırılır.
- bu uygulmaa geliştirme paketlerini pypi (paypay : pyhon paket geliştirme havuzu) yüklüyorlar
- bu havuz içerisinden de biz bir paket alıp uygulamamızı kolaylıkla yapabiliyoruz.
- örn web için django, veri analizi için numpy, gibi pakatleri projene kolaylıkla dahil edebilirsin
- bu paketleri projene dahil edersin.

----------- Peki bu paketleri nasıl yüklüyoruz ? ------------------
- projeye paket eklemek için bizim ekstra bir kütüpaneye ihtiyacımız var : pip
- termcolor modulu üzerinde çalışalım
- python 3.4 ten sonra bir kurulum yaptıysan bu paket otomatik gelmiştir
- pip --version yazıp paket versiyonuna bakabilirsin



"""
import termcolor

"""
- bunları dokuman üzerinden de inceleyebilirsin
sonuc= dir(termcolor)
sonuc= help(termcolor)

print(sonuc)

"""
# sonuc= help(termcolor) den fonksiyonu okursan zaten neyi nasıl yazacağını, seçenekleri söyler

sonuc=termcolor.colored("Merhaba",color="red", on_color="on_yellow",attrs=["bold"])

print(sonuc)

# pip list : ile kurulu olan paketleri listeleyebilirsin
# pip uninstall pacged_name : paketi sileblirsin

