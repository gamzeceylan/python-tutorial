# json içinde ya {} içinde (dict) ya da [] (list) içinde veriler olmalı

# birden fazla data ekleyeceksen diz içine almalısın
"""
data = {
    "userName": "gamzeceylan",
    "firsName": "Gamze",
    "lastName": "Ceylan"
}

import json

with open("users.json", "w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
"""

import json

"""
data = [
    {
        "userName": "gamzeceylan",
        "firsName": "Gamze",
        "lastName": "Ceylan"

    },
    {
        "userName": "gamzeceylan",
        "firsName": "Gamze",
        "lastName": "Ceylan"

    },
    {
        "userName": "gamzeceylan",
        "firsName": "Gamze",
        "lastName": "Ceylan"

    }
]


with open("users.json", "w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

"""

# yeni bilgi ekleme

user = {

    "userName": "salihaborin",
    "firsName": "Saliha",
    "lastName": "CBoreylan"

}

# önce dosyayı açalım okuyalım ve users ı alalım. bize bir dizi dönücek.
# bilgiyi de users içine ekleyelim
with open("users.json") as file:
    users = json.load(file)

users.append(user)  # append ettik şimdi de dosyaya users ı yazalım


with open("users.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)


# bilgileri ekranda görebiliriz
for i in users:
    print(i)


# güncelleme

for user in users:
    if user["userName"] == "gamzeceylan":
        user["userName"] = "gamze_ceylan"

with open("users.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)


# silme

users.remove(users[0])

with open("uses.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)


