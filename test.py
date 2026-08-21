import istatistik as ist

notlar = ist.random_uret(10)

min_not, max_not, ort_not = ist.istatistik_hesapla(*notlar)
print("Notlar:", notlar)
print(f"Minimum: {min_not}, Maximum: {max_not}, Ortalama: {ort_not}")