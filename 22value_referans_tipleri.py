"""
----- value types -----

-verinin kendisiyle ilgileniriz
-string ve number(float, int) type ler value tanımlamadır. 
-her biri ayrı alanlarda tanımlanır ve değerler kopyalanır

x=10
y=5
x=y
y=8
print(x)  ekrana 10 yazar çünkü y ni değişmesi onu etkilemez. ikisi farklı
          alanlarda tanımlanır ve fakrlı yerleri gösterirler

------- references types -------

-verinin adresiyle ilgileniriz
-list, class

a = ["elma", "muz"]
b = ["elma", "muz"]
a = b
b[0]="kivi"
print(a[0])  ekrana kivi yazar. b nin değişmesi a yı da etkiler.

-çünkü a ve b bir pointer dır.
-a ve b belleğin tanımlanan alanında adres tutarlar ve belleğin başka bir alanında
değerleri gösterirler. a=b dediğinde adresler,n gösterdiği yerleri aynı yapıyorsun

-orneğin 500 tane urun listemiz var. ve urunleri kopyalayıp taşımak sonra üzeirnde işlem yapmak
istiyoruz. 500 tane ürün ve her birinin bilgisini kopyalamak bellekte çok fazla yer kaplar ve performans
kaybı olur. tamamnını kopyalamk yerine adresi kopyalayıp adresi çağırdıdğında tüm bilgilerin gelmesi
ve üzerinde direkt değişiklik yapılabilmesi daha performanslı ve belleği gereksiz yere meşgul etmez
"""