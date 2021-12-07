# bir öncekinde listeler ile çaışıyorduk
# dictreader ile her veri key ve value ile erişilebilir olucak. aynı dict gibi

# import csv
from csv import DictReader

with open("products.csv") as file:
               csv_reader=DictReader(file)
               print(csv_reader) # dictreader objesi döner. artık dönen lis değil dct

               # her satır key ve value olarak döner. başlık bilgisi ilgili değerlere key olarak dağıtılmıştır
               """
               for d in csv_reader:
                              print(d)
               """
               # key ile çok daha kolay bilgilere ulaşırsın
               # artık index bilmemize gerek yok
               for d in csv_reader:
                              print(d["ProductName"], d["Price"])


"""

NOT : veriler , ile değil de | veya - ile ayrılmış olabilir. (bir virgül seçip ctrl shift l 
basarsan hepsi seçilir. toplu olarak değiştirebilirsin).
o zaman delimiter ile karakteri belirtmen gerekir
csv_reader=DictReader(file, delimiter="|") yazabilirsin. hata almazsın

"""