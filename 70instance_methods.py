"""
--- instance methods : nesneye özel methodlar ---

- init de bir instance method dur. 
- nesneye özel bir metodsa self parametresi alır
"""
import datetime


class Person:

    # yapıcı method (constructor)
    def __init__(self, name, surname, year):

        # object attributes, instance attributes
        self.name = name
        self.surname = surname
        self.year = year

    def intro(self):
        return f"Benim adim {self.name} ve soyadım {self.surname}"

    def calcute_age(self):
        now = datetime.datetime.now().year
        age = now-self.year
        return age


p1 = Person("Gamze", "Ceylan", 2000)
p2 = Person("Zeynep", "Sanver", 2001)

print(p1.intro())
print(p2.intro())

print(p1.calcute_age())