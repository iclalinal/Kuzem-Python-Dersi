import json

veri = {"kitaplar": ["simyacı", "suç ve ceza", "savaş ve barış", "1984", "hayvan çiftliği"], "toplam": 2}
metin = json.dumps(veri)
geri = json.loads(metin)
print(geri)
print(geri["kitaplar"], type(geri["toplam"]))