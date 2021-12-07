class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Şuan aktif users sayısı : {cls.active_users}"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1

    def full_name(self):
        return f"{self.firstname} {self.lastname}"


class Morderator(User):

    active_moderators = 0

    @classmethod
    def display_active_modetators(cls):
        return f"Şu anda aktif moderators sayısı : {Morderator.active_moderators}"

    def __init__(self, firstname, lastname, community):
        super().__init__(firstname, lastname)
        self.community = community
        Morderator.active_moderators += 1


    def remove_post(self):
        return f"{self.full_name()} {self.community} grubundan bir post sildi"


u1 = User("Ali", "Korkmaz")

m1 = Morderator("Gamze", "Ceylan", "yazılım")

# -------- isinstance ---------
# u1, User dan mı türedi ?
sonuc = isinstance(u1, User)  # true
sonuc = isinstance(m1, User)  # true
sonuc = isinstance(u1, Morderator)  # false
print(sonuc)


print(m1.full_name())

print(m1.remove_post())

print(User.display_active_users())
print(Morderator.display_active_modetators())

