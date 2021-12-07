# hata gelebilecek kısım yani işlemleerimiz => try
# hata alınırsa düşülecek metot, hata tipleri => except
# except kısmında özel hatalar oluşturabiliriz.
"""
except ZeroDivisionError :     0 hatası oluşursa burada yakalanır
except ValueError :            hatalı bir tip girerse burada yakalanır
except :                       özellemediğimiz tüm hatalarda buraya düşer

"""

# - Hataları sınıflandırabiliriz
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)

except ZeroDivisionError:
    print("sıfır kullanı hatası")

except ValueError:
    print("giriş hatası")

except:
    print("bilinmeyen bir hata")

"""


# - Birlikte de kullanabiliriz
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)

except (ZeroDivisionError,ValueError):
    print("sıfır kullanı hatası")

except:
    print("bilinmeyen bir hata")


"""

# --------------- as ---------------------------
# - as ile hataları kaydedebiliriz, yazdırabiliriz, kullanabilirz
# tüm hatalar Exception dan türetilmiştir. exception da olan özellikler alınıp özelleştirilmiştir.
# exception da object den türemiştir
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)

except (ZeroDivisionError, ValueError) as e:
    print("hata")
    print(e)

except Exception as e:
    print("bilinmeyen bir hata")
    print(e)

"""

# ---------------------- else -------------------------
# herhangi bir except bloğu işletişmezde else çalıştırılabilirz
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)

except (ZeroDivisionError, ValueError) as e:
    print("hata")
    print(e)

except Exception as e:
    print("bilinmeyen bir hata")
    print(e)

else:
    print("Her şey yolunda")

"""

# else bloğunu döngülerde kullanabiliriz

# except lere girmezse else giricek eğer exceptlere giriyorsa hata alırız else girmez ve döngü hata almadan açlışındaya kadar devam eder.
# else giryorsa hata almadık demektir ve durur

while True:
    try:
        x = int(input("X : "))
        y = int(input("y : "))
        print(x/y)

    except (ZeroDivisionError, ValueError) as e:
        print("Hata oluştu")
        print(e)

    except Exception as e:
        print("bilinmeyen bir hata")
        print(e)

    else:
        break


# ---------------- finally -----------------------------
# try cath blokları çalışsın ya çalışmasın mutlaka finally ye girer. hata alsa da almasa da girer
# örneğin veri tabanına bağlandıktan sonra bir vt kapatma işlemini burada yapabilirsin.

while True:
    try:
        x = int(input("X : "))
        y = int(input("y : "))
        print(x/y)

    except (ZeroDivisionError, ValueError) as e:
        print("Hata oluştu")
        print(e)

    except Exception as e:
        print("bilinmeyen bir hata")
        print(e)

    else:
        break

    finally:
        print("finally çalıştı")
