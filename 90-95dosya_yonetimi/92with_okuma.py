"""
-dosyayı açtığında kapatman gerekir.
- close işlemini yapmak yerine dosya üzerinde yapacağın işlemeri 
with bloğunda yapabilirsin. with bloğundan çıktığında dosya kapanmış olur

file = open("metin.txt")
file.close()
"""

with open("metin.txt") as file:
    print(file.read(10))
    print(file.tell())
    print(file.read())


sonuc = file.closed
print(sonuc)  # tue döner çünkü kapandı

# tell() cursor un bulunduğu indexi döner

print("progress".center(30, "*"))

# for ile dosyayı okuma
with open("metin.txt") as file:
    for i in file:
        # print(i) # dosya her satırı okunur ve alta geçer
        print(i, end="")  # her satır okunduktakn sonra boşluk bırakmayı kapadık


"""
- olmayan dosyayı okursan FileNotFoundError hatası alırsın.

"""
try:
    with open("asdf.txt", "r") as file:
        for i in file:
            print(i, end="")

except FileNotFoundError as ex:
    print("Dosya okuma hatası..", ex)

finally:
    print("Dosya kapandı")

# encoding="utf-8" ile dosyanın karakter okumasını değiştirebilirsin.
# open("asdf.txt", "r", encoding="utf-8")