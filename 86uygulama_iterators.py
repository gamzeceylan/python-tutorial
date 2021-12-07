sayilar = [2, 45, 3, 98, 53, 1]
s = "HelloWorld"
# - 1


def my_for(iterator, func):
    iterator = iter(iterator)

    while True:
        try:
            sayi = next(iterator)
            func(sayi)

        except StopIteration:
            break


my_for(sayilar, print)
my_for(s, print)


# - 2. uygulama
def kareal(x):
    print(x*x)


my_for(sayilar,kareal)