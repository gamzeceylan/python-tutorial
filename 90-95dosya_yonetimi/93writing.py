# "w" : (Write) yazma metodu.
# eğer konumda dosya yoksa aynı dizine dosyayı oluşturuyor
# eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur
# read modunda dosya otomatik utf-8 olarak okunur.
# ama write modunda farklı karakter kodlaması vardır. encoding="utf-8" diye belirtmelisin

file = open("write.txt", "w", encoding="utf-8")

""" 
-her sefeinde içeri farklı bir şey yazdırdğında bunların aynı yerin içine değil
sürekli sıfır dosyaya yazıldığını görürsün. çünkü dosya varsa silinir yeni oluşturulur ve yazılır
"""
file.write("sfdd\n")
file.write("asd.a sdff asdp\n")

file.close()  # tabiki dosyayı kapatman gerekiyor.
print(file)

# ya da kapatmadan with bloğunda işlem yaparsın

with open("write2.txt", "w", encoding="utf-8") as file:
    file.write("işğüşiçdslf\n")
    file.write("işğüşiçdslf\n")
    file.write("işğüşiçdslf\n")
    file.write("işğüşiçdslf\n")

with open("write2.txt", "r", encoding="utf-8") as file:
    print(file.read())


with open("C:/Users/gamze ceylan/Desktop/py_dosya_okuma.txt", "w", encoding="utf-8") as file:
    file.write("yalan dostum aşk diye bir şey yok")
