"""
- python modunda tek tek çalıştırırsan görüceksin ki dosya okunduktan
sonra dosya içine bir şeyler yazp kaydettiğin zaman ve kaldırdığın yerden dosyayı çalıştırmaya
devam edersen yeni yazdıkların da okunur.
- bir alta geçilen her satırın başında \n okunur.
- cmd de python çalıştırırken print kullanmana gerek yok zaten ekrandasın
- dosya içinde her karakterin bir index numarası vardır.

"""

f = open("metin.txt")

#------- seek() ----------
# dosyayı en sonra kadar okuduktan sonra en başa dönmek istersen kullanılır
# seek() içine gitmek istediğin yerin index numarasını alır cursor oraya gider ve cursorun olduğu index no yu döner
# f.seek(5) indexi 5 olan yere gider ve geriye 5 döner.
# dosyayı okuyup başa dönnmek istediğinde .seek(0) çalıştırmalısın
 
satir=f.readline()
print(f.seek(5))

#------- readline() ---------
# satır sonuna kadar okur

satir= f.readline()
print(satir) # sadece ilk satır döner

#----- readlines() -----------
# satırları tek tek alır ve liste olarak döner

satirlar= f.readlines()
print(satirlar)
print(satirlar[2]) # kaçındı indexteki satırı istiyorsan yazdırabilirsin

#---------- closed() --------------
# dosya kapalı mı diye sorar.

sonuc=f.closed
print(sonuc) # kapatmadığımız için false döner


#------ close() ----------
# dosya açıkken bellekte yer kaplar. kullandıktan sonra mutlaka kapatmalısın.

f.close() # dosyayı kapattık
sonuc=f.closed
print(sonuc) # true döner 

# kapalı olan dosyada okuma işlemlerini yapamazsın

# readable() ne işe yarıyor ???