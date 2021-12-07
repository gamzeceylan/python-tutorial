"""
# py yi güzel bir dil yapan özelliklerin başında moduller gelir
# kişiler ya da firmalar herhangi bir amacı hedefleyen bir modül yazar ve havuza atar, herkes havuzdan
modulu alır ve işlerini kısa sürede tamamlar
# py kurulu ile gelen moduller olduğu gibi kurulum ile gelmeyen ancak havuzda olan bir çok modül vardır.

#------------ Module Nedir ? -------------------

# uygulama büyüdükçe müdahale ederken sıkıntı yaşamamız için uygulamayı belli parçalara ayırmamız gerekiyor.
her parçaya da bir görev veririz. parçaları topladığımızda da programın kendisini temsil eder
# uygulamayı ayırdığımız heer bir parça bir modül dür ve modüller py uzantılı dosyalardır
# moduller birbiri içinde kullanılabilir 
# moduller bir bakıma fakrlı görevleri yerine getiren kütüphanelerdir.

orneğin moduleA.py de class oluştururuz, moduleB.py de fonksiyon tanımlamalarını yaparız, bu oluşturduğumuz
yapıları moduleC.py de çağırıp kullanırız. ama moduleC.py de bir fonk tanımlaması yapmayız.

# moduller 2 ye ayrılır. 
               1- Kendi hazırladığımız moduller 
               2- Hazır Moduller
                              a- Standart Kütüphane modülleri : py nin kendi geliştiricileri tarafından yazılmış olanlar.
                              örneğin math modulü. import diyip kendi uygulamanda kullanabilirsin

                              b- Üçüncü şahıs modülleri : py gelişriticileri değil 3. şahıslar geliştirmiştir.
                              bu kütüphanelerin hazır bulunduğu pypi(paypay) sitesi var. İstediğin kütüphanenin detaylarına
                              kullanımına oradan ulaşabilirsin

# mesela py ile bir web yapmak istiyorsak django kütüphanesini kullanman işini çok kolaylaştırır. rutin bazı işlemler senin
yerine yapılmıştır. tekrar yazmana gerek yok. yönlendirilirsin
# üçüncü şahıs modullerini kullanmak için : pip install package-name : ile uygulamana mutlaka kurman gerekir

"""
# kullanmak istediğimiz modüller aynı dizin içinde olmalı

"""
# import db dediğinde o sayfada db içindei özellikleri db. diyerek kullanabilirsin ve db içine import edilenler gelmez.
# from db import * dediğinde db sayfası komple entegre olur artık kullanmak için db demene gerek yok. ve db de yazdığın
kütüpleri de kullanabilirsin

"""