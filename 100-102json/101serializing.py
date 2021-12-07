# ------- serialize ----------------
# uygulama tarafında olan bir objeyi dosya formatına yani json a çevirmek
# elimizdeki dict yapısındak json bilgisini başka uygulamaya göndermeden önce serialize etmen gerekir
# objeyi str olarak gönderemezsin. json türüne çevirmen gerekir

import json

person = {
               "firstName":"Sadık",
               "lastName":"Turan",
               "hobbies":["spor","sinema"],
               "age":37,
               "children":[
                              {
                                             "firstName":"Çınar",
                                             "age":3
                              }
               ]
}


# bilgiyi göndermeden json türüne çevirelim

#---- dumps ------ 
# str türünü json a çevirir
# dosyaya json kayıt ederken de de dump kullanırsın !

print(type(person)) # dict yapısında

##sonuc=json.dumps(person, ensure_ascii=False,indent=2) # str türüne çevrildi
#  ensure_ascii=False karakter kodlamasınında sıkıntı çıkmaması için
# indent=2 indent vermezsen dict yapısında grünür ama vererek json yapısında görünmesini sağlarsın
# ama tabili gerçek uygulamalarda tek satırda yazılması daha az yer kaplayacağından daha avantajlı olur

##print(type(sonuc)) # str yapısına çevrildi

##print(sonuc)

# dosyaya bilgi kaydetme 

with open("person.json","w") as file:
               json.dump(person,file,ensure_ascii=False,indent=2)

