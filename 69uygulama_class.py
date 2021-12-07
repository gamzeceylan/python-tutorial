class Comment:
    def __init__(self, username, text, likes, dislikes):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislike = dislikes


com1 = Comment("ggmz", "Güzel bir kurs", 50, 25)
com2 = Comment("cyln", "Yararlı bir kurs", 5, 100)
com3 = Comment("zynp", "Muhteşem bir kurs", 89, 1)
com4 = Comment("mtngrg", "comment4", 47, 2)
com5 = Comment("myvss", "comment5", 100, 21)

comment = [com1, com2, com3, com4, com5]

for i in comment:
    print(f"{i.username} : {i.text}")
    print(f"likes : {i.likes}, dislikes : {i.dislike}")
