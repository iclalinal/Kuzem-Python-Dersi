def kdv_ekle(fiyat, oran=0.20):
    try:
        return fiyat * (1 + oran)
    except TypeError:
        return "Geçersiz fiyat veya oran değeri. Lütfen sayısal bir değer girin."

def gecti_kaldi(sinav_notu):
    return "Gecti" if sinav_notu >= 50 else "Kaldı"