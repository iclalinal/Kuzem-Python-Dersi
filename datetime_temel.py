from datetime import datetime

simdi = datetime.now()
print("Şu anki tarih ve saat:", simdi)
print("Yıl:", simdi.year, "Ay:", simdi.month, "Gün:", simdi.day)
print("Saat:", simdi.hour, "Dakika:", simdi.minute, "Saniye:", simdi.second)

print(simdi.strftime("%d/%m/%Y"))