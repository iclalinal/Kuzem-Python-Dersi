try: 
    yas = int(input("Yaşınızı girin: "))
except ValueError:
    print("Lütfen geçerli bir sayı girin.")

ogrenci = {"isim": "Ahmet"}
try:
    print(ogrenci["not"])
except KeyError:
    print("Öğrencinin not bilgisi yok.")

try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 10 / sayi
except ValueError:
    print("Lütfen geçerli bir sayı girin.")
except ZeroDivisionError:
    print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")

try: 
    sonuc = 10 / 0
except Exception as e:
    print("Bir hata oluştu:", e)