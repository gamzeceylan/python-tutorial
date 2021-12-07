"""
- bazı metotlar ve attribute ler nesne seviyesindedir ve üretilen her nesne için özeldir
- ama bazen nesne seviyesinde değil class seviyesinde metod üretmek isteyebiliriz. ve ürettiğimiz
bu metot tüm nesneler için aynı oldun isteriz. örneğin bir bankada faiz oranı herkes için %1,8 olmalı gibi

-nesne seviyesinde metotlar self alırdı

- class seviyesindeki attribute ler sınıf adlarıyla çağrılırlar.
"""


class User:

    # class seviyesinde bir özellik tanımlıyoruz. bu artık nesneye özel değil
    active_users = 0

    def __init__(self, first, last, age):
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

print(userA.full_name())
print(userB.full_name())

# sınıf adı ile class seviyesindekileri çağırırız. nesne ile değil
print(User.active_users)

print(userA.logout())  # active_users 1 azalmalı
print(User.active_users)
