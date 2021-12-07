"""
-list içine dictionary yazabilirsin

players = [
    {},
    {}
]

-böyle yaptıktan sonra list içine append ile dictionary eklersin 

-ya da dic içine dic tanımlayıp update ile güncelleme yaparsın

"""

# ------ 1.yol------------
# dic ile
players = {}

id = input("Oyuncu id : ")
name = input("Oyuncu ad : ")
nationality = input("Oyuncu ülke : ")
yearOfBirth = input("Oyuncu doğum yılı : ")
current_team = input("Oyuncu takım : ")
history = input("Oyuncu oynadığı yerler : ")

players.update({
    id: {
        "name": name,
        "nationality": nationality,
        "yearOfBirth": yearOfBirth,
        "current_team": current_team,
        "history": history.split(',')  # dikkat et dizi içinde tutuldu
    }
})

print(players)

# --------2. yol---------------------
# liste ile. emin değilim?????
players2 = []

id = input("Oyuncu id : ")
name = input("Oyuncu ad : ")
nationality = input("Oyuncu ülke : ")
yearOfBirth = input("Oyuncu doğum yılı : ")
current_team = input("Oyuncu takım : ")
history = input("Oyuncu oynadığı yerler : ")

players2.append({
    id= {
        "name": name,
        "nationality": nationality,
        "yearOfBirth": yearOfBirth,
        "current_team": current_team,
        "history": history.split(',')  # dikkat et dizi içinde tutuldu
    }
})
