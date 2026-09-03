with open("notlar.txt", "r") as dosya:
    icerik = dosya.read()
    print("Dosya içeriği:\n", icerik)

print("\nDosya satır satır okunuyor:")

with open("notlar.txt", "r") as dosya:
    for satir in dosya:
        temiz = satir.strip()  # Satırın başındaki ve sonundaki boşlukları temizle
        if temiz:  # Eğer satır boş değilse
            print(temiz)