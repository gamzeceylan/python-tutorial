"""
- Regular expressions : düzenli iafadelerdir.
- düzenli ifadeler pyhon a özgü değil tüm dillerde nnulunur. 
- dağınık bir metin içeriisnde istediğimiz formattaki metinleri yakalayabilmemizi sağlar
- örneğin e posta adreslerini içinde raham bulunan ya da gmail uzantılı olanlar olarak ayıklamak
için kullanılabilir.
- re olmasaydı bir çok if-else yazmak gerekebilirdi.
- birkaç saatte yapabileceğimiz bir işlemi saniyeleer içinde yerimize yapabiliryor.

"""
import re

result = dir(re)

# ------------ findall() -----------------------
# aradığın ifadeyi bulur ve geriye liste şeklinde kaç tane varsa döndürür
strn = "Python kursu : Python Programlama Rehberiniz | 40 saat"
result = re.findall("Python", strn)

# kaç tane olduğunu öğrenmek için
result = len(result)


# ---------------- split() --------------------
# verdiği karaktere göre o karakteri metin içerisinde bulunca oralarda metni bölüp liste yapar
# '' sadece bunu yazarsak her karakteri böler
result = re.split(' ', strn)


# --------------- sub() ----------------------
# verdiğin karakterleri değiştirir
# \s ve boşluk karaktesi aynı anlama gelir
result = re.sub(" ", "-", strn)
result = re.sub("\s", "-", strn)


# ---------------- search() -----------------
# arama işlemi yapar. match objesi döner.
# match içinde span vardır o da bulunan ifadenin yerini belirtir
# bulduğu ilk degeri döndürür
result = re.search("Python", strn)


# ----------- span()
# search ı çalıştırdıktan sonra da konumunu alabiliriz.
konum = result.span()
print(konum)

# --------------- start() / end()
# start() , search çalıştıktan sonra başladığı indexi verir. yani spanın ilk değerini
# end() de bittiği yeri verir.
baslama = result.start()
bitme = result.end()
print(baslama)
print(bitme)

# --------------- group()
# search ile aradığın ve konumu dönen ifadeyi verir.
arama = result.group()
print(arama)

# --------------- string()
# serch ile nerede aradını döner
ifade = result.string
print(ifade)

print(result)


# ------------------ Regular Expressions ----------------
"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır. ve list döner. zaten findall list döndürür
         [abc] => a      : 1 match : a,b,c yi arar
                  ac     : 2 match 
                  Python : No matches
         [a-e]  => [abcde]  : a,b,c,d,e yi arar 
         [1-5]  => [12345]
         [0-39] => [01239]  :  0 3 arasını arar ve 9 u sona ekler
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""

result = re.findall("[abc]", strn)  # bulduğuu tüm a ları yazar
result = re.findall("[sat]", strn)
result = re.findall("[a-e]", strn)
result = re.findall("[a-z]", strn)
result = re.findall("[0-5]", strn)
result = re.findall("[^abc]", strn)
result = re.findall("[^0-9]", strn)


"""
    . - Her hangi bir tek karakteri belirtir. her . bir basamak
   .. - iki basamaklı ifadelere böler. boşluk da dahil
        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches
    
"""

result = re.findall("...", strn)
result = re.findall("Py..on", strn)  # python lar döner


"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?
    ^a => a:    1 match : ifade a ile başlıyor mu
          abc:  1 match : ifade abc ile başlıyor mu
          bac:  No match

      - tüm metnin başlangıcı ifade edilir. kelime bazlı değil
"""

result = re.findall("^P", strn)  # ["P"] döner
result = re.findall("^K", strn)  # [] döner


"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 
"""

result = re.findall("t$", strn)
result = re.findall("saat$", strn)
result = re.findall("saatt$", strn) # [] döner



"""
(anlamadım)

     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.
 
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("sa*t", strn)

"""
(anlamadım)

     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa+t", strn)

"""
(anlamadım)

    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.
        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa?t", strn)

"""
    {} - Karakter sayısını kontrol eder.
        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}", strn)
result = re.findall("[0-9]{2}", strn)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

"""
    () - gruplamak için kullanılır.
         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""


"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?
    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50
    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""

"""
-RE leri ezberlemek zorunnda değilsin. ihtiyacın olduğunda gidip dokumana bakarsın.
- önemli olan en başta yazılanları kullanabilmek

"""

print(result)
