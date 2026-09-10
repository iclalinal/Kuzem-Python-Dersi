import json

class Calisan:
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas

    def bilgi_goster(self):
        print(f"Çalışan Adı: {self.isim}, Maaşı: {self.maas}")

class Yonetici(Calisan):
    def __init__(self, isim, maas, ekip_Boyutu):
        super().__init__(isim, maas)
        self.ekip_Boyutu = ekip_Boyutu

    def bilgi_goster(self):
        super().bilgi_goster()
        print(f"Yönetici Ekip Boyutu: {self.ekip_Boyutu}")

class Muhendis(Calisan):
    def __init__(self, isim, maas, uzmanlik_Alani):
        super().__init__(isim, maas)
        self.uzmanlik_Alani = uzmanlik_Alani

    def bilgi_goster(self):
        super().bilgi_goster()
        print(f"Mühendis Uzmanlık Alanı: {self.uzmanlik_Alani}")

class Satisci(Calisan):
    def __init__(self, isim, maas, satis_Hedefi):
        super().__init__(isim, maas)
        self.satis_Hedefi = satis_Hedefi

    def bilgi_goster(self):
        super().bilgi_goster()
        print(f"Satışçı Satış Hedefi: {self.satis_Hedefi}")


class Sirket:
    def __init__(self,ad):
        self.ad = ad
        self.calisanlar = []

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)

    def listele(self):
        print(f"{self.ad} Şirketinin Çalışanları:")
        for calisan in self.calisanlar:
            calisan.bilgi_goster()

    def calisan_ara(self, isim):
        for c in self.calisanlar:
            if c.isim == isim:
                return c
        return None
    
    def toplam_maas(self):
        toplam = 0
        for c in self.calisanlar:
            toplam += c.maas
        return toplam

    def kaydet(self, dosya_adi):
        veri = []
        for c in self.calisanlar:
            kayit = c.__dict__.copy()
            kayit["tur"] = type(c).__name__
            veri.append(kayit)
        with open(dosya_adi, "w", encoding="utf-8") as f:
            json.dump(veri, f, indent=4, ensure_ascii=False)

    def yukle(self, dosya_adi):
        with open(dosya_adi, "r", encoding="utf-8") as f:
            veri = json.load(f)
            self.calisanlar = []
            for d in veri:
                if d["tur"] == "Yonetici":
                    self.calisanlar.append(Yonetici(d["isim"], d["maas"], d["ekip_Boyutu"]))
                elif d["tur"] == "Muhendis":
                    self.calisanlar.append(Muhendis(d["isim"], d["maas"], d["uzmanlik_Alani"]))
                elif d["tur"] == "Satisci":
                    self.calisanlar.append(Satisci(d["isim"], d["maas"], d["satis_Hedefi"]))
                else:
                    self.calisanlar.append(Calisan(d["isim"], d["maas"]))

    def toplam_satis_hedefi(self):
        toplam = 0
        for c in self.calisanlar:
            if isinstance(c, Satisci):
                toplam += c.satis_Hedefi
        return toplam

    def calisan_sil(self, isim):
        bulunan = self.calisan_ara(isim)
        if bulunan is not None:
            self.calisanlar.remove(bulunan)
            return True
        return False
    
    def dusuk_maasli_sil(self, esik):
        kalanlar = []
        for c in self.calisanlar:
            if c.maas >= esik:
                kalanlar.append(c)
        self.calisanlar = kalanlar

    def calisan_guncelle(self, isim, yeni_maas):
        bulunan = self.calisan_ara(isim)
        if bulunan is not None:
            bulunan.maas = yeni_maas
            return True
        return False

    def unvana_gore_filtrele(self, unvan):
        sonuclar = []
        for c in self.calisanlar:
            if type(c).__name__.lower() == unvan.lower():
                sonuclar.append(c)
        return sonuclar

    def yuksek_maaslilari_getir(self, esik):
        sonuclar = []
        for c in self.calisanlar:
            if c.maas > esik:
                sonuclar.append(c)
        return sonuclar

    def toplam_calisan_sayisi(self):
        return len(self.calisanlar)

    def ortalama_maas(self):
        if self.toplam_calisan_sayisi() == 0:
            return 0
        return self.toplam_maas() / self.toplam_calisan_sayisi()

    def en_yuksek_maasli(self):
        if not self.calisanlar:
            return None
        return max(self.calisanlar, key=lambda c: c.maas)

    def en_dusuk_maasli(self):
        if not self.calisanlar:
            return None
        return min(self.calisanlar, key=lambda c: c.maas)

    def unvana_gore_grupla(self):
        grup = {}
        for c in self.calisanlar:
            unvan = type(c).__name__
            if unvan not in grup:
                grup[unvan] = []
            grup[unvan].append(c)
        return grup

    def unvan_dagılımı(self):
        dagilim = {}
        for c in self.calisanlar:
            unvan = type(c).__name__
            if unvan not in dagilim:
                dagilim[unvan] = 0
            dagilim[unvan] += 1
        return dagilim

    def rapor_olustur(self):
        rapor = f"Şirket Adı: {self.ad}\n"
        rapor += f"Toplam Çalışan Sayısı: {self.toplam_calisan_sayisi()}\n"
        rapor += f"Toplam Maaş: {self.toplam_maas()}\n"
        rapor += f"Ortalama Maaş: {self.ortalama_maas()}\n"
        rapor += f"En Yüksek Maaşlı Çalışan: {self.en_yuksek_maasli().isim} - {self.en_yuksek_maasli().maas}\n"
        rapor += f"En Düşük Maaşlı Çalışan: {self.en_dusuk_maasli().isim} - {self.en_dusuk_maasli().maas}\n"
        rapor += f"Unvan Dağılımı: {self.unvan_dagılımı()}\n"
        return rapor

    def kaydet(self, dosya_adi):
        rapor = self.rapor_olustur()
        with open(dosya_adi, "w", encoding="utf-8") as f:
            f.write(rapor)

