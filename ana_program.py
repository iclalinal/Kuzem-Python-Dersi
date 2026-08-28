# try: 
#     yas = int(input("Yaşınızı girin: "))
# except ValueError:
#     print("Lütfen geçerli bir sayı girin.")

# ogrenci = {"isim": "Ahmet"}
# try:
#     print(ogrenci["not"])
# except KeyError:
#     print("Öğrencinin not bilgisi yok.")

# try:
#     sayi = int(input("Bir sayı girin: "))
#     sonuc = 10 / sayi
# except ValueError:
#     print("Lütfen geçerli bir sayı girin.")
# except ZeroDivisionError:
#     print("Sıfıra bölme hatası! Lütfen sıfırdan farklı bir sayı girin.")

# try: 
#     sayi = int(input("Bir sayı girin: "))
#     sonuc = 10 / sayi
#     print("Sonuç:", sonuc)
# except Exception as e:
#     print("Bir hata oluştu:", e)


# import hesaplamalar

# print(hesaplamalar.kdv_ekle(100, 0.18))
# print(hesaplamalar.kdv_ekle("aa", 0.18))

# while True:
#     try:
#         yas = int(input("Yaşınızı girin: "))
#         break
#     except ValueError:
#         print("Lütfen geçerli bir sayı girin.")

# print("Yaşınız:", yas)


# def guvenli_bol(a, b):
#      try:
#          sonuc = a / b
#      except ZeroDivisionError:
#          return "Sıfıra bölünemez"
#      except TypeError:
#          return "Geçersiz veri tipi"
#      else:
#          return sonuc

# print(guvenli_bol(10, 2))
# print(guvenli_bol(10, 0))  
# print(guvenli_bol(10, "a"))  


# while True:
#     try:
#         sayi = int(input("Bir sayı girin: "))
#         if 1 <= sayi <= 100:
#             print("Geçerli bir sayı girdiniz:", sayi)
#             break
#         else:
#             print("Lütfen 1 ile 100 arasında bir sayı girin.")
#     except ValueError:
#         print("Lütfen geçerli bir sayı girin.")
#     else:
#         print("Hata oluşmadı, sayıyı başarıyla aldık.")

# print("Program sonlandı.")


# def yas_kontrol(yas):
#     if yas < 0:
#         raise ValueError("Yaş negatif olamaz.")
#     elif yas < 18:
#         return "Reşit değilsiniz."
#     else:
#         return "Reşitsiniz."

# try:
#     print(yas_kontrol(-5))
# except ValueError as e:
#     print("Hata:", e)


def kayit_yap(isim, yas):
    if yas < 0 or yas > 120:
        raise ValueError("Geçersiz yaş değeri.")
    print(f"{isim} kaydı başarıyla yapıldı. Yaş: {yas}")

kayit_yap("Ahmet", -5)  # Geçerli yaş