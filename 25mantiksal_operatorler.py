# ------ And operatorü -------

x = 10
sonuc = 5 < x < 15  # true döner ama aslında iki sorguyu barındırıyor.
sonuc = (5 < x) and (x < 15)  # true döner
# true and true => ture
# true and false => false
# false and false => false

print(sonuc)

# ----------- Or operatörü -----------------

sonuc = (x < 2) or (x % 2 == 0)
# true or true => ture
# true or false => true
# false or false => false

print(sonuc)

# ------ not operatorü -----------------
# tersine çevirir.

sonuc = not(x > 5)  # false döner
print(sonuc)


# ------ x, 1 - 10 arasında bir çift sayı mı ? --------

sonuc = ((1 < x) and (x < 10)) and (x % 2 == 0)
print(sonuc)