sirket = Sirket("ABC Şirketi")

sirket.calisan_ekle(Yonetici("Ahmet", 10000, 5))
sirket.calisan_ekle(Muhendis("Mehmet", 8000, "Yazılım"))
sirket.calisan_ekle(Satisci("Ayşe", 6000, 100))
sirket.calisan_ekle(Calisan("Ali", 5000))
sirket.calisan_ekle(Satisci("Fatma", 7000, 150))



sirket.listele()
print("-"*30)

basarili = sirket.calisan_sil("Ahmet")
print(f"Ahmet silindi mi? {'Evet' if basarili else 'Hayır'}")
print("-"*30)
sirket.listele()
print("-"*30)
sirket.calisan_guncelle("Mehmet", 9000)
print("-"*30)
yuksek_maasli = sirket.yuksek_maaslilari_getir(7000)
print("Yüksek maaşlı çalışanlar:")
for c in yuksek_maasli:
    c.bilgi_goster()

print("-"*30)
print("Çalışanlar maaşa göre sıralı:")
print("-"*30)
print("-"*30)

maasa_gore = sorted(sirket.calisanlar, key=lambda c:c.maas, reverse=True)
for c in maasa_gore:
    print(f"{c.isim} - {c.maas}")


print("-"*30)
print("Çalışanlar isme göre sıralı:")
print("-"*30)
print("-"*30)

isme_gore = sorted(sirket.calisanlar, key=lambda c:c.isim)
for c in isme_gore:
    print(f"{c.isim} - {c.maas}")


print("-"*30)
print(sirket.rapor_olustur())
sirket.kaydet("sirket_raporu.txt")

print("-"*30)
print(f"Toplam çalışan sayısı: {sirket.toplam_calisan_sayisi()}")
print(f"En yüksek maaşlı çalışan: {sirket.en_yuksek_maasli().isim} - {sirket.en_yuksek_maasli().maas}")
print(f"En düşük maaşlı çalışan: {sirket.en_dusuk_maasli().isim} - {sirket.en_dusuk_maasli().maas}")
print(f"Ortalama maaş: {sirket.ortalama_maas()}")

print("-"*30)
print(f"Unvan dağılımı: {sirket.unvan_dagılımı()}")

print("-"*30)
print("-"*30)
print("Unvana göre gruplanmış çalışanlar:")
print("-"*30)

gruplar = sirket.unvana_gore_grupla()
for unvan in gruplar:
    print(f"{unvan}: {len(gruplar[unvan])} çalışan")