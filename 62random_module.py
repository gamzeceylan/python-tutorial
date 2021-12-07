import random
"""
result = dir(random)  # mevcut fonk ulaşmak için
result = help(random)  # tek tek nası kullanıldıklarına ulaşmak için
result = help(random.random) # özel bir metodun nası kullanıldığını öğrenmek için

"""

# ---- ranstege bir sayı üretme : random() ------------
# random() bir aralık belirtmezsen 0.0 ile 1.0 arasında sayılar üretir
result = random.random()  # float döner


# --------- random.uniform(x,y) -----------------------
# belirtilen aralıkta bir sayı üretir
result = random.uniform(10, 20)  # belirtilen aralıkta float sayı üretir
result = int(random.uniform(10, 20))  # int e çevirebiliriz


# --------- randint() -------------------------
# belirtilen aralıkta direkt int sayı üretir
result = random.randint(10, 20)
print(result)


# ------ örnek ------
names = ["ali", "hasan", "isa", "musa", "cenk"]
result = names[random.randint(0, len(names)-1)]  # -1 eklemezsen taşma olur
print(result)

# ------ choice() -------
# choie() , tukarıdaki gibi len -1 falan ile uğraşmadan otomadik dizi içinden bir eleman secer
result = random.choice(names)
print(result)

greeting = "hello my name is gamze"
result = random.choice(greeting)
print(result)

# ---------- shuffle() ----------
# liste içindeki elemanları karıştırmak için kullanılır
#elemanların liste içinde olması gerekir
liste = list(range(10))
print(liste)  # sırasıyla yazılır

random.shuffle(liste)
print(liste)  # artık karışık gelir.


# --------- sample() ---------------
# verdiğin sayıda herhangi bir eleman getirir
# elemanların kiste içinde olmasına gerek yok zaten liste veriyorsun onun üzerinden karıştırıyor

liste = range(100)
#herhangi 3 elemn getirir.
# #liste=list(range(100)) yazmasan da kendi otomatik listeye çevirir
result = random.sample(liste, 3) 
print(result)
