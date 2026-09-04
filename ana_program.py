import json

def kitap_kaydet(kutuphane, dosya_adi):
    with open(dosya_adi,"w", encoding="utf-8") as dosya:
        json.dump(kutuphane, dosya, ensure_ascii=False, indent=4)


kutuphane = {"kitaplar": ["simyacı", "suç ve ceza", "savaş ve barış", "1984", "hayvan çiftliği"], "toplam": 2}
kitaplar = kutuphane["kitaplar"]

kitap_kaydet(kitaplar, "kutuphane.json")
