# 1- gönderilern bir string bilgi içinde her karakterin kaçar kez tekrar ettiğini bul

def tekrar(metin):
    return {letter: metin.count(letter) for letter in metin}

# { a: 5, b: 3 } şeklinde döner. listlerdeki mantığın dict hali


print(tekrar("gamzeeeaaaz"))


# 2- list, commandi posiition ve value bilgilerine göre liste üzerinde güncelleme yap

# value = None yazdık çünkü mesela pop işleminde göndermicez
def updateList(liste, command, posiition, value=None):
    if(command == "remove" and posiition == "end"):
        return liste.pop()

    elif (command == "remove" and posiition == "beginning"):
        return liste.pop(0)

    elif (command == "add" and posiition == "end"):
        liste.append(value)
        return liste

    elif(command == "add" and posiition == "beginning"):
        liste.insert(0, value)
        return liste


sonuc = updateList([1, 2, 34, 5], "add", "end", "4")
print(sonuc)


# gönderilen renklerde blue varsa true dönsün

def contains_blue(*args):
    if "blue" in args:
        return True
   # else:
      #  return False

    return False # else yazmasan da burayı çalıştırmak zorunda. onu yazma gereksiz


print(contains_blue("yellow","red","blue"))
print(contains_blue("yellow","red","black","purple","pink"))