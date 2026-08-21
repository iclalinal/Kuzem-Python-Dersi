import hesaplamalar

fiyat = float(input("Fiyatı girin: "))
kdv_dahil_fiyat = hesaplamalar.kdv_ekle(fiyat)
print("Fiyat (KDV dahil):", kdv_dahil_fiyat)


print("Not 45:", hesaplamalar.gecti_kaldi(45))