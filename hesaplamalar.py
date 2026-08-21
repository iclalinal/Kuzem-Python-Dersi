def kdv_ekle(fiyat, oran=0.20):
    return fiyat * (1 + oran)

def gecti_kaldi(sinav_notu):
    return "Gecti" if sinav_notu >= 50 else "Kaldı"