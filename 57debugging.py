# uygulama çalışırken aşamaları kontrol etmek istiyorsan debug yapmalısın
# debug için python db kütüp eklemelisin (import pdb)
# uygulamayı durdurmak istediğin yere pdb.set_trace() yazmalısın
# import pdb; pdb.set_trace() bu şekilde tek satırda da tanımlama yapabilirsin


# ------ komutlar -----
# l => list : geri kalan kodları console da listelemek istiyorsak
# n => next line : sonraki satıra geçmek için kod
# p => print : istediğin bir değişkenin içini p ile yazdırabilirsin p degisken
# c => continue : programın sona kadar işletilip durdurulmasını sağlar. debugdan çıkar
# hangi değişkenin içini görmek istiyorsan da o değişkenin adını girmen yeterli. ama p degisken olarak kullan sen yine de
# quit() : debug moddan çıkar

import pdb

one = "one"
two = "two"

# pdb.set_trace()

sonuc = one + two
three = "three"
sonuc += three
print(sonuc)


def add_numbers(a, b, c):
    import pdb
    pdb.set_trace()
    return a+b+c

add_numbers(1,6,5)