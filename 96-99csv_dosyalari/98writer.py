from csv import writer, reader

# tekil halde ekleme
"""
with open("cars.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Marka","Model"]) #başlık kısmı
    csv_writer.writerow(["Toyota","Yaris"])
    csv_writer.writerow(["Toyota","Corolla"])
"""

# coğul halde ekleme
"""
with open("cars.csv","w") as file:
    csv_writer = writer(file)
    # her satır listenin bir liste elemenı
    csv_writer.writerows([["Marka","Model"],["Toyota","Yaris"],["Toyota","Corolla"]])
"""

# eleman ekleme
"""
with open("cars.csv","a") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Toyota","Rav4"])
"""

# dosya içinden başka dosyaya yazma
"""
with open("products.csv") as file:
    csv_reader = reader(file)
    with open("new-products.csv","w") as file:
        csv_writer = writer(file)
        for product_row in csv_reader:
            csv_writer.writerow([p.upper() for p in product_row])
"""

# aynı dosya içine yazma
with open("products.csv","r+") as file:
    csv_reader = reader(file)
    csv_writer = writer(file)
    next(csv_reader)
    products = [[p[0],float(p[1])*1.2,p[2],p[3],p[4]] for p in csv_reader]
    file.seek(0)
    csv_writer.writerow(["ProductName","Price","IsPublished","Category","Reviews"])
    csv_writer.writerows(products)