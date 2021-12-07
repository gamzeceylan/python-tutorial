# Inheritance : Kalıtım
# base class , parent class : temel sınıf, türetilen sınıf
# child class : türeyen sınıf

# örneğin hayvan sınıfından evcil hayvan ve vahşi hayvan sınıdından türetilir.
# kuş kedi, evcil hayvan sınııfndan türetilir.
# aslan kaplan, vahşi hayvan sınıfından türetilir.
# türeyen nesneler türetilen sınıfın özelliklerine sahip olur

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi")

    def intro(self):
        print(self.name, self.surname, self.age)


class Student (Person):
    pass


class Teacher (Person):
    pass


# s1 = Student()

# nesne türetilirken __init__ çağrıldığı için ve sturdent ve teacher Persondan
# kalıtıldığı için s1 ve t1 nesneleri de Person ın parametrelerini ister

p1 = Person("Ahmet", "Ceylan", 45)
# print(p1.name, p1.surname, p1.age)
p1.intro()

s1 = Student("Hasan", "Koluk", 24)
# print(s1.name, s1.surname, s1.age)
s1.intro()

t1 = Teacher("Kemal", "Yılmaz", 38)
# print(t1.name, t1.surname, t1.age)
t1.intro()

# hepsinde de "person nesnesi türetildi" yazar
