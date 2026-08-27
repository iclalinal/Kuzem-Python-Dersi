import kutuphane_islemleri as k_i
from datetime import datetime

kutuphane = {}

k_i.kitap_ekle(kutuphane, "Sefiller", "Victor Hugo")
k_i.kitap_ekle(kutuphane, "Suç ve Ceza", "Fyodor Dostoyevski")

basarili = k_i.odunc_al(kutuphane, "Sefiller")
if basarili:
    print(basarili, datetime.now().strftime("%d-%m-%Y"), "Sefiller kitabı ödünç alındı.")

basarisiz = k_i.odunc_al(kutuphane, "Sefiller")
if basarisiz:
    print(basarili, datetime.now().strftime("%d-%m-%Y"), "Sefiller kitabı ödünç alındı.")
else:
    print("Sefiller kitabı ödünç alınamadı, zaten ödünç verilmiş.")
