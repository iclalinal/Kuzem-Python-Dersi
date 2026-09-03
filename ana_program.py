import csv
ogrenciler = [
    ["Ali", 85],
    ["Ayşe", 90],
    ["Mehmet", 78],
    ["Fatma", 92],
]

with open("notlar.csv","w", newline="") as dosya:
    yazici =csv.writer(dosya)
    yazici.writerow(["Ad","Not"])
    yazici.writerows(ogrenciler)


with open("notlar.csv","r", newline="") as dosya:
    okuyucu = csv.reader(dosya)
    baslik = next(okuyucu)  # Başlık satırını atla
    for satir in okuyucu:
        print(satir)