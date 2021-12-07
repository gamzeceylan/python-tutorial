"""
- öğrendiğimiz liste tipleri : list, tuple, dicrionary
- sets ler yine {} arasına tanımlanır ama key değeri verilmez
- sets ler indexlenemez ce sıralanamaz
- her çalıştırdığında farklı sırada karşına gelir.
- eğer eklenen elemanların index değerleri önemsizse sets kullan çünkü elemanlar karışık sıralanır.
- index önemsizse sets kullanmak daha performansı arttırır.
- tek tek elemanlara ulaşamayız

- index önemli değilse, üzerine bir eleman ekleyeceksek ama var olanı değiştirmeyeceksek sets kullanabiliriz.
ama üzerinde hiçbir işlem yapmayacaksak da tuples kullanırız

"""
meyveler = {"elma", "kiraz", "kavun", "üzüm"}

#-------------- Ekrana yazdırma ------------------
print(meyveler)

for x in meyveler:
    print(x)

# sonuc = meyveler[0] indexlenemez

#--------------- Arama -------------------------
sonuc = "elma" in meyveler  # arama yapılabilir


#------------------- Ekleme -----------------------------
meyveler.add("karpuz")  # yeni bir bilgi eklenebilir
meyveler.update({"kivi","muz","üzüm"}) #çoklu ekleme de yapılabilir. ama üzüm olduğundan tekrar eklenmez


#--------------------- Uzunluk ---------------------------
sonuc= len(meyveler) #eleman sayısını alabilirirz

#------------------------ Silme ----------------------------
meyveler.remove("karpuz") #silme yapabiliriz. eğer bilgi bulunmazsa hata alırız
meyveler.discard("karpuzz") #discard da girilen değeri siler. eğer değer bulunzmazsa hata vermez

meyveler.pop() #liste karışık olduğu için hangi elemanın silineceği bilinemez

meyveler.clear() #komple silinir

print(sonuc)
print(meyveler)

#------------------------- Birleştirme --------------------------
baharatlar={"kimyon","tuz","un","şeker"}
sebzeler={"ıspanak","lahana","domates","biber","şeker"}

sonuc=sebzeler.union(baharatlar)
#listeler birleştirilir. aynı değerler varsa tekrarlanmazz bir kere yazılrı
print(sonuc)
 