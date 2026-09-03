try:
    with open('gunluk.txt', 'r') as dosya:
        print("Önceki kayitlar:")
        for satir in dosya:
            print(satir.strip())
except FileNotFoundError:
    print("ilk kaydınız")

yeni_giris = input("Yeni kaydınızı giriniz: ")
with open('gunluk.txt', 'a') as dosya:
    dosya.write(yeni_giris + '\n')