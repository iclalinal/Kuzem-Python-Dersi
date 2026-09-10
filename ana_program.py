class Kitap:
    def __init__(self, ad,yazar,sayfa_sayisi, musait= True):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.musait = musait


kitap1 = Kitap("Simyacı", "Paulo Coelho", 197)
kitap2 = Kitap("Suç ve Ceza", "Fyodor Dostoyevski", 430, False)
print(kitap2.musait)

print(kitap1.ad)
print(kitap1.yazar)