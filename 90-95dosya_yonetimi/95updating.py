# with open("markalar.txt","a") as file:
#                file.write("6-BMW")

# update yapmak için hem okuman hem yazman gerekiyor. o yüzden r+ modunda aç

# başa ekleme
"""
with open("markalar.txt", "r+", encoding="utf-8") as file:
    markalar = file.read()
    markalar = "1-Toyota\n" + markalar
    file.seek(0)  # kursoru en başa almalısın
    file.write(markalar)

"""

# ortaya ekleme
with open("markalar.txt","r+",encoding="utf-8") as file:
               markalar=file.readlines() # satır satır diziye attık
               markalar.insert(2,"3-Renault\n") # satır sonu olunda elemanlar \n ile kaydediliyor
               file.seek(0)
               file.writelines(markalar) # writelines satıt satır yazdırır


