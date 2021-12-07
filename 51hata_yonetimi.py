"""
- oluşabilecek hatalara exception,
- hatayı ele alma yani exception handling de hata mesajı çıkmasına denir
- uygulama yı biz çalıştırırken hata almayız da uygulmaayı yayına soktuğumuz zaman hata alma ihitmaline karşı kullanılır
- örnekğin kullanıcıdan sayısal değer istdiğimizde kullanıcı harf girebilir.
- hatalar bir objeye karşılık gelir
- her hatanın da özel bir adı vardır
- hataları kullanıcıların hata objelerini görmesi istenmez. hatalar kayıt edilir. loglanır. hangi işlem sonucunda, ne zaman hangi hata alındı vs.
buna göre de geliştirici hataları düzeltir

-hatalar try except bloklarıyla alırır. try da işlemler yapılır. except de hata çıkarsa gelebilecek hataları ele alırsın. ve hata aldığında bu blok çalışır

"""


try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x+y)

except:
    print("Hata oluştu") # örn bir harf girerse hata oluşur
