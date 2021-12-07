# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı : open(dosyaAdi, dosyaErişmeModu)
# dosyaErişmeModu => dosyayı hangi amaçla kullanıcağımızı belirtir.
# "r" => okuma modu. ! belirtilen konumda dosya olmalıdır.
# dosyaErişmeModu vermezsen varsayılan olaran "r" alınır.
# read modunda dosyayı açmak demek o dosyanın belirtilen yolda mutlaka olması demek yoksa hata verir


# açılma işlemi bir obje getirir ve bu obje bellekte yer kaplar
# bellekten silmek için dosyanın kapanması gerekir. 
f = open("metin.txt")
# dosyadan object döner. name : dosya adı, mode : açılma amacı, encoding : karakter kodlaması
print(f)


# yardım dokumani
# print(help(f))

# dosya read() ile okundu
print(f.read())
"""
NOT : dosyayı read() ile okuduğunda en baştan başlanır ve en sona gider orda kalır.
bunun üzeinden tektar read() çalıştırırsan '' boşluk döner.
- read() yalın olarak çağırdığında sona kadar okur ama tabiki ne kadar okuyacağını belirtebilirsin
"""

