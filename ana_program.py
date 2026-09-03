import csv

kitaplar = [["simyacı","paulo coelho", 1988], ["sineklerin tanrısı", "william golding", 1954], ["1984", "george orwell", 1949]]

with open("kitaplar.csv","w", newline="") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["Kitap Adı", "Yazar", "Yayın Yılı"])
    yazici.writerows(kitaplar)


alanlar = ["ad", "yazar","musait"]
with open("kutuphane.csv","w", newline="") as dosya:
    yazici = csv.DictWriter(dosya, fieldnames=alanlar)
    yazici.writeheader()
    yazici.writerow({"ad": "simyacı", "yazar": "paulo coelho", "musait": True})

with open("kutuphane.csv","r", newline="") as dosya:
    okuyucu = csv.DictReader(dosya)
    for satir in okuyucu:
        print(satir)