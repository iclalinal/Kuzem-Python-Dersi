import csv

# Öğrenci verilerini içeren liste
ogrenciler = [["isim","ders","not"],["Ali","Matematik",90],["Ayşe","Fizik",85],["Mehmet","Kimya",78],["Fatma","Biyoloji",92],["Ahmet","Tarih",88]]

with open("ogrenciler.csv", "w", newline="",encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerows(ogrenciler)

print("ogrenciler.csv dosyası oluşturuldu ve veriler yazıldı.")

with open("ogrenciler.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.DictReader(dosya)
    satirlar = list(okuyucu)

for satir in satirlar:
    print(satir)

print("ogrenciler.csv dosyasındaki veriler okundu ve ekrana yazdırıldı.")

print("\n85 ve üzeri not alan öğrenciler:")
basarili_ogrenciler = [s for s in satirlar if int(s['not']) >= 85]
for s in basarili_ogrenciler:
    print(f"- {s['isim']} ({s['not']})")

print("\n Oratalama notu hesaplanıyor...")

notlar =[int(s['not']) for s in satirlar]
ortalama = sum(notlar) / len(notlar)
print(f"Ortalama not: {ortalama:.2f}") 