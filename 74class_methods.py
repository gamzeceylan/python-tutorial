"""
- class seviyesinde attribute tanımlayabildiğimiz gibi metod da tanımlayabiliriz.
- clas seviyesindeki metodların basına @classmethod eklemelisin
- nesne seviyesindeki metodlara verdiğin self ve class seviyesindeki metotlara verdiğin cls
her zaman en başta yazılan parametreler olmalıdır. adına başka şeyler de diyebilirsin ama en başta
tanımlanmalı

- class metodlarının yoğun olarak kullanıldığı yer :
örneğin nesneler init içinde oluşturuluyor. init te oluşturmak yerine class seviyesinde bir metod
ile oluşturabiliriz

"""


class User:

    active_users = 0


    # class seviyesindeki bir metodla nesne oluşturmak. init e parametre göndermeden
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        # geriye bir nesne oluşturur. o yüzden return cls demelisin
        return cls(first, last, age)
        # cls() ve Users() aynı şeydir hangisini yazdığın farketmez

    @classmethod  # bunu eklemelisin
    def display_active_users(cls):

        # return print(cls)  # class ekrana yazdırılıcak
        return f"{cls.active_users} tane aktif kullanıcı var"

    def __init__(self, first, last, age):
        print(self)  # nesne ekrana yazdırılıcak
        self.first = first
        self.last = last
        self.age = age

        User.active_users += 1  # her nesne oluştuğunda aktif kullanıcıyı 1 arttırıyoruz

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çıkış yaptı"


userA = User("Gamze", "Ceylan", 21)
userB = User("Beyza", "Yılmaz", 34)
userc = User("Gamze", "Ceylan", 21)
userd = User("Beyza", "Yılmaz", 34)

# class seviyesindeki metotlara yine sınıf adıyla ulaşırız.

# print(User.display_active_users())


User.from_string("Melek,Uysal,43") # yine bir nesne oluştu
"""
- dict {"key": "value"}
bunu böyle oluşturmak yerine dict.fromkey(p) de bir dict oluşturur. 
from_string ona karşılık geliyor gibi düşün

"""