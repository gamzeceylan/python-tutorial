"""
- *args tuple döner () arasına yazar
- **kwargs dict döner {} arasına yazar

def fonk1(*args):
    print(type(args))
    print(args)


def fonk2(**kwargs):
    print(type(kwargs))
    print(kwargs)

fonk1()
fonk2()

"""

# aşağıda sözlük veri yapısı oluşur. tek tek istediğimmiz parametreleri yollayabiliriz


def displayUser(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} {value}")

    print("\n")


displayUser(username="gamzecyln", email="gmz.com")
displayUser(username="sdkturan", email="sadik.com", telefon="0123")


def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


myFunc(10, 21, 45, 32, 43, 7, 89, 32, key1="key1", key2="key2", key3="key3")
