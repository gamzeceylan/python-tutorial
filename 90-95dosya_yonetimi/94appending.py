# "a" : append, ekleme. dosya konumda yoksa dosya oluşur.
# a odu wtire gibi içerikleri silmez, üzerine bir bilgi ekle
# "r+" : hem okuma hem yazma modu. dosya konumda yoksa hata verir

# append dosyanın en sonuna yazar
with open("write.txt", "a") as file:
    # kursorun konumunu değiştirmen etkilemez. append kaldığı yerden devam eder
    file.seek(0)
    file.write("\nbu metin yeni eklendi")


# r+ dosyanın en başına yazar. o yüzden önce read() ile dosyayı sona kadar okuyup sonra ekleme yaparsan sona eklenir
with open("write.txt", "r+") as file:
    # file.seek(10) kursoru istediğin yere de alabilirsin
    file.read() # kursoru sona alır
    file.write("\nlalala")

