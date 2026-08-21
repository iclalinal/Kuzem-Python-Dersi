import hesaplamalar as hp

fiyat = hp.kdv_ekle(100)
print("Fiyat (KDV dahil):", fiyat)

sinav_notu = 75
durum = hp.gecti_kaldi(sinav_notu)
print("Öğrenci Durumu:", durum)