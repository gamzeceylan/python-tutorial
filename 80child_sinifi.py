
class Person:
    # kalıtılan tüm nesneler için çalışıcak
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi")

    def intro(self):
        print(self.name, self.surname, self.age)


"""
class Student (Person):
 
     def __init__(self):
     print("student nesnesi türetildi")


    def __init__(self, name, surname, age, number):
        # tekrar parametreleri set etmene gerek yok. bunu Person sınıfı yapıcak oraya gönder
        Person.__init__(self, name, surname, age)

        self.number = number
        print("student nesnesi türetildi")
"""


class Student(Person):

    def __init__(self, name, surname, age, number):
        # tekrar parametreleri set etmene gerek yok. bunu Person sınıfı yapıcak oraya gönder
        # Person. ve self yerine direkt super() yazabilirsin. aynı anlama gelir
        super().__init__(name, surname, age)

        self.number = number
        print("student nesnesi türetildi")

    def intro(self):
        print(f"{self.name} {self.number}")

    def study(self):
        print(f"{self.number} isimli ogrenci ders çalışıyor")


class Teacher (Person):
    def __init__(self, name, surname, age, branch):
        Person.__init__(self, name, surname, age)
        self.branch = branch

    def teach(self):
        print(f"{self.name} {self.surname} isimli öğrentmen ders veriyor")

# nesneler türetildiği anda eğer kendi sınıflarında bir init metodu yoksa base sınıfın init i çalışır.
# ama kendi sınıflarında bir init varsa base sınıfın initi ezilir ve child sınıfınınki çalışır
# o yüzden base class ta verdiğin attribute leri child class ın initinde de vermelisin


p1 = Person("Ahmet", "Ceylan", 45)
p1.intro()


# s1 = Student("Hasan", "Koluk", 24)
s1 = Student("Hasan", "Koluk", 24, "123535")
print(s1.number)
s1.intro()  # Person intro metodu ezilmiş olmalı. student intro çalışmalı. çünkü son yazılan diğerini ezer
s1.study()

t1 = Teacher("Kemal", "Yılmaz", 38, "Bilgisayar")
t1.intro()
t1.teach()
