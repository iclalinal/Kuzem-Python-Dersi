def kitap_ekle(kutuphane, kitap_adi, yazar):
    kutuphane[kitap_adi] = {"yazar": yazar, "musait": True}

def odunc_al(kutuphane, kitap_adi):
    if kitap_adi in kutuphane and kutuphane[kitap_adi]["musait"]:
        kutuphane[kitap_adi]["musait"] = False
        return True
    return False

def kitap_teslim_et(kutuphane, kitap_adi):
    if kitap_adi in kutuphane and not kutuphane[kitap_adi]["musait"]:
        kutuphane[kitap_adi]["musait"] = True
        return True
    return False
